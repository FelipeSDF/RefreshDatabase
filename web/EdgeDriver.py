from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options  # EdgeOptions
import os

class EdgeDriver:
    def __init__(self):
        self.edge_options = Options()

        # Configurações de download
        prefs = {
            "download.default_directory": os.path.join(os.getcwd(), 'downloads/xlsx/'),
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True
        }

        self.edge_options.add_experimental_option("prefs", prefs)

        # Criação do driver (certifique-se de ter o msedgedriver no PATH ou forneça o caminho diretamente)
        self.driver = webdriver.Edge(options=self.edge_options)

    def acessUrl(self, url):
        sleep(2)
        print('acessando')
        self.driver.get(str(url))

    def quit(self):
        return self.driver.close()
