from nf_common_base.b_source.services.b_dictionary_service.objects.b_dictionaries import (
    BDictionaries,
)


class RowBDictionaries(BDictionaries):
    def __init__(
        self, dictionary: dict
    ):
        super().__init__()

        self.dictionary = dictionary
