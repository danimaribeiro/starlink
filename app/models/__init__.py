from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://blue_onion:onion_labs@db/interview')

Session = sessionmaker(engine)