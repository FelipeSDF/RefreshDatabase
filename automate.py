import datetime
import os
from socket import TCP_NODELAY
from time import sleep
import time
import shutil
from dotenv import load_dotenv
from pathlib import Path

import pyautogui
from gui.gui import Gui
from web import ChromeDriver, EdgeDriver

env = load_dotenv()

class Control():
  def __init__(self, url:str=None):
    self.url = url
    self.gui = Gui()
    
    self.driver = EdgeDriver()
    
    self.driver.driver.maximize_window()
    
  def start(self):
    self.driver.acessUrl(self.url)
    return 'comecou'

  def stop(self):
    self.driver.quit() 
    return ('parou')

  def saveAllInDrive(self):
    return replacer.replace()

class MagniFinanceControl(Control):
  def __init__(self, url):
    super().__init__(url=url)

  def automateAll(self):
    self.start()
    
    sleep(5)
    
    self.automateLogin()
    
    sleep(100)
    
    self.automateExpanseAll()
    
    sleep(20)
    
    self.automateIncomes()
   
    sleep(20)
    
    self.gui.pressKey('pagedown')
    
    sleep(20)
    
    self.automateAccountings()
    
    sleep(5)
    
    # self.saveAllInDrive()
    
    self.stop()
  
  def automateLogin(self):
    sleep(5)
    self.gui.click(str( Path.cwd() /'images'/ 'loginemailfield.png'))
    self.gui.write(os.environ["MAGNIFINANCE_EMAIL"])
    sleep(5)
    self.gui.click(str( Path.cwd() /'images'/ 'MagniFinancePasswordField.png'))
    self.gui.write(os.environ["MAGNIFINANCE_PASSWORD"])

    self.gui.pressKey('enter')
  
  def automateExpanseAll(self):
    self.gui.click('./images/BI_Onlive_Expanse_all.png')
    
    sleep(65)

    self.gui.click('./images/export_to_excel.png')
    sleep(50)
    self.gui.write(str(Path.cwd() / 'downloads' / 'Magnifinance'))
    self.gui.pressKey('enter')
  
  def automateIncomes(self):
    self.gui.click('./images/Incomes.png')
    
    sleep(65)

    self.gui.click('./images/export_to_excel.png')
    sleep(50)
    self.gui.write(str(Path.cwd() / 'downloads' / 'Incomes'))
    self.gui.pressKey('enter')
  
  def automateAccountings(self):
    self.gui.click('./images/accountingMagnifinance.png')
    
    sleep(50)
    self.gui.pressKey('pageup')
    sleep(5)
    self.gui.click('./images/export_to_excel.png')
    sleep(25)
    self.gui.write(str(Path.cwd() / 'downloads' / 'Accounting - Magnifinance'))
    sleep(2)
    self.gui.pressKey('enter')

