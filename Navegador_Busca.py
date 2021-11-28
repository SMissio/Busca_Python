#!/usr/bin/env python
# coding: utf-8

# In[33]:


from selenium import webdriver as opsele
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyautogui as escolher_opcao
import pyautogui as tempopc
import pyautogui as escrever

escrever.alert("Por Gentileza Aguarde o Rpa vai iniciar.")

tempopc.sleep(2)
opcao = pyautogui.confirm('Escolha a opção desejada',buttons = ['Caneca', 'Copo','Garrafa'])

if opcao == "Copo":
    meuNavegador = opsele.Chrome()
    meuNavegador.get("https://www.google.com/")
    tempopc.sleep(6)
    meuNavegador.find_element_by_name("q").send_keys("Copo valor")
    escolher_opcao.press('Enter')
    tempopc.sleep(3)
    meuNavegador.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    
    tempopc.sleep(8)
    meuNavegador.find_element_by_xpath('//*[@id="rcnt"]/div[2]/div/div/div[3]/div[2]/div/div/span[1]/div/a').click()
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")
elif opcao == "Caneca":
    meuNavegador = opsele.Chrome()
    meuNavegador.get("https://www.google.com/")
    tempopc.sleep(6)
    meuNavegador.find_element_by_name("q").send_keys("Caneca valor")
    escolher_opcao.press('Enter')
    tempopc.sleep(3)
    meuNavegador.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    tempopc.sleep(8)
    meuNavegador.find_element_by_name("lower").send_keys("85")
    tempopc.sleep(6)
    meuNavegador.find_element_by_name("upper").send_keys("100")
    tempopc.sleep(6)
    tempopc.press('enter')
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")
elif opcao == "Garrafa":
    meuNavegador = opsele.Chrome()
    meuNavegador.get("https://www.google.com/")
    tempopc.sleep(6)
    meuNavegador.find_element_by_name("q").send_keys("Garrafa valor")
    escolher_opcao.press('Enter')
    tempopc.sleep(3)
    meuNavegador.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    tempopc.sleep(8)
    meuNavegador.find_element_by_xpath('//*[@id="ow26"]/div[1]/div').click()
    tempopc.sleep(8)
    meuNavegador.find_element_by_xpath('//*[@id="lb"]/div/g-menu/g-menu-item[3]/div').click()
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")
    


# In[ ]:





# In[ ]:




