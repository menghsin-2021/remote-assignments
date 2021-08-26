import pymysql.cursors

# Connect to the database
import pymysql



def connect_db(host, user, password, db_name=None, port=3306):
    try:
        connect_db = pymysql.connect(host=host,
                                     port=port,
                                     user=user,
                                     password=password,
                                     database=db_name,)
        return connect_db
    except pymysql.MySQLError as e:
        print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        return None

def create_db(cursor, DBNAME):
    # create database
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4' ".format(DBNAME)
        )
    except Exception as e:
        print("Exeception occured:{}".format(e))

    # use database
    try:
        cursor.execute("USE {}".format(DBNAME))
    except Exception as e:
        print("Exeception occured:{}".format(e))

    return cursor

def create_tb(cursor, TABLES, TBNAME=None):
    TABLES[TBNAME] = ("CREATE TABLE IF NOT EXISTS {}( \
        `id` int(11) NOT NULL AUTO_INCREMENT, \
        `email` varchar(255) COLLATE utf8_bin NOT NULL, \
        `password` varchar(255) COLLATE utf8_bin NOT NULL, \
        PRIMARY KEY (`id`) \
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1;".format(TBNAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
            print("OK")
        except Exception as e:
            print("Exeception occured:{}".format(e))










