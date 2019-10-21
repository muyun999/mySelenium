from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://www.optima-trans.net/#/"
driver.get(url)
time.sleep(2)
# js1 = """document.querySelector('.k-datepicker-input').removeAttribute("readonly")"""
js1="""document.querySelector(".k-datepicker-input").removeAttribute("readonly")"""
driver.execute_script(js1)
time.sleep(2)
js2 = """document.querySelector(".k-datepicker-input").value='2018-11-11'"""
driver.execute_script(js2)
# elm.clear()
# elm.send_keys("2017-10-10")
# js3 = """document.querySelectorAll(".k-option")[1]"""
# driver.execute_script(js3)
# js4 = """var elm = document.querySelectorAll(".k-option")[1];
#         elm.style.border="2px solid red";
#         elm.value='浙江省杭州市';
# """
# driver.execute_script(js4)



if __name__ == "__main__":
    pass


