from models.user import User
from seed_project import db_session


def create_new_user(first_name, last_name):
    user = User(first_name=first_name, last_name=last_name)
    db_session.add(user)
    db_session.commit()