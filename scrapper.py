from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from pandas import DataFrame


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.osmania.ac.in/res07/20210211.jsp")
        self.results = {}
        self.roll_nos = []
        self.names = []
        self.sgpa = []
        self.threshold = [245319733180, 245319737120]

    def get_results(self, roll_no,
                    path="/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                         "1]/td/b/font/input[1]",
                    branch=1
                    ):

        if roll_no > self.threshold[branch]:
            return
        name_input = self.driver.find_element_by_xpath(path)
        name_input.send_keys(str(roll_no))
        self.driver.find_element_by_xpath(
            path[:-2] + "2]").click()
        while True:
            try:
                if self.driver.find_element_by_xpath(
                        "/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                        "3]/td/table/tbody/tr[1]/td/b/font "
                ).text == "Result":
                    self.roll_nos.append(str(roll_no))
                    self.names.append(
                        self.driver.find_element_by_xpath(
                            "/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                            "1]/td/table/tbody/tr[3]/td[2]/b/font "
                        ).text
                    )
                    store = []
                    try:
                        store.append(
                            [self.driver.find_element_by_xpath(
                                "/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                                "3]/td/table/tbody/tr[3]/td[2]/b/font "
                            ).text,
                             self.driver.find_element_by_xpath(
                                 "/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                                 "3]/td/table/tbody/tr[4]/td[2]/b/font "
                             ).text]
                        )
                        self.sgpa.append(" and ".join(*store))
                    except NoSuchElementException:
                        self.sgpa.append(
                            self.driver.find_element_by_xpath(
                                "/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr["
                                "3]/td/table/tbody/tr[3]/td[2]/b/font "
                            ).text
                        )

                self.get_results(roll_no + 1,
                                 path="/html/body/form/div/center/table/tbody/tr[4]/td/div/center/table/tbody/tr["
                                      "1]/td/b/font/input[1]",
                                 branch=branch)
                break

            except NoSuchElementException:
                sleep(0.65)

    def convert_to_csv(self, branch):
        names = ["CSE_results.csv", "IT_results.csv"]
        self.results = {"ROLL_NO": self.roll_nos, "Name": self.names, "SGPA": self.sgpa}
        print(self.results)
        df = DataFrame.from_dict(self.results)
        df.to_csv(names[branch], index=False)
