from nf_common_base.b_source.common.infrastructure.nf.objects.registers.nf_verse_registers import (
    NfVerseRegisters,
)


class NfMultiverseRegisters(
    NfVerseRegisters
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
