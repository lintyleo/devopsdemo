__version__ = "2.0.2"
__author__ = "ArtLinty"

from base import BoxDriver, Logger, parse_dict


class BasePage(object):
    __logger = None
    __driver = None

    def __init__(self, driver: BoxDriver, logger=None):
        """
        ApiPage 类的构造方法
        :param driver: 传递 用例中的 BoxRequest 实例化对象，默认是 self.request
        :param logger: 传递 用例中的 Logger 实例化对象，默认是 self.logger
        """

        self.__driver = driver
        self.__logger = logger
        self.info("[%s] - 使用构造方法完成实例化!" % __name__)

    def info(self, msg):
        """
        记录日志
        :param msg:
        :return:
        """
        if self.logger is not None and isinstance(self.logger, Logger):
            self.logger.info(msg)

    def _open(self, url):
        """
        打开页面
        :param url:
        :return:
        """
        self.driver.navigate(url)
        self.driver.maximize_window()
        self.info("[%s] page navigate: %s! " % (__name__, url))

    def _get_config(self, data_dict: dict, data_key: str):
        """
        获取配置文件的值
        :param data_dict:  配置文件字典
        :param data_key:  配置文件路径
        :return:
        """
        self.info("[%s] - 获取配置文件的值：data_key=%s, data_dict=%r!" % (__name__, data_key, data_dict))
        return parse_dict(dict_data=data_dict, data_key=data_key)

    @property
    def current_url(self):
        """
        current url
        :return:
        """
        return self.driver.current_url

    @property
    def title(self):
        """
        title
        :return:
        """
        return self.driver.current_title

    @property
    def driver(self):
        """
        get current request
        :return:
        """
        return self.__driver

    @property
    def logger(self):
        """
        日志对象，给业务使用，让他使用这个对象写日志，把他做的事情记录在里面
        :return:
        """
        return self.__logger
