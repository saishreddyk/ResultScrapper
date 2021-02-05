from scrapper import Scrapper
s = Scrapper("https://www.osmania.ac.in/res07/20210211.jsp")
s.get_results(245319737001, branch=1)
s.convert_to_csv(branch=1)
s = Scrapper("https://www.osmania.ac.in/res07/20210211.jsp")
s.get_results(245319733001, branch=0)
s.convert_to_csv(branch=0)
