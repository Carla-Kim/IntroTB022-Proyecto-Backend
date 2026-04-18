from flask import jsonify

def ReturnErrors(*errors):
    return {
        "errors": list(errors)
    }

class APIError(Exception):
    code = "INTERNAL_ERROR"
    status = 500
    level = "error"

    def __init__(self, message="Unexpected error", description=None):
        super().__init__(message)
        self.message = message
        self.description = description

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "level": self.level,
            "description": self.description
        }

class BadRequestError(APIError):
    code = "BAD_REQUEST"
    status = 400

    def __init__(self, errors=None, message="Bad Request"):
        super().__init__(message)
        self.errors = errors or [self.to_dict()]
    
    def to_dict(self):
        return self.errors

class NotFoundError(APIError):
    code = "NOT_FOUND"
    status = 404

class ConflictError(APIError):
    code = "CONFLICT"
    status = 409

def build_error(error: APIError):
  return jsonify({
      "errors": [error.to_dict()]
  }), error.status

def register_error_handlers(app):

    @app.errorhandler(APIError)
    def handle_api_error(error):
        return build_error(error)
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        api_error = APIError(
            message="Internal server error",
        )
        return build_error(api_error)
