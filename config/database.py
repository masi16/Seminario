from database import database_config

name = "src_db"
user = "root"
password = "S4guridadTotal!"
port = 3306
host = "localhost"

databaseURL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"

database_config["SRC_DB"] = {
    "NAME": name,
    "USER": user,
    "PASSWORD": password,
    "PORT": port,
    "HOST": host
}
database_config["SRC_DB_URL"] = databaseURL