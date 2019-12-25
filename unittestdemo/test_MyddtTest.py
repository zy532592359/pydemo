from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import ddt
testdatas=[
    {'user':'zhangyang','pass':'111','expect':'True'},
    {'user':'zhangyang','pass':'123456','expect':'False'}
]
@ddt.ddt
class myddttest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(*testdatas)
    def test_01(self,data):
        self.driver.get("http://192.168.27.204:8001/")
        self.driver.find_element_by_name("uname").send_keys(data['user'])
        self.driver.find_element_by_name("pass").send_keys(data['pass'])
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        try:
            aa = expected_conditions.presence_of_element_located(locator=(By.XPATH,"//a[@href='/list']"))(self.driver)
        except Exception as e:
            aa=False
        finally:
            if(aa != False):
                aa=True
            self.assertTrue(str(aa)==data['expect'])



if __name__ == '__main__':
    unittest.main()
