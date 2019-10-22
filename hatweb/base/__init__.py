__version__ = "2.0.2"
__author__ = "ArtLinty"
"""
# Usage：
# call build_driver() for web driver instance
"""
from urllib.parse import urlencode

from base.infrastructure import Logger
from base.box import BoxDriver
from base.helper import CsvHelper, PathHelper, DbHelper, YamlHelper, read_txt_format, DictHelper

"""
main portal, for web browser driver
"""

"""
main portal, for web api request
"""


def build_driver(url, driver_type: str, wait_seconds=None):
    """
    get driver for web browser testing
    :param wait_seconds:
    :param url: str，访问浏览器的 url
    :param driver_type: str，指定浏览器的类型，忽略大小写
        : c, chrome
        : i, ie
        : f, firefox
        : o, opera
        : s, safari
        : h, headless, headless_chrome, hc
    :return: BoxDriver
    """
    if not isinstance(driver_type, str):
        driver_type = 'c'

    driver_type = _parse_type(driver_type.lower())
    if wait_seconds:
        driver = BoxDriver(driver_type, wait_seconds=wait_seconds)
    else:
        driver = BoxDriver(driver_type)
    driver.navigate(url)
    driver.maximize_window()
    return driver


def build_logger(log_path):
    """
    build logger
    :param log_path:
    :return:
    """
    return Logger(
        log_path=log_path,
        call_path=__name__
    )


def encode_url(url: str, params: dict):
    """
    对 URL 进行编码
    :param url:
    :param params:
    :return:
    """
    return url, urlencode(params)


def read_txt(current, file_path):
    """
    读纯文本文件
    :param current:
    :param file_path:
    :return:
    """
    txt_file = PathHelper.get_actual_path_by_current_file(current, file_path)
    return read_txt_format(txt_file)


def read_csv(current, file_path):
    """
    读 CSV 文件，CSV 文件必须有标题
    :param current: 读 CSV 文件的绝对路径，直接填写 __file__ 就可以了
    :param file_path: CSV 文件相对当前的路径（是相对路径），当前文件通过相对路径访问 csv 所需要的路径字符串
    :return: list 列表，列表中的元素是 dict，dict 的 key 是 csv 的第一行的标题
    """
    csv_file = PathHelper.get_actual_path_by_current_file(current=current, file_path=file_path)
    return CsvHelper.read_for_parametrize(csv_file)


def read_yaml(current, file_path, key):
    """
    读 YAML 文件，YAML 文件必须有标题
    :param current: 读 YAML 文件的绝对路径，直接填写 __file__ 就可以了
    :param file_path: YAML 文件相对当前的路径（是相对路径）
    :param key: 读 YAML 文件中制定的 key
    :return: dict，dict 的内容是 YAML 对应的 key 的 value
    """
    yml_file = PathHelper.get_actual_path_by_current_file(current=current, file_path=file_path)
    return YamlHelper.get_config_as_dict(file=yml_file, key=key)


def read_json(current_file_path, json_to_current):
    """
    读 Json 文件，然后转化为 dict
    :param current_file_path:
    :param json_to_current:
    :return:
    """
    json_file = PathHelper.get_actual_path_by_current_file(current_file_path, json_to_current)
    return JsonHelper.read_json_file_as_dict(json_file)


def parse_dict(dict_data: dict, data_key, index=None, sub_key=None):
    """
    解析 JSON
    :param dict_data: 被解析的 JSON 的字典格式
    :param data_key: 请用 "." 隔开路径
    :param index:
    :param sub_key:
    :return:
    """

    return DictHelper.parse_dict_value(
        json_dict=dict_data,
        data_key=data_key,
        index=index,
        sub_key=sub_key
    )


"""
private method
"""


def _parse_type(driver_type):
    """
    parse driver type
    :param driver_type: str: driver type
        chrome: c or chrome
        firefox: f or firefox
        ie: i or ie
        safari: s or safari
        headless chrome: h or hc or headless, headless chrome
    :return: default value: BoxDriver.DriverType.CHROME
    """
    if driver_type == 'c' or driver_type == "chrome":
        return BoxDriver.DriverType.CHROME
    elif driver_type == 'f' or driver_type == "firefox":
        return BoxDriver.DriverType.FIREFOX
    elif driver_type == 'i' or driver_type == "ie":
        return BoxDriver.DriverType.IE
    elif driver_type == 's' or driver_type == "safari":
        return BoxDriver.DriverType.SAFARI
    elif driver_type == 'h' or driver_type == "headless" \
            or driver_type == "hc" or driver_type == "headless_chrome":
        return BoxDriver.DriverType.CHROME_HEADLESS

    return BoxDriver.DriverType.CHROME
