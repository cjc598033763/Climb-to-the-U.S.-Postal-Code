# -*-coding:utf-8-*-
from selenium.webdriver.chrome.options import Options
from lianxi2 import BaseOperator
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class lianxi:
    def __init__(self):
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.driver=webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://arcb.com/tools/rate-quote.html#/new")
        self.zentao=BaseOperator(self.driver)
        self.loc1=("xpath", "//div[4]/div/div[1]/abt-party/div/div[2]/div[1]/abt-city-coding-input//input")
        self.loc3=("xpath", "//ul[@role='listbox']/li")
        self.loc=""

    def open_file(self):
        f=open("Untitled-1.txt", "r")
        list_f=eval(str((f.readlines())).replace("\\n", ""))
        return list_f

    #
    # def for_list_f(self):
    #     for n in self.open_file():
    #         self.zentao.sendKeys(self.loc1, str(n))
    #         return len(self.zentao.findElements(self.loc3))

    def len_list_f(self):
        return self.zentao.get_att(self.loc1, "value")

    def test01(self):
        time.sleep(20)
        for n in self.open_file():
            print(n)
            self.zentao.sendKeys(self.loc1, str(n))
            time.sleep(2)
            if str.isdigit(self.zentao.get_att(self.loc1, "value")):
                for i in range(1, len(self.zentao.findElements(self.loc3)) + 1):
                    loc2=("xpath", '//ul[@role="listbox"]/li[{num}]'.format(num=i))
                    self.zentao.ActionChains_move(loc2)
                    with open("a.txt", "a") as f:
                        f.write(self.zentao.get_ele_text(loc2) + "\n")
                        f.close()
                    print(str(self.open_file().index(n) + 1))
                    print(str(self.open_file().index(n) + 1) + "---------" + self.zentao.get_ele_text(loc2))
                self.zentao.clear(self.loc1)
            else:
                with open("a.txt", "a") as f:
                    f.write(self.zentao.get_att(self.loc1, "value") + "\n")
                    f.close()
                    print(str(self.open_file().index(n) + 1))
                    print(str(self.open_file().index(n) + 1) + "---------" + self.zentao.get_att(self.loc1, "value"))
                    self.zentao.clear(self.loc1)
                    pass


if __name__ == '__main__':
    print(lianxi().test01())
