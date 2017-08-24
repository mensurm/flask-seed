""" Utility module that creates necessary database objects """

from seed_project import engine
from seed_project.models import Base


if __name__ == '__main__':
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
