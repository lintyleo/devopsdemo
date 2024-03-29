__version__ = "2.0.2"
__author__ = "ArtLinty"

from base import BoxRequest, Logger, parse_dict


class BaseApi(object):
    __logger = None
    __request = None

    def __init__(self, request: BoxRequest, logger=None):
        """
        ApiPage 类的构造方法
        :param request: 传递 用例中的 BoxRequest 实例化对象，默认是 self.request
        :param logger: 传递 用例中的 Logger 实例化对象，默认是 self.logger
        """

        self.__request = request
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

    def _send(self, uri: str,
              method: str,
              data_dict=None,
              auth=None,
              cookies=None,
              headers=None,
              files=None,
              is_json_content=True):
        """
        发送 HTTP/HTTPS 请求
        :param uri: 请求网址的路径部分（去掉协议，主机和端口）
        :param method:  请求方法
        :param data_dict:  请求需要传递的数据，与请求方法无关
        :param auth:  请求的授权认证
            支持 HTTP basic Auth， 传递 tuple，两个元素，分别是用户名和密码
            支持 Auth 2.0 认证，传递 str，字符串
            支持 自定义或者其他认证，传递 dict，两个key： key 和 value
        :param cookies:
        :param headers: 请求头
        :param files:  请求文件
        :param is_json_content: 是否是 JSON 格式的内容
        :return:
        """

        self.info("[%s] - 在 BaseApi 类中发送请求，使用的数据：uri=%s, method=%s, data_dict=%r, auth=%r"
                  % (__name__, uri, method, data_dict, auth))

        if self.request is not None and isinstance(self.request, BoxRequest):
            self.request.send(
                uri=uri,
                method=method,
                data_dict=data_dict,
                auth=auth,
                cookies=cookies,
                headers=headers,
                files=files,
                is_json_content=is_json_content
            )

    def _parse(self, body_key_list=None):
        """
        解析 send 的结果
        :param body_key_list: 需要解析的响应正文中的 key 的列表
        :return:
        """
        self.info("[%s] - 在 BaseApi 中解析响应结果，使用数据：body_key_list=%r, data_dict=%r"
                  % (__name__, body_key_list, self.json_dict))

        resp = self._parse_http_resp()
        for data_Key in body_key_list:
            value = parse_dict(dict_data=self.json_dict, data_key=data_Key)
            resp[data_Key] = value
            self.info("[%s] - 解析响应的 JSON 字典成功，data_key=%s, value=%r"
                      % (__name__, data_Key, value))

        return resp

    def _parse_list(self, list_data_key: str, index: int, sub_data_key_list: list):
        """
        解析 结果中的 list 数据
        :param list_data_key: list 所在的 key，例如 results[], 填写 results
        :param index:  索引下标
        :param sub_data_key_list:  列表中的每个元素的key
        :return:
        """
        self.info("[%s] - 在 BaseApi 中解析响应结果的 list，使用数据：list_data_key=%s, index=%d, sub_data_key_list=%r, data_dict=%r"
                  % (__name__, list_data_key, index, sub_data_key_list, self.json_dict))

        resp = self._parse_http_resp()
        for sub_data_key in sub_data_key_list:
            value = parse_dict(dict_data=self.json_dict, data_key=list_data_key, index=index, sub_key=sub_data_key)
            resp[sub_data_key] = value
            self.info("[%s] - 在 BaseApi 中解析响应的 JSON 字典成功，data_key=%s, value=%r"
                      % (__name__, sub_data_key, value))

        return resp

    def _get_config(self, data_dict: dict, data_key: str):
        """
        获取配置文件的值
        :param data_dict:  配置文件字典
        :param data_key:  配置文件路径
        :return:
        """
        self.info("[%s] - 获取配置文件的值：data_key=%s, data_dict=%r!" % (__name__, data_key, data_dict))
        return parse_dict(dict_data=data_dict, data_key=data_key)

    def _merge_dict(self, first_dict: dict, second_dict: dict):
        """
        合并两个字典，作为一个字典，使用 update()
        :param first_dict:
        :param second_dict:
        :return: 两个字典的并集
        """
        # update() 是直接更新了 first_resp 这个字典（合并了 second_resp)
        # 注意 update() 返回值是 None，直接使用 first_resp 就可以了
        first_dict.update(second_dict)
        self.info("[%s] - 合并了两个字典，first=%r, second=%r" % (__name__, first_dict, second_dict))
        return first_dict

    def _remove_none_param(self, params: dict):
        """
        移除掉参数字典中，值是 None 的元素，保证做到参数不传
        :param params:
        :return:
        """
        if params and isinstance(params, dict):
            keys = params.keys()

            keys_to_remove = []
            for k in keys:
                if params[k] is None:
                    keys_to_remove.append(k)

            for ktr in keys_to_remove:
                params.pop(ktr)
                self.info("[%s] - 在 params 移除了值为 None 的 key:%r! " % (__name__, ktr))

        return params

    def _parse_http_resp(self):
        """
        分析 http 的响应
        :return: 返回 dict
            status_code
            response_headers
            full_response
            json_dict
        """
        resp = {}
        if self.request and isinstance(self.request, BoxRequest):
            resp["status_code"] = self.request.status_code
            resp["cookies"] = self.request.cookies
            resp["response_dict"] = self.request.response_dict
            resp["json_dict"] = self.request.json_dict

        return resp

    @property
    def request(self):
        """
        get current request
        :return:
        """
        return self.__request

    @property
    def response(self):
        """
        get current response
        :return:
        """
        if self.request and isinstance(self.request, BoxRequest):
            return self.request.response_dict

        return None

    @property
    def logger(self):
        """
        日志对象，给业务使用，让他使用这个对象写日志，把他做的事情记录在里面
        :return:
        """
        return self.__logger

    @property
    def json_dict(self):
        """
        当前业务API 的json 字典
        :return:  dict
        """
        if self.request and isinstance(self.request, BoxRequest):
            return self.request.json_dict

        return None
