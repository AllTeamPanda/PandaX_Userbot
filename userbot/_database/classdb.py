from ..sql_helper.database.afk_sql import AFKSQL
from ..sql_helper.database.dv_sql import DVSQL
from ..sql_helper.database.filters_sql import FILTERSSQL
from ..sql_helper.database.notes_sql import NOTESSQL
from ..sql_helper.database.pmpermit_sql import PMPERMITSQL
from ..sql_helper.database.welcome_sql import WELCOMESQL


class Database(AFKSQL, NOTESSQL, PMPERMITSQL, DVSQL, WELCOMESQL, FILTERSSQL):
    pass
