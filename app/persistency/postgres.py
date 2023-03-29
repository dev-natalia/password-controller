from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .. import settings


engine = create_engine(settings.DB_URL_USER, pool_pre_ping=True)

Base = declarative_base()