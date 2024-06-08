import logging

class ErrorHandlingAgent:
    def __init__(self):
        # Initialize logging
        logging.basicConfig(level=logging.ERROR)
        self.logger = logging.getLogger(__name__)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def handle_exception(self, exception):
        self.logger.exception(exception)
        return {"status": "error", "message": str(exception)}
