from contextlib import contextmanager
from time import sleep
from typing import Generator
import pyautogui

class Gui:
  def click(self, image_path):
    local = self.localeByPrint(image_path)
    if local:
        
        pyautogui.click(local)
        return True
    else:
        print(f"Imagem '{image_path}' não encontrada na tela.")
        return False
  
  def write(self, message:str):
    return pyautogui.write(message)
  
  def pressKey(self, key: str, times:int = 1):
    
    for _ in range(times):
     pyautogui.press(key)
      
  
  @contextmanager
  def keydownAction(self, key:str) -> Generator:
    pyautogui.keyDown(key)
    try:
      yield
    finally:
      pyautogui.keyUp(key)
  
  def localeByPrint(self,imagePath:str):
    return pyautogui.locateCenterOnScreen(image=imagePath, confidence=0.7)