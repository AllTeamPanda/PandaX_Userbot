
# Credits: @robotrakitangakbagus, @diemmmmmmmmmm
# FROM PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport



from .._database import pyDatabase
SqL = pyDatabase()



getdb = SqL.get_key
setdb = SqL.set_key
deldb = SqL.del_key

def usname():
    name = "Database SQL https://elephantsql.com/"
    return name

def ping():
    is_database_working = False
    return is_database_working
