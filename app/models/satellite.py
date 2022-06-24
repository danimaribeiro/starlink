import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext import declarative


def auto_str(cls):
    def __repr__(self):
        return '%s(\n%s\n)' % (
            type(self).__name__,
            '\n'.join('\t%s=%s' % item for item in vars(self).items() if item[0] != "_sa_instance_state")
        )
    cls.__repr__ = __repr__
    return cls

Base = declarative.declarative_base()

@auto_str
class SpaceTrack(Base):
    __tablename__ = "space_track"

    eid = sa.Column(sa.String(64), nullable=False, primary_key=True)
    satellite_id = sa.Column(sa.String(64), nullable=False)
    name = sa.Column(sa.String(64), nullable=False)
    created_date = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    epoch = sa.Column(sa.DateTime, nullable=False)
    longitude = sa.Column(sa.Float, nullable=True)
    latitude = sa.Column(sa.Float, nullable=True)
    velocity_kms = sa.Column(sa.Float, nullable=True)
