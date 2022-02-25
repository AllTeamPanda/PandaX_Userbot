from sys import version_info
from .Config import Config
from git import Repo

__Tgl__ = 25
__Bln__ = 02
__Thn__ = 2022


__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "PandaX_UserBot <https://github.com/ilhammansiz/PandaX_Userbot>"
__copyright__ = "PandaX_UserBot Copyright (©) 2020 - 2021  " + __author__


def get_version() -> str:
    """ version """
    repo = Repo()
    repo.remote(Config.UPSTREAM_REMOTE).fetch()
    ver = f"{__Tgl__}.{__Bln__}.{__Thn__}"
    if "/ilhammansiz/pandax_userbot" in Config.UPSTREAM_REPO.lower():
        diff = list(repo.iter_commits(f'v{ver}..HEAD'))
        if diff:
            ver = f"{ver}-patch.{len(diff)}"
    else:
        diff = list(repo.iter_commits(
            f'{Config.UPSTREAM_REPO}/master..HEAD'))
        if diff:
            ver = f"{ver}-custom.{len(diff)}"
    return ver + '@' + repo.active_branch.name
