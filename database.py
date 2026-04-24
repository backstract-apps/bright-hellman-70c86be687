

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-ed6ce8034bdc421d8318b23f8ccca033-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzYxNjEyMjEsInAiOnsicm9hIjp7Im5zIjpbIjAxOWQ4Yjc1LTViMDEtNzQ1Ny05Yzk0LTI3NDc2MWM4NjUyZiJdfSwicnciOnsibnMiOlsiMDE5ZDhiNzUtNWIwMS03NDU3LTljOTQtMjc0NzYxYzg2NTJmIl19fSwicmlkIjoiNzNmNzQ1ZTQtM2RlYy00MWNhLWFkZjAtZWI0NDM2NzQ2M2YxIn0.hVqMz4rjInDT4FmnTMOCgJAXVqzIjbHRK-jpMBu9XGKDZB72_g2GBl3BnRVZqbNPt6glUV0Je9cKTvrxXzDsAg",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

