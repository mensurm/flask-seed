
from httplib import INTERNAL_SERVER_ERROR
from seed_project.exceptions import ApiException
from flask import jsonify
from werkzeug.exceptions import HTTPException
from seed_project import app


@app.errorhandler(Exception)
def handle_error(e):
    """
    Application wide error handler function.
    :param e: Exception that was thrown
    :return: JSON representation of the error and the HTTP response code
    """
    app.logger.error(str(e))
    status_code = INTERNAL_SERVER_ERROR
    message = dict(message=str(e))

    if isinstance(e, HTTPException):
        status_code = e.code

    if isinstance(e, ApiException):
        status_code = e.code
        message = e.description_as_dict()

    return jsonify(message), status_code


app.register_error_handler(404, handle_error)
app.register_error_handler(500, handle_error)
