

from flask import jsonify, request
from httplib import CREATED, OK
from seed_project import app
from seed_project import db_session
from validation.forms import UserForm
from seed_project.exceptions import InvalidInputException
from services import create_new_user


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Remove session at the end of the request or when the application shuts down
    :param exception:
    :return: None
    """
    app.logger.debug("Removing db session")
    db_session.remove()


@app.route('/api', methods=['GET'])
def status():
    """
    Route for testing the availability of the API
    """
    app.logger.debug('Return status')
    return jsonify(status='ONLINE'), OK


@app.route('/api/user', methods=['POST'])
def create_user():
    """
    Create a user in the database
    """
    app.logger.debug('Request to create user')

    user_form = UserForm.from_json(request.json)
    if user_form.validate() is False:
        raise InvalidInputException(errors=user_form.errors)

    create_new_user(user_form.first_name.data, user_form.last_name.data)

    response = jsonify(message='User created')
    return response, CREATED