class QuickBooksControl(Control):
  def __init__(self, url = None):
    self.archiveNames = {'ACCOUNTING_-_QUICKBOOKS':20,'INVOICE_LIST_BY_DATE':50,'PROFIT_AND_LOSS_DETAIL':60,'UNPAID_BILLS':50}
    # self.archiveNames = {'ACCOUNTING_-_QUICKBOOKS':20,'PROFIT_AND_LOSS_DETAIL':60}

    super().__init__(url=url)
    
    
  def automateAll(self):
    self.start()
    
    time.sleep(10)

    
    self.automateLogin()

    for name in self.archiveNames:
      self.updatePreiod(str(name))
      self.automateDownloads(str(name), self.archiveNames[name])

    time.sleep(5)
    

    self.saveAllInDrive()
    
    self.stop()
    
    return True
    
  def automateLogin(self):
    try:
      email = os.environ['QUICKBOOKS_EMAIL']
      self.gui.write(email)
      self.gui.pressKey('enter')
      
      sleep(5)
      
      self.gui.write(os.environ['QUICKBOOKS_PASSWORD'])
      self.gui.pressKey('enter')
      
      sleep(10)
      
      image_path = Path.cwd() / 'images' / 'image093714.png'
      
      print(image_path)
      self.gui.click(str(image_path))
      
      
    except Exception as e:
      raise e

  def automateDownloads(self, archiveName :str, timeToWait : int):
    try:
      sleep(10)
        
      self.driver.driver.get(os.environ[archiveName])
      
      sleep(15)
      
      self.gui.pressKey('pageup', times = 3)
      
      with self.gui.keydownAction('shift'):
        pyautogui.scroll(-1000)
      
      sleep(2)
      self.gui.click(str(Path.cwd() / 'images' / '141107.png'))
      sleep(5)
      
      self.gui.click(str(Path.cwd() / 'images' / 'image.png'))
      
      time.sleep(timeToWait)
      
      self.gui.write(str(Path.cwd() / 'downloads' / archiveName.replace('_', ' ').title()))
      
      sleep(2)
      
      self.gui.pressKey('enter')
    
    except Exception as e:
      return e
  
  def updatePreiod(self, archivename:str):
    sleep(5)
    
    print(archivename)
    if archivename ==  'INVOICE_LIST_BY_DATE':
      
      self.driver.driver.get(os.environ[archivename])
      sleep(15)
      
      self.gui.pressKey('pageup', times = 3)
      
      sleep(2)
      
      self.gui.click(str(Path.cwd() / 'images' / '2021.png'))
      
      today = datetime.date.today()
      
      self.gui.write('01/01/2021')
      
      self.gui.pressKey('tab')

      self.gui.write(today.strftime('%m/%d/%Y'))
      
      self.gui.click(str(Path.cwd() / 'images' / 'runReport.png'))
      
      sleep(5)
      
      self.gui.pressKey('pageup', times = 3)
      
      sleep(2)
      
      self.gui.click(str(Path.cwd() / 'images' / 'saveCustomization.png'))
      
      sleep(2)
      
      self.gui.click(str(Path.cwd() / 'images' / 'save.png'))
      
      sleep(2)
      
    elif archivename == 'PROFIT_AND_LOSS_DETAIL':
      
      self.driver.driver.get(os.environ[archivename])
      sleep(15)
      
      self.gui.pressKey('pageup', times = 3)
      
      self.gui.click(str(Path.cwd() / 'images' / '2024.png'))
      
      today = datetime.date.today()
      
      self.gui.write(f'{today.month}/01/{int(today.year)-1}')
      
      self.gui.pressKey('tab')

      self.gui.write(today.strftime('%m/%d/%Y'))
      
      self.gui.click(str(Path.cwd() / 'images' / 'runReport.png'))
      
      sleep(5)
      
      self.gui.pressKey('pageup', times = 3)
      
      sleep(2)
      
      self.gui.click(str(Path.cwd() / 'images' / 'saveCustomization.png'))
      
      sleep(2)
      
      self.gui.click(str(Path.cwd() / 'images' / 'save.png'))
      
      sleep(2)
    
    return True

class ReplacerControl():
  def __init__(self, initialPath):
    self.path = initialPath
    
  def replace(self):
    downloadsUrl = str(Path.cwd() / 'downloads')
    
    for archive in os.listdir(downloadsUrl):
      
      if archive != 'Magnifinance.xlsx':
        src = str(Path.cwd() / 'downloads' / archive)
        dst = str(self.path + f'/{archive}')
        
        shutil.move(src, dst)
        
      else:
        srcV = str(self.path + f'/{archive}')
        dstV = str(self.path + f'/versionamento/{str(archive).replace('.xlsx','')} - 02-06-2025.xlsx')
        
        shutil.copy(srcV, dstV)
        
        src = str(Path.cwd() / 'downloads' / archive)
        dst = str(self.path + f'/{archive}')
        
        shutil.move(src, dst)

replacer = ReplacerControl('G:/Drives compartilhados/BI Management/New/BI/Relatórios/Base Compartilhadas/Financeiro/testing')
