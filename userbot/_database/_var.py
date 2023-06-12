import os


from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    STRING_SESSION = os.environ.get(
        "SESSION", None)
    VC_SESSION = STRING_SESSION
    MONGO_URI = os.environ.get("MONGO_URI", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    REDIS_URI = os.environ.get("REDIS_URI", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
    REDISHOST = os.environ.get("REDISHOST", None)
    REDISPORT = os.environ.get("REDISPORT", None)
    REDISUSER = os.environ.get("REDISUSER", None)
    STRING_SESSION2 = os.environ.get("SESSION2") or None
    STRING_SESSION3 = os.environ.get("SESSION3") or None
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    DATABASE_URL = DB_URI
    STRING_SESSION4 = os.environ.get("SESSION4") or None
    STRING_SESSION5 = os.environ.get("SESSION5") or None
    STRING_SESSION6 = os.environ.get("SESSION6") or None
    STRING_SESSION7 = os.environ.get("SESSION7") or None
    STRING_SESSION8 = os.environ.get("SESSION8") or None
    STRING_SESSION9 = os.environ.get("SESSION9") or None
    STRING_SESSION10 = os.environ.get("SESSION10") or None
    STRING_SESSION11 = os.environ.get("SESSION11") or None
    STRING_SESSION12 = os.environ.get("SESSION12") or None
    STRING_SESSION13 = os.environ.get("SESSION13") or None
    STRING_SESSION14 = os.environ.get("SESSION14") or None
    STRING_SESSION15 = os.environ.get("SESSION15") or None
    STRING_SESSION16 = os.environ.get("SESSION16") or None
    STRING_SESSION17 = os.environ.get("SESSION17") or None
    STRING_SESSION18 = os.environ.get("SESSION18") or None
    STRING_SESSION19 = os.environ.get("SESSION19") or None
    STRING_SESSION20 = os.environ.get("SESSION20") or None
    STRING_SESSION21 = os.environ.get("SESSION21") or None
    STRING_SESSION22 = os.environ.get("SESSION22") or None
    STRING_SESSION23 = os.environ.get("SESSION23") or None
    STRING_SESSION24 = os.environ.get("SESSION24") or None
    STRING_SESSION25 = os.environ.get("SESSION25") or None
    STRING_SESSION26 = os.environ.get("SESSION26") or None
    STRING_SESSION27 = os.environ.get("SESSION27") or None
    STRING_SESSION28 = os.environ.get("SESSION28") or None
    STRING_SESSION29 = os.environ.get("SESSION29") or None
    STRING_SESSION30 = os.environ.get("SESSION30") or None
    STRING_SESSION31 = os.environ.get("SESSION31") or None
    STRING_SESSION32 = os.environ.get("SESSION32") or None
    STRING_SESSION33 = os.environ.get("SESSION33") or None
    STRING_SESSION34 = os.environ.get("SESSION34") or None
    STRING_SESSION35 = os.environ.get("SESSION35") or None
    STRING_SESSION36 = os.environ.get("SESSION36") or None
    STRING_SESSION37 = os.environ.get("SESSION37") or None
    STRING_SESSION38 = os.environ.get("SESSION38") or None
    STRING_SESSION39 = os.environ.get("SESSION39") or None
    STRING_SESSION40 = os.environ.get("SESSION40") or None
    STRING_SESSION41 = os.environ.get("SESSION41") or None
    STRING_SESSION42 = os.environ.get("SESSION42") or None
    STRING_SESSION43 = os.environ.get("SESSION43") or None
    STRING_SESSION44 = os.environ.get("SESSION44") or None
    STRING_SESSION45 = os.environ.get("SESSION45") or None
    STRING_SESSION46 = os.environ.get("SESSION46") or None
    STRING_SESSION47 = os.environ.get("SESSION47") or None
    STRING_SESSION48 = os.environ.get("SESSION48") or None
    STRING_SESSION49 = os.environ.get("SESSION49") or None
    STRING_SESSION50 = os.environ.get("SESSION50") or None
    VC_STRING_SESSION3 = os.environ.get("VC_SESSION3") or None
    VC_STRING_SESSION2 = os.environ.get("VC_SESSION2") or None
    VC_STRING_SESSION = os.environ.get("VC_SESSION") or None
    
    VC_STRING_SESSION4 = os.environ.get("VC_SESSION4") or None
    VC_STRING_SESSION5 = os.environ.get("VC_SESSION5") or None
    VC_STRING_SESSION6 = os.environ.get("VC_SESSION6") or None
    VC_STRING_SESSION7 = os.environ.get("VC_SESSION7") or None
    VC_STRING_SESSION8 = os.environ.get("VC_SESSION8") or None
    VC_STRING_SESSION9 = os.environ.get("VC_SESSION9") or None
    VC_STRING_SESSION10 = os.environ.get("VC_SESSION10") or None
    VC_STRING_SESSION11 = os.environ.get("VC_SESSION11") or None
    VC_STRING_SESSION12 = os.environ.get("VC_SESSION12") or None
    VC_STRING_SESSION13 = os.environ.get("VC_SESSION13") or None
    VC_STRING_SESSION14 = os.environ.get("VC_SESSION14") or None
    VC_STRING_SESSION15 = os.environ.get("VC_SESSION15") or None
    VC_STRING_SESSION16 = os.environ.get("VC_SESSION16") or None
    VC_STRING_SESSION17 = os.environ.get("VC_SESSION17") or None
    VC_STRING_SESSION18 = os.environ.get("VC_SESSION18") or None
    VC_STRING_SESSION19 = os.environ.get("VC_SESSION19") or None
    VC_STRING_SESSION20 = os.environ.get("VC_SESSION20") or None
    VC_STRING_SESSION21 = os.environ.get("VC_SESSION21") or None
    VC_STRING_SESSION22 = os.environ.get("VC_SESSION22") or None
    VC_STRING_SESSION23 = os.environ.get("VC_SESSION23") or None
    VC_STRING_SESSION24 = os.environ.get("VC_SESSION24") or None
    VC_STRING_SESSION25 = os.environ.get("VC_SESSION25") or None
    VC_STRING_SESSION26 = os.environ.get("VC_SESSION26") or None
    VC_STRING_SESSION27 = os.environ.get("VC_SESSION27") or None
    VC_STRING_SESSION28 = os.environ.get("VC_SESSION28") or None
    VC_STRING_SESSION29 = os.environ.get("VC_SESSION29") or None
    VC_STRING_SESSION30 = os.environ.get("VC_SESSION30") or None
    VC_STRING_SESSION31 = os.environ.get("VC_SESSION31") or None
    VC_STRING_SESSION32 = os.environ.get("VC_SESSION32") or None
    VC_STRING_SESSION33 = os.environ.get("VC_SESSION33") or None
    VC_STRING_SESSION34 = os.environ.get("VC_SESSION34") or None
    VC_STRING_SESSION35 = os.environ.get("VC_SESSION35") or None
    VC_STRING_SESSION36 = os.environ.get("VC_SESSION36") or None
    VC_STRING_SESSION37 = os.environ.get("VC_SESSION37") or None
    VC_STRING_SESSION38 = os.environ.get("VC_SESSION38") or None
    VC_STRING_SESSION39 = os.environ.get("VC_SESSION39") or None
    VC_STRING_SESSION40 = os.environ.get("VC_SESSION40") or None
    VC_STRING_SESSION41 = os.environ.get("VC_SESSION41") or None
    VC_STRING_SESSION42 = os.environ.get("VC_SESSION42") or None
    VC_STRING_SESSION43 = os.environ.get("VC_SESSION43") or None
    VC_STRING_SESSION44 = os.environ.get("VC_SESSION44") or None
    VC_STRING_SESSION45 = os.environ.get("VC_SESSION45") or None
    VC_STRING_SESSION46 = os.environ.get("VC_SESSION46") or None
    VC_STRING_SESSION47 = os.environ.get("VC_SESSION47") or None
    VC_STRING_SESSION48 = os.environ.get("VC_SESSION48") or None
    VC_STRING_SESSION49 = os.environ.get("VC_SESSION49") or None
    VC_STRING_SESSION50 = os.environ.get("VC_SESSION50") or None
    


class Database(object):
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    SESSION = os.environ.get("SESSION", None)
    SESSION2 = os.environ.get("SESSION2", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    PyroSESSION = os.environ.get("PyroSESSION", None)
    MONGO_DB = Var.MONGO_URI
    PyroSESSION2 = os.environ.get("PyroSESSION2", None)
    PyroSESSION3 = os.environ.get("PyroSESSION3", None)
    PyroSESSION4 = os.environ.get("PyroSESSION4", None)
    DB_URIl = os.environ.get("DATABASES_URL", "mongodb+srv://petercord:b38DJZL3X6zhnHJ0@cluster0.e9xau.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    PyroBOT_TOKEN = os.environ.get("PyroBOT_TOKEN", None)
 
