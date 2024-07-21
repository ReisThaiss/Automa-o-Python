from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Abre o navegador Chrome
navegador = webdriver.Chrome()

#Abre o site do magazine luiza
navegador.get("https://www.magazineluiza.com.br/")

#Encontra o elemento pelo XPath e clica nele
search_box = navegador.find_element(By.XPATH, '//*[@id="input-search"]')
search_box.click()
search_box.send_keys("notebooks")

time.sleep(2)  # Aguarda 2 segundos

#Envia a tecla "Enter" para o campo de busca
search_box.send_keys(Keys.RETURN)

import requests 
from bs4 import BeautifulSoup 

#Acessa o link de notebooks da magazine

link = "https://www.magazineluiza.com.br/busca/notebooks/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, "html.parser")

#Pega as informações do produto, avaliação e url do notebook
produto = site.find("h2", class_="sc-doohEh dHamKz")
print (produto.get_text())

avaliacao = site.find("span", class_ = "sc-epqpcT jdMYPv")
print (avaliacao.get_text())

url = site.find("a", class_ = "sc-eBMEME uPWog sc-dxUMQK jeUYOh sc-dxUMQK jeUYOh")
print (url.get_text())