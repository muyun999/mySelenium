from selenium.common.exceptions import NoSuchElementException
LOCATOR_DICT = {
    'id': 'By.ID',
    'css': 'By.CSS_SELECTOR',
    'name': 'By.NAME',
    'xpath': 'By.XPATH',
    'link_text': 'By.LINK_TEXT',
    'tag': 'By.TAG_NAME',
    'class_name': 'By.CLASS_NAME'
}


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def run_script(self, js=None):
        if js is None:
            print("请传入js参数")
        else:
            self.driver.execute_script(js)


class PageElement:
    def __init__(self, timeout=2, desc=None, **kwargs):
        self.timeout = timeout
        self.desc = desc
        if not kwargs:
            print("请输入一个定位元素")
        if len(kwargs) > 1:
            print("只能输入一个定位元素")
        self.k, self.v = next(iter(dict(kwargs).items()))
        if self.k not in LOCATOR_DICT.keys():
            print("输入的元素定位有误,请使用'id','css','name','xpath','link_text','tag','class_name'")
        else:
            self.element_locator = LOCATOR_DICT.get(self.k), self.v

    def get_element(self):
        try:
            elem = self.driver.find_element(*self.element_locator)
        except NoSuchElementException:
            print("找不到元素")
            return None
        else:
            style_red = 'arguments[0].style.border="2px solid red"'
            self.driver.execute_script(style_red, elem)
            return elem

    def find(self):
        for i in range(1,self.timeout):
            print(f"第{i}次查找元素:{self.element_locator}")
            if self.get_element() is not None:
                return self.get_element()

    def __get__(self, instance, owner):
        return self.find()



