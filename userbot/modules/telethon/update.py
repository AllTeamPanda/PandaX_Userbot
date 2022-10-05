##
from ... import LOGS, __version__
from . import PandaBot, edit_or_reply
import asyncio
from base64 import b64decode

try:
    from git import Repo
    from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
except ImportError:
    Repo = None

plugin_category = "modules"

async def gen_chlog(repo, diff):
    """Generate Changelogs..."""
    UPSTREAM_REPO_URL = b64decode("aHR0cHM6Ly9naXRodWIuY29tL2lsaGFtbWFuc2l6L1BhbmRhWF9Vc2VyYm90").decode("utf-8")
    ac_br = repo.active_branch.name
    ch_log = tldr_log = ""
    ch = f"<b>PandaUserbot {__version__} updates for <a href={UPSTREAM_REPO_URL}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"PandaUserbot {__version__} updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b><a href={UPSTREAM_REPO_URL.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log



async def updater():
    try:
        off_repo = b64decode("aHR0cHM6Ly9naXRodWIuY29tL2lsaGFtbWFuc2l6L1BhbmRhWF9Vc2VyYm90").decode("utf-8")
    except Exception as er:
        LOGS.exception(er)
        return
    try:
        repo = Repo()
    except NoSuchPathError as error:
        LOGS.info(f"`directory {error} is not found`")
        Repo().__del__()
        return
    except GitCommandError as error:
        LOGS.info(f"`Early failure! {error}`")
        Repo().__del__()
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    repo.create_remote("upstream", off_repo) if "upstream" not in repo.remotes else None
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)



async def bash(cmd, run_code=0):
    """
    run any command in subprocess and get output or error."""
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip() or None
    out = stdout.decode().strip()
    if not run_code and err:
        split = cmd.split()[0]
        if f"{split}: not found" in err:
            return out, f"{split.upper()}_NOT_FOUND"
    return out, err







@PandaBot.ilhammansiz_cmd(
    pattern="update(| now)?$",
    command=("update", plugin_category),
    info={
        "header": "To update userbot.",
        "description": "I recommend you to do update deploy atlest once a week.",
        "options": {
            "now": "Will update bot but requirements doesnt update.",
            "deploy": "Bot will update completly with requirements also.",
        },
        "usage": [
            "{tr}update now",
            "{tr}update deploy",
        ],
    },
)
async def _(e):
    xx = await edit_or_reply(e, "memulai Update....")
    panda = e.pattern_match.group(1).strip()
    if panda == "deploy":
        await updater()
        await bash("git pull -f && pip3 install -r requirements.txt")
        await xx.edit("Update perlahan tapi pasti")
        os.execl(sys.executable, "python3", "-m", "userbot")
        return
    if panda == "now":
        m = await updater()
        os.execl(sys.executable, "python3", "-m", "userbot")
        branch = (Repo.init()).active_branch
        if m:
            x = await edit_or_reply(e, "Update..")
            Link = x.message_link
            await xx.edit(
                f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
                parse_mode="html",
                link_preview=False,
            )
        else:
            await xx.edit(
                f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/ilhammansiz/PandaX_Userbot/tree/{branch}">[{branch}]</a></strong>',
                parse_mode="html",
                link_preview=False,
            )
