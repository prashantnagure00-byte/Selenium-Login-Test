from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
def test_login():
    driver.get("https://skillgun.com")
    time.sleep(5)
    mobile = driver.find_element(By.ID,"ContentPlaceHolder1_tbPhoneNumber" )
    mobile.send_keys("your mobile number")
    time.sleep(5)
    email = driver.find_element(By.ID,"ContentPlaceHolder1_tbEmail"  )
    email.send_keys("your email id")
    time.sleep(5)
    password = driver.find_element(By.ID,"ContentPlaceHolder1_tbPassword" )
    password.send_keys("password")
    time.sleep(5)
    cb = driver.find_element(By.ID,"ckbkPolicyAgreement")
    cb.click()
    time.sleep(5)
    log = driver.find_element(By.ID,"ContentPlaceHolder1_btnLogin" )
    log.click()
    time.sleep(5)
    assert "Home" in driver.current_url
