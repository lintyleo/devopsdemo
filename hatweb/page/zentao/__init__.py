from page.zentao.index_page import IndexPage
from page.zentao.login_page import LoginPage


def biz_set_language(driver, language, logger=None):
    """
    设置登录页面的语言
    :param driver:
    :param language:
    :param logger:
    :return:
    """
    page = LoginPage(
        driver=driver,
        logger=logger
    )

    return page.set_language(
        language=language
    )


def biz_login(driver, account, password, logger=None):
    """
    登录场景
    :param driver:
    :param account:
    :param password:
    :param logger:
    :return:
    """
    page = LoginPage(
        driver=driver,
        logger=logger
    )

    return page.login(
        account=account,
        password=password
    )


def biz_get_real_name(driver, logger=None):
    """
    获取真实姓名
    :param driver:
    :param logger:
    :return:
    """

    page = IndexPage(
        driver=driver,
        logger=logger
    )

    return page.get_real_name()


def biz_is_menu_active(driver, menu, logger=None):
    """
    菜单是否激活场景
    :param driver:
    :param menu:
    :param logger:
    :return:
    """
    page = IndexPage(
        driver=driver,
        logger=logger
    )

    return page.is_menu_active(menu)


def biz_get_real_name_after_login(driver, account, password, logger=None):
    """
    获取真实姓名在登录后
    :param driver:
    :param account:
    :param password:
    :param logger:
    :return:
    """

    page = IndexPage(
        driver=driver,
        logger=logger
    )
    current_url = page.login(account, password)
    real_name = page.get_real_name()
    return current_url, real_name
