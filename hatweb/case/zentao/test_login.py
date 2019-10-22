import allure
import pytest

from base import read_csv, read_yaml
from case import BaseTest
from page.zentao import biz_set_language, biz_get_real_name_after_login


class TestLogin(BaseTest):
    """
    author: ArtLinty
    email: hello@linty.art
    desc: 测试测试禅道登录业务
    """
    __test = dict(
        collection=read_csv(current=__file__, file_path="test_login.csv"),
        url=read_yaml(current=__file__, file_path="../../config/env_active.yml", key="zentao.url"),
        title="在登录页面，使用合法数据登录，操作成功",
        case="https://dwz.cn/GUIf2ZeN",
        feature="登录",
        story="系统登录操作",
        tag=("web", "zentao", "login", "valid"),
        severity=allure.severity_level.CRITICAL
    )

    @pytest.fixture(autouse=True)
    def prepare(self):
        """
        测试固件
        :return:
        """

        self.init_logger(__name__)
        self.init_driver(url=self.__test.get("url"))

        yield
        self.close_driver()

    @allure.feature(__test.get("feature"))
    @allure.story(__test.get("story"))
    @allure.tag(*__test.get("tag"))
    @allure.severity(__test.get("severity"))
    @allure.testcase(url=__test.get("case"))
    @allure.title(__test.get("title"))
    @pytest.mark.parametrize("data", __test.get("collection"))
    def test_login(self, data):
        """
        测试登录，合法数据正常登录
        :param data:
        :return:
        """

        account = data.get("account")
        password = data.get("password")
        language = data.get("language")

        actual_lang_button_text = biz_set_language(
            driver=self.driver,
            language=language,
            logger=self.logger
        )
        self.snapshot("在登录页面设置语言后截图=%r" % data)
        self.info("[%s] - 在登录页面设置语言，使用数据： %r" % (__name__, dict(language=language)))
        assert self.assert_equal(expected=data.get("exp_button_lang"), actual=actual_lang_button_text)

        current_url, actual_real_name = biz_get_real_name_after_login(
            driver=self.driver,
            account=account,
            password=password,
            logger=self.logger
        )

        self.info(
            "[%r]-登录禅道, 使用数据 account=%r, password=%r"
            % (__file__, account, password)
        )
        self.snapshot("登录后截图数据=%r" % data)
        expected = data.get("expected_url")
        assert self.assert_in(
            expected=expected,
            actual=current_url
        ), "登录后URL地址不对, expected=%r, actual=%r, 当前数据=%r" % (expected, current_url, data)

        expected = data.get("expected_real_name")
        assert self.assert_in(
            expected=expected,
            actual=actual_real_name
        ), "登录后 realname 地址不对, expected=%r, actual=%r, 当前数据=%r" % (expected, actual_real_name, data)
