from __future__ import annotations

import base64
import importlib
import json
import os
from abc import ABC, abstractmethod
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from types import ModuleType
from typing import ClassVar

DEFAULT_REQUIRED_KEYS: tuple[str, ...] = (
    "uri",
    "username",
    "password",
)
DEFAULT_OPTIONAL_KEYS: tuple[str, ...] = (
    "database",
)


class CredentialProviderError(RuntimeError):
    """Raised when credentials cannot be retrieved securely."""


class BaseCredentialProvider(ABC):
    """Common behaviour for all credential providers."""

    name: ClassVar[str]

    def __init__(
        self,
        required_keys: Iterable[str] = DEFAULT_REQUIRED_KEYS,
        optional_keys: Iterable[str] | None = DEFAULT_OPTIONAL_KEYS,
    ) -> None:
        self.required_keys = tuple(required_keys)
        self.optional_keys = tuple(optional_keys or ())

    @property
    def expected_keys(self) -> tuple[str, ...]:
        """Return the ordered credential keys to collect."""
        return self.required_keys + self.optional_keys

    def get_credentials(self) -> dict[str, str]:
        """Return validated credential values."""
        raw_credentials = self._collect_credentials()
        missing = [
            key
            for key in self.required_keys
            if not self._has_value(raw_credentials.get(key))
        ]
        if missing:
            message = (
                "Missing required credential fields: "
                f"{', '.join(sorted(missing))}"
            )
            raise CredentialProviderError(message)
        credentials: dict[str, str] = {}
        for key, value in raw_credentials.items():
            if key not in self.expected_keys:
                continue
            if not self._has_value(value):
                continue
            credentials[key] = str(value)
        return credentials

    @staticmethod
    def _has_value(value: object | None) -> bool:
        """Return True when value is meaningfully populated."""
        if value is None:
            return False
        if isinstance(value, str) and value.strip() == "":
            return False
        return True

    @abstractmethod
    def _collect_credentials(self) -> Mapping[str, object | None]:
        """Retrieve raw credential values prior to validation."""


class EnvironmentVariableCredentialProvider(BaseCredentialProvider):
    """Load credentials from environment variables."""

    name = "environment"

    def __init__(
        self,
        variable_mapping: Mapping[str, str] | None = None,
        *,
        environment: Mapping[str, str] | None = None,
        required_keys: Iterable[str] = DEFAULT_REQUIRED_KEYS,
        optional_keys: Iterable[str] | None = DEFAULT_OPTIONAL_KEYS,
    ) -> None:
        super().__init__(required_keys, optional_keys)
        self.environment = environment or os.environ
        self.variable_mapping = self._build_mapping(variable_mapping or {})

    def _build_mapping(
        self,
        overrides: Mapping[str, str],
    ) -> dict[str, str]:
        mapping: dict[str, str] = {}
        for key in self.expected_keys:
            mapping[key] = f"NEO4J_{key.upper()}"
        mapping.update(overrides)
        return mapping

    def _collect_credentials(self) -> Mapping[str, object | None]:
        credentials: dict[str, object | None] = {}
        for key in self.expected_keys:
            env_key = self.variable_mapping.get(key)
            if env_key is None:
                continue
            credentials[key] = self.environment.get(env_key)
        return credentials


@dataclass(slots=True)
class _HashicorpAuth:
    token: str | None = None
    role_id: str | None = None
    secret_id: str | None = None

    def ensure_valid(self) -> None:
        has_token = BaseCredentialProvider._has_value(self.token)
        has_approle = (
            BaseCredentialProvider._has_value(self.role_id)
            and BaseCredentialProvider._has_value(self.secret_id)
        )
        if not has_token and not has_approle:
            raise CredentialProviderError(
                "HashiCorp Vault provider requires either a token "
                "or AppRole credentials (role_id and secret_id).",
            )


