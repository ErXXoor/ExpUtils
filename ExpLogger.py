
from loguru._logger import Logger as _Logger
from loguru._logger import Core as _Core

__all__ = ["exp_logger"]

exp_logger = _Logger(
    core=_Core(),
    exception=None,
    depth=0,
    record=False,
    lazy=False,
    colors=False,
    raw=False,
    capture=True,
    patchers=[],
    extra={},
)
