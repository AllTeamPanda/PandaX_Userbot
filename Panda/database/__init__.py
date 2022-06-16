
from .aktif import *
from .mongodb import mongodb

mongo_client = mongodb()

db_x = mongo_client["PandaX_Userbot"]
