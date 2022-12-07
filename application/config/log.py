from datetime import datetime
import logging

FORMAT = '%(asctime)s -- %(levelname)s --> %(message)s '
FILENAME = f"logs/LogFile-{datetime.today().date()}.txt"
logging.basicConfig(format=FORMAT,filename=FILENAME,level=logging.INFO)

def info(log):
    logging.info(log)

def error(log):
    logging.error(log)

def debug(log):
    logging.debug(log)

def warning(log):
    logging.warning(log)

