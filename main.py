from scrapper import Scrapper
from threading import Thread


def extract_it_results():
    s = Scrapper("https://www.osmania.ac.in/res07/20210211.jsp")
    s.get_results(245319737001, branch=1)
    s.convert_to_csv(branch=1)


def extract_cse_results():
    s = Scrapper("https://www.osmania.ac.in/res07/20210211.jsp")
    s.get_results(245319733001, branch=0)
    s.convert_to_csv(branch=0)


it = Thread(target=extract_it_results, name="IT_thread")
cse = Thread(target=extract_cse_results, name="CSE_thread")
it.start()
cse.start()
