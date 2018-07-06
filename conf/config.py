__author__ = 'jasonyang'


class DebugConfig:
    def __init__(self):
        self.CREDIT_DATABASE = 'mysql'
        self.CREDIT_MYSQL_HOST = '10.7.16.11'
        self.CREDIT_MYSQL_DBNAME = 'credit_test'
        self.CREDIT_MYSQL_USER = 'root'
        self.CREDIT_MYSQL_PASSWORD = 'nsfocus'  # 'qESwYIBL5I'
        self.CREDIT_MYSQL_PORT = 3306
        self.CREDIT_MYSQL_TIMEOUT = 3600


class OnlineConfig:
    def __init__(self):
        self.CREDIT_DATABASE = 'mysql'
        self.CREDIT_MYSQL_HOST = '10.6.109.1'
        self.CREDIT_MYSQL_DBNAME = 'credit'
        self.CREDIT_MYSQL_USER = 'credit'
        self.CREDIT_MYSQL_PASSWORD = 'qweO1!k2ndP'  # 'qESwYIBL5I'
        self.CREDIT_MYSQL_PORT = 3306
        self.CREDIT_MYSQL_TIMEOUT = 3600


class NoConfigType(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def get_config(config_name):
    if config_name == 'debug':
        return DebugConfig()
    elif config_name == 'online':
        return OnlineConfig()
    else:
        raise NoConfigType('no config type exist!')
