from nf_common_base.b_source.common.infrastructure.nf.objects.registries.nf_verse_registries import (
    NfVerseRegistries,
)


class NfMultiverseRegistries(
    NfVerseRegistries
):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback,
    ):
        pass
