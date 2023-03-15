from subprocess import run



__pversion__ = "`@main`."
__version_code__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "0"
)

__version__ = __pversion__ + __version_code__

panda_version = __version__



from sys import version_info



branch = f"@main"


__Tgl__ = "26"
__Bln__ = "02"
__Thn__ = "2023"


__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "PandaX_UserBot <https://github.com/ilhammansiz/PandaX_Userbot>"
__copyright__ = "PandaX_UserBot Copyright (©) 2020 - 2021  " + __author__


versi = f"{__Tgl__}.{__Bln__}.{__Thn__}"

