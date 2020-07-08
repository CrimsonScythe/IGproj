from selenium import webdriver

driver = webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe")

driver.get('https://www.instagram.com/explore/tags/food/')
# //*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span
elements = driver.find_element_by_xpath(xpath='//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')
# elements = driver.find_elements_by_xpath(xpath='//*[@id="main"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/a[2]/div/strong')

print(elements.text)

driver.close()
