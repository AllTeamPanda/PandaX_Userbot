
from Panda.core.logger import logging
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from . import edit_delete, edit_or_reply, ilhammansiz_cmd, HEROKU_APP_NAME, HEROKU_API_KEY, Config
from ..core.data import _sudousers_list
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = _sudousers_list()

cmd = Config.COMMAND_HAND_LER

plugin_category = "plugins"
LOGS = logging.getLogger(__name__)


@ilhammansiz_cmd(
    pattern="sudo$",
    command=("sudo", plugin_category),
    info={
        "header": "To enable sudo of your Pandauserbot.",
        "description": "Initially all sudo commands are disabled, you need to enable ",
        "usage": "{tr}sudo",
    },
)
async def sudo(event):
    sudo = "True" if _sudousers_list() else "False"
    users = sudousers
    listsudo = users.replace(" ", "\n» ")
    if sudo == "True":
        await edit_or_reply(
            event,
            f"🔮 **Sudo:** `Enabled`\n\n📚 ** List Sudo Users:**\n» {listsudo}\n\n**SUDO_COMMAND_HAND_LER:** `{Config.SUDO_COMMAND_HAND_LER}`",
        )
    else:
        await edit_delete(event, "🔮 **Sudo:** `Disabled`")



@ilhammansiz_cmd(
    pattern="addsudo(?:\s|$)([\s\S]*)",
    command=("addsudo", plugin_category),
    info={
        "header": "To add user as your sudo.",
        "usage": "{tr}addsudo <username/reply/mention>",
    },
    allow_sudo=False,
)
async def sudore(event):
    ok = await edit_or_reply(event, "Prosessing...")
    vars = "SUDO_USERS"
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await ok.edit(f"Reply to a user.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = target
    await ok.edit(f"Menambahkan  `{target}` sedang merestart di heroku tunggu 2-3 min.")
    heroku_var[vars] = newsudo



@ilhammansiz_cmd(
    pattern="delsudo(?:\s|$)([\s\S]*)",
    command=("delsudo", plugin_category),
    info={
        "header": "To add user as your sudo.",
        "usage": "{tr}addsudo <username/reply/mention>",
    },
    allow_sudo=False,
)
async def _(event):
    suu = event.text[8:]
    xxx = await edit_or_reply(event, "`Processing...`")
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            xxx,
            "Balas ke pengguna atau berikan user id untuk menghapusnya dari daftar pengguna sudo Anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            xxx, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus pengguna sudo**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu != "" and suu.isnumeric():
        target = suu
    elif reply:
        target = await get_user(event)
    gett = str(target)
    if gett in sudousers:
        newsudo = sudousers.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{target}` **dari Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "SUDO_USERS"
        heroku_Config[var] = newsudo
    else:
        await edit_delete(
            xxx, "**Pengguna ini tidak ada dalam Daftar Pengguna Sudo anda.**", 45
        )


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    return replied_user.user.id
