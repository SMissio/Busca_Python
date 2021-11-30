from selenium import webdriver as opsele
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyautogui as escolher_opcao
import pyautogui as tempopc
import pyautogui as escrever

navegor = opsele.Chrome()
navegor.get("https://www.google.com/")
tempopc.sleep(2)
opcao = pyautogui.confirm('Escolha a opção desejada', buttons=['Caneca', 'Copo', 'Garrafa'])


def pesquisa_item(name):
    if name:
        tempopc.sleep(6)
        navegor.find_element_by_name("q").send_keys(f"{name} valor")
        escolher_opcao.press('Enter')
    else:
        raise ValueError("Opção não pode ser nula")


def acessa_shopping():
    tempopc.sleep(3)
    navegor.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    tempopc.sleep(8)


def filtra_por_valores_minimo_e_maximo(min=0, max=0):
    if max and min:
        navegor.find_element_by_name("lower").send_keys(f"{min}")
        tempopc.sleep(6)
        navegor.find_element_by_name("upper").send_keys(f"{max}")
        tempopc.sleep(6)
        tempopc.press('enter')
    else:
        raise ValueError("Valores maximo e minimo devem ser maiores do que zero")


def filtra_menores_valores():
    navegor.find_element_by_xpath('//*[@id="rcnt"]/div[2]/div/div/div[3]/div[2]/div/div/span[1]/div/a').click()


def classifica_menor_para_maior():
    navegor.find_element_by_xpath('//*[@id="ow26"]/div[1]/div').click()
    tempopc.sleep(8)
    navegor.find_element_by_xpath('//*[@id="lb"]/div/g-menu/g-menu-item[3]/div').click()


if opcao == "Copo":
    pesquisa_item("Copo")
    acessa_shopping()
    filtra_menores_valores()
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")
elif opcao == "Caneca":
    pesquisa_item("Caneca")
    acessa_shopping()
    filtra_por_valores_minimo_e_maximo(85, 100)
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")
elif opcao == "Garrafa":
    pesquisa_item("Garrafa")
    acessa_shopping()
    classifica_menor_para_maior()
    escrever.alert("Origada por aguardar o Rpa terminou a pesquisa, pode verificar")