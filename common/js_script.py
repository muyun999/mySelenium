from selenium import webdriver

class js_script_css:
    def __init__(self, css, index=None, desc=None):
        self.css = css
        self.desc = desc
        if index is None:
            self.index = 0
        else:
            self.index = index

    def __get__(self, instance, owner):
        if not instance:
            return None
        else:
            global driver
            driver = instance.driver
            return self

    def remove_Attribute(self, attribute='readonly'):
        # 可用于时间日期控件等
        js = f"""document.querySelectorAll("{self.css}")[{self.index}].removeAttribute("{attribute}")"""
        driver.execute_script(js)

    def set_value(self, value):
        js = f"""var elm = document.querySelectorAll("{self.css}")[{self.index}];
                 elm.style.border="2px solid red";
                 elm.value = "{value}";
        """
        driver.execute_script(js)

    def click(self):
        js = f"""var elm = document.querySelectorAll("{self.css}")[{self.index}];
                elm.style.border ="2px solid red";
                elm.click();
        """
        driver.execute_script(js)
