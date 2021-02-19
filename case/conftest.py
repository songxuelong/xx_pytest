from pages.login_page import LoginPage
from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    #_driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无界面
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
    chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    _driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)


    # 窗口最大化
    _driver.maximize_window()


    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver


@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver

