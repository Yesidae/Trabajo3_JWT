from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL")
SCHEMA = os.getenv("DB_SCHEMA")

print("DATABASE_URL:", DATABASE_URL)  # 👈 prueba

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no se está cargando. Revisa el .env")

engine = create_engine(DATABASE_URL)

metadata = MetaData(schema=SCHEMA)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base(metadata=metadata)