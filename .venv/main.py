import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"C:\Users\avesb\Documents\chromedriver-win64\chromedriver-win64")
driver = webdriver.Chrome()
