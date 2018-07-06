# -*-encoding:utf-8-*-
__author__ = 'jasonyang'


class Config(object):
    '''项目配置文件'''

    def __init__(self, pattern):
        print("getting " + pattern + " config....")
        self.pattern = pattern
        self.debug = {
            'CREDIT_DATABASE': 'mysql',
            'CREDIT_MYSQL_HOST': '10.7.16.11',
            'CREDIT_MYSQL_DBNAME': 'dashboard',
            'CREDIT_MYSQL_USER': 'root',
            'CREDIT_MYSQL_PASSWORD': 'nsfocus',
            'CREDIT_MYSQL_PORT': 3306,
            'CREDIT_MYSQL_TIMEOUT': 3600,
            'CREDIT_MEMCACHE_LIST': ['127.0.0.1:11211'],
            'CREDIT_POAC_API': 'http://10.6.109.6/reputation/hashmd5verify/'}
        self.online = {
            'CREDIT_DATABASE': 'mysql',
            'CREDIT_MYSQL_HOST': '10.6.109.1',
            'CREDIT_MYSQL_DBNAME': 'dashboard',
            'CREDIT_MYSQL_USER': 'root',
            'CREDIT_MYSQL_PASSWORD': 'nsfocus',
            'CREDIT_MYSQL_PORT': 3306,
            'CREDIT_MYSQL_TIMEOUT': 3600,
            'CREDIT_MEMCACHE_LIST': ['127.0.0.1:11211'],
            'CREDIT_POAC_API': 'http://10.6.109.6/reputation/hashmd5verify/'}

    @property
    def config(self):
        try:
            return self.__getattribute__(self.pattern)
        except Exception, e:
            print("error info:no " + self.pattern + ' config pattern exist! please check your config')
            # print(e)
            return {}


if __name__ == '__main__':
    config = Config('debug')
    print config.debug.get('CREDIT_DATABASE', None)
