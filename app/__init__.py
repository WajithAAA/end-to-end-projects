#import logging
import os
#from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from app.common import resp
from config import Config, config
from src.logger import logging


# logger = logging.getLogger("Project is running")
# formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#                               datefmt='%Y-%m-%d:%H:%M:%S')

def create_app(config_name):
    # info_log_path = os.path.join(Config.LOGS, "info.log")
    # error_log_path = os.path.join(Config.LOGS, "error.log")
    # os.makedirs(info_log_path, exist_ok=True)
    # os.makedirs(error_log_path, exist_ok=True)

    # info_log_handler = TimedRotatingFileHandler(info_log_path,
    #                                             when="d",
    #                                             interval=1,
    #                                             backupCount=730)
    # info_log_handler.setFormatter(formatter)
    # logger.setLevel(logging.INFO)
    # logger.addHandler(info_log_handler)

    # error_log_handler = TimedRotatingFileHandler(error_log_path,
    #                                              when="d",
    #                                              interval=1,
    #                                              backupCount=730)

    # error_log_handler.setFormatter(formatter)
    # error_log_handler.setLevel(logging.ERROR)
    # logger.addHandler(error_log_handler)

    logging.info(f"Project Started")

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])

    app.secret_key = b'YSHS_5#262L"F4USHSbs672^262'

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')

    return app