# ilham mansiz
# Panda
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# the secret configuration specific things
from PandaX_Userbot import DB_URI


def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print("DB_URI is not configured. Features depending on the database might have issues.")
    print(str(e))



from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric


class Snips(BASE):
    __tablename__ = "snips"
    snip = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        snip, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.snip = snip
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference


Snips.__table__.create(checkfirst=True)


def get_snips(keyword):
    try:
        return SESSION.query(Snips).get(keyword)
    except:
        return None
    finally:
        SESSION.close()


def get_all_snips():
    try:
        return SESSION.query(Snips).all()
    except:
        return None
    finally:
        SESSION.close()


def add_snip(keyword, reply, snip_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(Snips).get(keyword)
    if adder:
        adder.reply = reply
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Snips(keyword, reply, snip_type, media_id,
                      media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_snip(keyword):
    note = SESSION.query(Snips).filter(Snips.snip == keyword)
    if note:
        note.delete()
        SESSION.commit()




from telethon import events, utils
from telethon.tl import types

from PandaX_Userbot import petercordpanda_bot as bot
from PandaX_Userbot import Stark
from Configs import Config


TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2





@Stark.on(events.NewMessage(pattern=r"\#(\S+)"))
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if snip:
        if snip.snip_type == TYPE_PHOTO:
            media = types.InputPhoto(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        elif snip.snip_type == TYPE_DOCUMENT:
            media = types.InputDocument(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        else:
            media = None
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        await Stark.send_message(
            event.chat_id, snip.reply, reply_to=message_id, file=media
        )


@Stark.on(
    events.NewMessage(pattern="^/save ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def _(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {"type": TYPE_TEXT, "text": msg.message or ""}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip["type"] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip["type"] = TYPE_DOCUMENT
            if media:
                snip["id"] = media.id
                snip["hash"] = media.access_hash
                snip["fr"] = media.file_reference
        add_snip(
            name,
            snip["text"],
            snip["type"],
            snip.get("id"),
            snip.get("hash"),
            snip.get("fr"),
        )
        await event.reply(
            "Note {name} saved successfully. Get it with #{name}".format(name=name)
        )
    else:
        await event.reply("Reply to a message with `snips keyword` to save the snip")


@Stark.on(events.NewMessage(pattern="^/notes"))
async def on_snip_list(event):
    all_snips = get_all_snips()
    OUT_STR = "Available Snips:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"➤ `#{a_snip.snip}` \n"
    else:
        OUT_STR = "No Snips. Start Saving using `/addnote`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "snips.text"
            await Stark.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
    else:
        await event.reply(OUT_STR)


@Stark.on(
    events.NewMessage(pattern="^/clearnote (\S+)", func=lambda e: e.sender_id == bot.uid)
)
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.reply("Note #{} deleted successfully".format(name))
    

