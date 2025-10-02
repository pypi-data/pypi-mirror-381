import sys

import bclearer_interop_services.graph_services.cozodb_service.object_models as cozodb_object_models

sys.modules["cozodb_object_models"] = (
    cozodb_object_models
)
