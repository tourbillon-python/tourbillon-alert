import sys

PY34_PLUS = sys.version_info[0] == 3 and sys.version_info[1] >= 4

if PY34_PLUS:
    from .alert.alert import *
else:
    from .alert2.alert import *
