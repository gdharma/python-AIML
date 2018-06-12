from selenium import webdriver



# EMPI Login page
chromedriver = "C:\drivers\chromedriver"
driver=webdriver.Chrome(chromedriver)
driver.get("https://empi.sit.mo.wellpoint.com/EmpiPortal/login.jsp")
print(driver.current_url)