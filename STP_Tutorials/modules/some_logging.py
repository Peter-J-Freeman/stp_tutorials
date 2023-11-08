import logging

# Import the logger with the same name used in the settings.py
logger = logging.getLogger('MyAwesomeApp')


def some_function():
    # Use the logger to log messages at different log levels
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')
