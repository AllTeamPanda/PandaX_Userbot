from pyrogram.raw.functions.photos import DeletePhotos, UploadProfilePhoto

DeletePhotosRequest = DeletePhotos
UploadProfilePhotoRequest = UploadProfilePhoto

from Panda import STORAGE, SqL
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import edit_or_reply, get_text, get_user

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False



OWNER = SqL.getdb("OWNERS") or ""
BIO = SqL.getdb("BIO") or ""




@ilhammansiz_on_cmd(
    ["clone"],
    cmd_help={
        "help": "Cloning",
        "example": "{ch}clone username/reply to user",
    },
)
async def clone(client, message):
  text = get_text(message)
  op = await edit_or_reply(message, "`Cloning`")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await op.edit("`Whom i should clone:(`")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**From now I'm** __{f_name}__")
    

@ilhammansiz_on_cmd(
    ["unclone"],
    cmd_help={
        "help": "Cloning",
        "example": "{ch}unclone username/reply to user",
    },
)
async def revert(client, message):
 await message.edit("`Reverting`")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("`I am back!`")

