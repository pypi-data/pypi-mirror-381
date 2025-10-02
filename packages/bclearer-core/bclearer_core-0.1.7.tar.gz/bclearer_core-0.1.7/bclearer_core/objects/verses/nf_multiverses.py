from nf_common_base.b_source.common.infrastructure.nf.objects.verses.nf_verses import (
    NfVerses,
)


class NfMultiverses(NfVerses):
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
