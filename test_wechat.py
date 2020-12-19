import time

from selenium import webdriver
import pytest
import yaml
class TestDemo():


    def get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address= '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        cookies = self.driver.get_cookies()
        with open('./data.yml','w',encoding='UTF-8') as f:
            yaml.dump(cookies,f)


    def test_addpeople(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com')
        with open('./data.yml', 'r', encoding='UTF-8') as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_css_selector("a.qui_btn.ww_btn.js_add_member")[2].click()
        self.driver.find_element_by_id('username').send_keys("ceshi12")
        self.driver.find_element_by_id('memberAdd_english_name').send_keys("test")
        self.driver.find_element_by_id('memberAdd_acctid').send_keys("1234567181")
        self.driver.find_element_by_id('memberAdd_phone').send_keys("17332831283")
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_css_selector('.member_edit>form>div:nth-child(1)>a:nth-child(2)').click()
        self.driver.implicitly_wait(5)
        res = self.driver.find_element_by_css_selector("//*[@title='member_list']")
        print(res)
        assert res ==  "ceshi12"
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    TestDemo().get_cookie()
    TestDemo().test_addpeople()