class HashicorpVaultCredentialProvider(BaseCredentialProvider):
    """Retrieve credentials stored in HashiCorp Vault."""

    name = "hashicorp_vault"

    def __init__(
        self,
        url: str,
        path: str,
        *,
        auth_token: str | None = None,
        role_id: str | None = None,
        secret_id: str | None = None,
        mount_point: str = "secret",
        verify: bool | str | None = None,
        field_mapping: Mapping[str, str] | None = None,
        client: object | None = None,
        required_keys: Iterable[str] = DEFAULT_REQUIRED_KEYS,
        optional_keys: Iterable[str] | None = DEFAULT_OPTIONAL_KEYS,
    ) -> None:
        super().__init__(required_keys, optional_keys)
        self.url = url
        self.path = path
        self.mount_point = mount_point
        self.verify = verify
        self.field_mapping = dict(field_mapping or {})
        self._client = client
        self._auth = _HashicorpAuth(
            token=auth_token,
            role_id=role_id,
            secret_id=secret_id,
        )
        if self._client is None:
            self._auth.ensure_valid()

    def _import_hvac(self) -> ModuleType:
        try:
            return importlib.import_module("hvac")
        except ModuleNotFoundError as exc:
            raise CredentialProviderError(
                "HashiCorp Vault support requires the 'hvac' package.",
            ) from exc

    def _build_client(self) -> object:
        if self._client is not None:
            return self._client
        hvac = self._import_hvac()
        client = hvac.Client(
            url=self.url,
            token=self._auth.token,
            verify=self.verify,
        )
        if not BaseCredentialProvider._has_value(self._auth.token):
            client.auth.approle.login(
                role_id=self._auth.role_id,
                secret_id=self._auth.secret_id,
            )
        return client

    def _collect_credentials(self) -> Mapping[str, object | None]:
        client = self._build_client()
        try:
            response = client.secrets.kv.v2.read_secret_version(
                path=self.path,
                mount_point=self.mount_point,
            )
        except Exception as exc:  # pragma: no cover - passthrough
            raise CredentialProviderError(
                f"Unable to read Vault secret at '{self.path}'.",
            ) from exc
        data = response.get("data", {}).get("data", {})
        if not isinstance(data, Mapping):
            raise CredentialProviderError(
                "Vault secret payload is not a mapping.",
            )
        credentials: dict[str, object | None] = {}
        for key in self.expected_keys:
            source_key = self.field_mapping.get(key, key)
            credentials[key] = data.get(source_key)
        return credentials


class AwsSecretsManagerCredentialProvider(BaseCredentialProvider):
    """Retrieve credentials from AWS Secrets Manager."""

    name = "aws_secrets_manager"

    def __init__(
        self,
        secret_id: str,
        *,
        region_name: str | None = None,
        profile_name: str | None = None,
        field_mapping: Mapping[str, str] | None = None,
        session: object | None = None,
        required_keys: Iterable[str] = DEFAULT_REQUIRED_KEYS,
        optional_keys: Iterable[str] | None = DEFAULT_OPTIONAL_KEYS,
    ) -> None:
        super().__init__(required_keys, optional_keys)
        self.secret_id = secret_id
        self.region_name = region_name
        self.profile_name = profile_name
        self.field_mapping = dict(field_mapping or {})
        self._session = session

    def _import_boto3(self) -> ModuleType:
        try:
            return importlib.import_module("boto3")
        except ModuleNotFoundError as exc:
            raise CredentialProviderError(
                "AWS Secrets Manager support requires the 'boto3' package.",
            ) from exc

    def _build_session(self) -> object:
        if self._session is not None:
            return self._session
        boto3 = self._import_boto3()
        return boto3.session.Session(profile_name=self.profile_name)

    def _collect_credentials(self) -> Mapping[str, object | None]:
        session = self._build_session()
        client = session.client(
            "secretsmanager",
            region_name=self.region_name,
        )
        try:
            response = client.get_secret_value(SecretId=self.secret_id)
        except Exception as exc:  # pragma: no cover - passthrough
            raise CredentialProviderError(
                f"Unable to read AWS secret '{self.secret_id}'.",
            ) from exc
        payload = self._decode_secret_payload(response)
        credentials: dict[str, object | None] = {}
        for key in self.expected_keys:
            source_key = self.field_mapping.get(key, key)
            credentials[key] = payload.get(source_key)
        return credentials

    def _decode_secret_payload(self, response: Mapping[str, object]) -> dict[str, object]:
        if "SecretString" in response:
            raw_value = response["SecretString"]
            if not isinstance(raw_value, str):
                raise CredentialProviderError(
                    "AWS secret string payload must be text.",
                )
            try:
                parsed = json.loads(raw_value)
            except json.JSONDecodeError:
                return {"value": raw_value}
            if isinstance(parsed, Mapping):
                return dict(parsed)
            raise CredentialProviderError(
                "AWS secret string payload is not JSON object.",
            )
        if "SecretBinary" in response:
            raw_binary = response["SecretBinary"]
            decoded = base64.b64decode(raw_binary)
            if isinstance(decoded, bytes):
                decoded_text = decoded.decode("utf-8")
            else:
                decoded_text = decoded
            try:
                parsed = json.loads(decoded_text)
            except json.JSONDecodeError as exc:
                raise CredentialProviderError(
                    "AWS binary secret payload must contain JSON.",
                ) from exc
            if isinstance(parsed, Mapping):
                return dict(parsed)
            raise CredentialProviderError(
                "AWS binary secret payload is not JSON object.",
            )
        raise CredentialProviderError(
            "AWS secret response did not contain recognised payload.",
        )
