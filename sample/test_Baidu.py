from common.page_object import PageElement, BasePage
from selenium import webdriver
from common.js_script import js_script_css


class BaiduPage(BasePage):
    search_bar = PageElement(name="wd")
    click_bar = PageElement(id="su")
    dateclear = js_script_css('.k-datepicker-input')
    city = js_script_css(".k-option", 0)
    clickbar = js_script_css(".k-option", 0)


driver = webdriver.Firefox()
page = BaiduPage(driver)
page.get("http://www.optima-trans.net/#/")
# page.search_bar.send_keys("圣墟")
# page.city.remove_Attribute()
# page.city.set_value("浙江省温州市")
page.clickbar.click()


if __name__ == '__main__':
    pass

