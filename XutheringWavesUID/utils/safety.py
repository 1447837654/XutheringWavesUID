from gsuid_core.logger import logger
try:
    from .waves_build.safety import *
except ImportError:
    logger.warning("无法导入 safety，将尝试下载")
    