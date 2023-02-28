from .url_database import pyDatabase
pdB = pyDatabase()



gvarstatus = pdB.get_key
addgvar = pdB.set_key
delgvar = pdB.del_key
