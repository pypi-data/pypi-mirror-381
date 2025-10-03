import sys
from types import ModuleType
from . import core
from .core import builtins,__builtins__
__version__ = "9.6.19"
try:
    original_builtins_dict = builtins.copy()
    __builtins__ = ProtectedBuiltinsDict(original_builtins_dict)
    builtins = __builtins__
except Exception:
    pass
try:
    core.__dict__ = ProtectedBuiltinsDict(core.__dict__)
except Exception as e:
    pass
public_objects = []
for name in dir(core):
    if not name.startswith("_"):
        obj = getattr(core, name)
        if isinstance(obj, (type, ModuleType)) or callable(obj):
            public_objects.append(name)
__all__ = public_objects + ["__version__","__builtins__","core","builtins"]
globals().update({
    name: getattr(core, name)
    for name in public_objects
})

