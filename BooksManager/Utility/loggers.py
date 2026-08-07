# Utility/loggers.py
import logging

# Configure structured logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO, # Records INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_logger(name):
    return logging.getLogger(name)