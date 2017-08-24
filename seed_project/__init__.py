
import logging
import wtforms_json
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import TestingConfiguration

app = Flask(__name__)
app.config.from_object('seed_project.TestingConfiguration')

#initialize logging
app.logger.setLevel(app.config['LOGGING_LEVEL'])
logging_handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
logging_formatter = logging.Formatter(app.config['LOGGING_MESSAGE_FORMAT'], app.config['LOGGING_TIME_FORMAT'])
logging_handler.setFormatter(logging_formatter)
app.logger.addHandler(logging_handler)

# initialize wtforms json extension - enables initialization of WTForms from JSON data
wtforms_json.init()

engine = create_engine(app.config['DATABASE_URI'], convert_unicode=True)

# Factory method that returns a Session object with same properties when called.
# For sqlite, a NullPool is used by default
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session_factory)

import routes, error_handlers



