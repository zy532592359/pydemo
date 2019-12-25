from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import *
import requests
from urllib.request import build_opener,HTTPCookieProcessor,Request
import http.cookiejar
import time
import unittest
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_t1(self):
        #self.openfirfox()
        self.driver.get("http://192.168.27.204:8001")
        self.driver.find_element_by_name("uname").send_keys("zhangyang")
        self.driver.find_element_by_name("pass").send_keys("111")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        sel = self.driver.find_element_by_tag_name("select")
        ss = Select(sel)
        time.sleep(3)
        ss.select_by_index(3)
        time.sleep(3)
        self.assertEqual(1,1)
        #self.closefirefox()

    def test_t2(self):
        #self.openfirfox()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.baidu.com")
        shezhi=self.driver.find_element_by_link_text("设置")
        ActionChains(self.driver).move_to_element(shezhi).perform()
        time.sleep(3)
        self.driver.find_element_by_link_text("搜索设置").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[6]/td[2]/div[1]/a[@class='prefpanelgo']").click()
        time.sleep(3)
        #alert=self.driver.switch_to_alert()
        alert = self.driver.switch_to.alert
        time.sleep(3)
        #png = self.driver.get_screenshot_as_file("a.png")
        #self.driver.save_screenshot("abc.png")
        alert.accept()
        time.sleep(3)
        self.assertEqual(1,2)
        #self.closefirefox()

    def test_t3(self):
        url = "http://192.168.27.204:8001/list"
        #data={'uname':'zhangyang','pass':'111'}
        data = {'uname': 'zhangyang', 'pass': '111'}
        response = requests.post(url="http://127.0.0.1:8001/login", data=data, timeout=5)
        cookie=response.cookies
        #print(dir(cookie))
        s = requests.session()
        s.keep_alive = False
        response=requests.get(url,cookies=cookie, timeout=5)
        print(response.text)
        self.assertEqual(1,1)

    def test_t4(self):
        cookie_jar=http.cookiejar.MozillaCookieJar("a.txt")
        cookie_processor = HTTPCookieProcessor(cookie_jar)
        opener = build_opener(cookie_processor)
        url = "http://192.168.27.204:8001/login"
        data = {'uname': 'zhangyang', 'pass': '111'}
        from urllib.parse import urlencode
        data=urlencode(data).encode()
        #print(data)
        req = Request(url=url,data=data,method="POST")
        #response=urlopen(req)
        response=opener.open(req)
        print(response.headers)

        #return headers
        print(response.read().decode("utf-8"))
        #response.close()
        #第二次访问list
        req2 = Request(url="http://192.168.27.204:8001/list", method="GET")
        response2 = opener.open(req2)
        print(response2.headers)
        print(response2.read().decode("utf-8"))
        self.assertEqual(1,1)



    #tt.t5(cok)
#kw

