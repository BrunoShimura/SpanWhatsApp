from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unicodedata import normalize
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import selenium
import random
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("user-data-dir=selenium") 
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://web.whatsapp.com/")
time.sleep(30)
while True:
    try:
        verificacao = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div').text
    except:
        verificacao = ''

    if str(verificacao) == 'Para usar o WhatsApp no seu computador:':
        time.sleep(5)
    else:
        break

soup = BeautifulSoup(driver.page_source,'html.parser')

contatos = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
time.sleep(0.5)
contatos.click()
time.sleep(random.randint(2, 6))

nomeDoContato = ('Guizardi') #Digite o nome do contato

novaConversa = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input')
novaConversa.send_keys(nomeDoContato)   
time.sleep(random.randint(2, 6))
novaConversa.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 6))

while True:#Spam de mensagens

    spam = ('Eae blz') #Mensagem a ser enviada
    campoTexto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    campoTexto.send_keys(spam)
    campoTexto.send_keys(Keys.ENTER)
    time.sleep(0.5)

# while True:#Spam de emojis

#     abrirEmojis = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div/div[2]/button/span')
#     abrirEmojis.click()
#     time.sleep(1)
#     emojiDedo = driver.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/span[1]')
#     emojiDedo.click()
#     time.sleep(1)
#     campoTexto = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#     campoTexto.send_keys(Keys.ENTER)
#     time.sleep(2)
