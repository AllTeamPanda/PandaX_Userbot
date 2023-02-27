
# Credits: @robotrakitangakbagus, @diemmmmmmmmmm
# FROM PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport



from .._database import DatabaseCute
SqL = DatabaseCute()



getdb = SqL.getdb 
setdb = SqL.setdb 
deldb = SqL.deldb

def usname():
    name = "Database SQL https://elephantsql.com/"
    return name

def ping():
    is_database_working = False
    return is_database_working
