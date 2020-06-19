import scanner


target_url = "http://google.com/login/"
links_to_ignore = ["http://google.com/logout/"]

data_dict = {"username": "admin", "password": "password", "Login": "submit"}


vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://google.com/login/", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()
