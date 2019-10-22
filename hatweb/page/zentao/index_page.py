from base import read_yaml
from page.zentao.login_page import LoginPage


class IndexPage(LoginPage):
    """
    author: ArtLinty
    email: hello@linty.art
    desc: 禅道企业版 主页 业务
    """
    __config = read_yaml(current=__file__, file_path="web.yml", key="IndexPage")

    def get_real_name(self):
        """
        获取右上角真实姓名
        :return:
        """
        self.info("[%s] - 获取真实姓名！ " % __name__)
        return self.driver.get_text(self._get_config(data_dict=self.__config, data_key="LOCATOR.REAL_NAME_SPAN"))

    def is_menu_active(self, menu: str):
        """
        判断菜单是否处于激活状态
        :param menu:
            my,
            product,
            project,
            qa,
            ops,
            oa,
            feedback,
            doc,
            report,
            company,
            admin
        :return:
        """
        if menu.strip() != "":
            menu = menu.lower().strip()
        if menu in ["my", "product", "project", "qa", "ops", "oa", "feedback", "doc", "report", "company", "admin"]:
            selector = self._get_config(data_dict=self.__config, data_key="LOCATOR.%s_LI" % menu.upper())

        else:
            selector = None

        if selector is not None:
            self.info("[%s] - 获取菜单的选中状态，数据是 %r！ " % (__name__, dict(menu=menu)))
            return "active" in self.driver.get_attribute(
                selector,
                "class"
            )

        return None
