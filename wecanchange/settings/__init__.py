from .base import *

# local settings
try:
    from .local import *
except:
    pass

# stage settings
try:
    from .stage import *
except:
    pass

# preview settings
try:
    from .preview import *
except:
    pass

# production settings
try:
    from .production import *
except:
    pass