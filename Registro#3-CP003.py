# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSecambiaelnombrequeseregistroalmomentodecrearlacuenta():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_secambiaelnombrequeseregistroalmomentodecrearlacuenta(self):
    self.driver.get("https://tucan.toolsincloud.net/home.php")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("UsuarioTuCan3")
    self.driver.find_element(By.NAME, "submit").click()
  
