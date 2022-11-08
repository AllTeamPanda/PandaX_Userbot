from . import fonts
from . import memeshelper as pandamemes
from .aiohttp_helper import AioHttp
from .utils import *

flag = True
check = 0
while flag:
    try:
        from .chatbot import *
        from .functions import *
        from .memeifyhelpers import *
        from .progress import *
        from .qhelper import process
        from .tools import *
        from .utils import _format, _pandatools, _pandautils

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break

from .containers import Containers
from .datavars import DataVars
from .decorators import Decorators
from .filters import *
from .functions import Functions


class Helpers(Containers, Functions, Decorators, DataVars):
    pass
