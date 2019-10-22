from base import read_yaml
from page.zentao.web import ZentaoPage


class LoginPage(ZentaoPage):
    """
    author: ArtLinty
    email: hello@linty.art
    desc: 禅道企业版 登录页面业务
    """

    __config = read_yaml(current=__file__, file_path="web.yml", key="LoginPage")

    def login(self, account, password):
        """
        登录
        :param account:
        :param password:
        :return: 当前 URL
        """

        driver = self.driver

        driver.type(self._get_config(data_dict=self.__config, data_key="LOCATOR.ACCOUNT_INPUT"), account)
        driver.type(self._get_config(data_dict=self.__config, data_key="LOCATOR.PASSWORD_INPUT"), password)
        driver.click(self._get_config(data_dict=self.__config, data_key="LOCATOR.SUBMIT_BUTTON"))
        self.info("[%s] - 使用数据登录: %r" % (__name__, dict(account=account, password=password)))

        return self.current_url

    def set_language(self, language):
        """
        设定语言
        :param language:
            zh_hans: 中文简体
            zh_hant: 中文繁体
            en: 英文
            de: 德语
        :return:
        """
        if language is not None and isinstance(language, str):
            language = language.lower().strip()
        else:
            language = ""
        if language in ["zh_hans", "zh_hant", "en", "de"]:
            language_selector = "LOCATOR.%s_MENU" % language.upper()
            self.driver.click(self._get_config(data_dict=self.__config, data_key="LOCATOR.LANGUAGE_BUTTON"))
            self.driver.click(self._get_config(data_dict=self.__config, data_key=language_selector))
            self.info("[%s] - 设定语言为 %s" % (__name__, language_selector))

        return self.driver.get_text(self._get_config(
            data_dict=self.__config,
            data_key="LOCATOR.LANGUAGE_BUTTON"
        ))
