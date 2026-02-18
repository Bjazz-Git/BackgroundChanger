import backgroundchanger

class AppException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


class MissingImage(AppException):
    def __init__(self, directory):
        message = "Missing Image"
        error = f"Image could not be located in directory {directory}"
        super().__init__(message, error)


class InvalidImage(AppException):
    def __init__(self):
        message = "Invalid Image"
        error = "Image could not be set as a background"
        super().__init__(message, error)