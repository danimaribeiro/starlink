import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext import declarative


Base = declarative.declarative_base()

# Base.metadata.bind = session_registry.primary.engine


class SpaceTrack(Base):
    __tablename__ = "space_track"

    eid = sa.Column(sa.String(64), nullable=False, primary_key=True)
    name = sa.Column(sa.String(64), nullable=False)
    created_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    epoch = sa.Column(sa.DateTime, nullable=False)
    longitude = sa.Column(sa.Float, nullable=True)
    latitude = sa.Column(sa.Float, nullable=True)
    velocity_kms = sa.Column(sa.Float, nullable=True)
    