from selenium import webdriver
from selenium.common import exceptions

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
