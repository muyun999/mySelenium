from common.page_object import PageElement, BasePage
from selenium import webdriver


class BaiduPage(BasePage):
    search_bar = PageElement(name="wd")
    click_bar = PageElement(id="su")


driver = webdriver.Firefox()
page = BaiduPage(driver)
page.get("https://www.baidu.com")
page.search_bar.send_keys("圣墟")
page.click_bar.click()


if __name__ == '__main__':
    pass

