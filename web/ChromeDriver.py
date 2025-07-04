from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 

class ChromeDriver:
  def __init__(self):
      self.chrome_options = Options()
      # self.chrome_options.add_argument(r"--user-data-dir=C:\Users\felip\AppData\Local\Google\Chrome\User Data")
      # self.chrome_options.add_argument(r"--profile-directory=Default")
      
      prefs = {
          "download.default_directory": os.path.join(os.getcwd(), 'downloads/xlsx/'),
          "download.prompt_for_download": False,
          "directory_upgrade": True,
          "safebrowsing.enabled": True
      }

      self.chrome_options.add_experimental_option("prefs", prefs)


      self.driver = webdriver.Chrome(options=self.chrome_options)

    
  def acessUrl(self, url):
    sleep(2)
    print('acessando')
    self.driver.get(str(url))
  
  def quit(self):
    return self.driver.close()