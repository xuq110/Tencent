# -*- coding:utf-8 -*-

import os
import sys
sys.path.append("D:\Python36_install\Lib\site-packages")
import allure
import pytest
from selenium import webdriver
import time


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
#@pytest.mark.parametrize('test_data1',['allure','hello','unittest'])
@pytest.mark.parametrize('test_data1',['your','god','success'])
def test_steps_demo(test_data1):

    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step( 'f' "输入搜索词:{ test_data1 }" ):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()

'''if __name__ == '__main__':
    pytest.main["-v test_baidu.py --alluredir=./result/"]

'''