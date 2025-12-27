from gsuid_core.logger import logger

def __getattr__(name):
    if name == "WuWaCalc":
        try:
            from ..waves_build.wuwacalc import WuWaCalc
            globals()["WuWaCalc"] = WuWaCalc
            return WuWaCalc
        except ImportError:
            return None
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")