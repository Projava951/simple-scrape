from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

ser = Service(r"C:/Users/Administrator/.cache/selenium/chromedriver/win32/113.0.5672.63")
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

driver = webdriver.Chrome(service=ser, desired_capabilities=desired_capabilities)

driver.get("https://app.webull.com")

get_url = driver.current_url

print("The current url is:" + str(get_url))

#Redirect
while True:
	val = input("Have you logged in? yes(y) or no(n) : ")

	if val == 'y' or val == 'yes':
		logs = driver.get_log("performance")
		# Iterates every logs and parses it using JSON
		for log in logs:
			network_log = json.loads(log["message"])["message"]

			if("Network.request" in network_log["method"]):

				# Writes the network log to a JSON file by
				# converting the dictionary to a JSON string
				# using json.dumps().
				if ("request" in network_log["params"] and network_log["params"]["request"]["url"] == "https://u1suser.webullfintech.com/api/user/v1/login/account/v2"):
					if ("postData" in network_log["params"]["request"]):
						postData = json.loads(network_log["params"]["request"]["postData"])
						print("DeviceId: " + postData["deviceId"])
						print("RegionId: " + str(postData["regionId"]))

