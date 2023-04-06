import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

#postgresql://[name of the user]:[password]@localhost/[name of the database]
# DATABASE_URL = "postgresql://postgres:password@localhost/fastapi_database"
# DATABASE_URL = "postgresql://postgresUser:postgresPW@localhost:5455/postgresDB"
DATABASE_URL = "postgresql://matijaUser:matijaPassword@localhost:5455/matijaDatabase"

engine= _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = _declarative.declarative_base()