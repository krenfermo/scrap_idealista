


from seleniumbase import BaseCase
import random
from seleniumbase import Driver
import time
from seleniumbase.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import utils as ut 
from selenium.webdriver.common.keys import Keys

import requests
from stem import Signal
from stem.control import Controller

import time

 
SCRAPERAPI_KEY = "5f6fc6edaf9267d33a9fcc94214c58d9"  # Reemplaza con tu clave
SCRAPERAPI_PROXY = f"http://scraperapi:{SCRAPERAPI_KEY}@proxy-server.scraperapi.com:8001"  # Formato compatible con SeleniumBase
SCRAPERAPI_PARAMS = f"api_key={SCRAPERAPI_KEY}&render=true"



def simulate_human_interaction(driver):
    # Simula movimientos de scroll y tiempos de espera humanos
    driver.execute_script("window.scrollTo(0, 0);")  # Desplazar al principio
    driver.sleep(random.uniform(1, 3))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Desplazar al final
    driver.sleep(random.uniform(2, 4))
    driver.execute_script("window.scrollTo(0, 0);")  # Desplazar al principio
    driver.sleep(random.uniform(2, 4))
    
def accept_cookies(driver):
    try:
        driver.wait_for_element_visible("button#didomi-notice-agree-button", timeout=20)
        driver.uc_click("button#didomi-notice-agree-button")
        print("click cookies")
        return True
    except TimeoutException:
        print("El boton de cookies no se encontro o no se pudo hacer clic a tiempo.")
    except Exception as e:
        print(f"Error al aceptar cookies: {e}")
    return False

def navega(url):
    try:
        #COMPRUEBO LA IP CAMBIADA
        #make_request(url)
        
        #chrome = setup_browser()
        chrome=setup_browser_SCRAPERAPI()
        #chrome=setup_browser_TOR()
        time.sleep(1)
        chrome.sleep(random.uniform(2, 4))
        chrome.uc_open_with_reconnect(url, 3) 
        
        import datetime
        now = datetime.datetime.now()

        chrome.save_screenshot(ut.resource_path("assets/screen_{}.png".format(str(now.time()))))
        time.sleep(1)
        #return True 
        time.sleep(1)
        if not accept_cookies(chrome):
                chrome.save_screenshot(ut.resource_path(f"assets/screen_b_2.png"))
                ut.printr(f'Indice => 1 | cookies ')
                
        time.sleep(1)     
                
        simulate_human_interaction(chrome)

        chrome.save_screenshot(ut.resource_path(f"assets/screen_b_3.png"))
       
        chrome.find_element(By.XPATH, '//div[@class="main-image_first"]').click()
        
        time.sleep(2)
        chrome.save_screenshot(ut.resource_path(f"assets/screen_b_3.png"))
        chrome.find_element(By.XPATH, '//*[@id="gallery-contact-btn-new"]').click()

    
        time.sleep(2)
        chrome.save_screenshot(ut.resource_path(f"assets/screen_b_4.png"))
        # Llenar el campo de mensaje
        mensaje = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[2]/div/label/textarea')
        mensaje.clear()
        mensaje.send_keys("Hola, estoy interesado ")

        # Llenar el email
        time.sleep(2)
        print("llena interesado")
        email_input = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[3]/div[1]/div/label/div/input')
        email_input.clear()  # Limpia el campo si tiene algún valor previo
        email_input.send_keys("usuario2@ejemplo.com")  # Ingresa el correo deseado
        print("llena correo")
        time.sleep(2)
        # Llenar el teléfono
        telefono = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[3]/div[2]/div[1]/label/div/div/div/div[1]/div/input')
        telefono.clear()
        telefono.send_keys("640123456")
        print("llena nuemero")
        time.sleep(2)
        # Llenar el nombre
        nombre = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[3]/div[2]/div[2]/label/input')
        nombre.clear()
        nombre.send_keys("Juan Pérez")
        nombre.send_keys(Keys.TAB)
        time.sleep(.5)
        checkbox = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[3]/div[5]/div/label')
        checkbox.send_keys(Keys.SPACE)
        
        time.sleep(2)
        chrome.save_screenshot(ut.resource_path(f"assets/screen_b_5.png"))
        # Simular el envío del formulario (Contactar por chat)
        boton_contactar = chrome.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/div/section/div/div[4]/form/div[5]/button[1]')
        boton_contactar.click()
        time.sleep(2)
        chrome.sleep(random.uniform(2, 4))
        chrome.execute_script("window.scrollTo(0, 100)")
        print("llena")
 
        print("dio click en contactar")
 
        chrome.save_screenshot(ut.resource_path(f"assets/screen_b_6.png"))

        chrome.quit()
    except Exception as err:
        print(err)
        #chrome.quit()



def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="12345")  # Cambia según tu configuración de TOR
        controller.signal(Signal.NEWNYM)

def make_request(url):
    session = requests.Session()
    # Configurar TOR como proxy
    session.proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }

    try:
        response = session.get(url, timeout=10)
        print("IP utilizada:", session.get("https://api.ipify.org").text)
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error durante la solicitud:", e)
        return None
    
    
def setup_browser_TOR():
    print("Cambiando IP...")
    change_ip()  
    time.sleep(random.randint(5, 10))  
    print("Haciendo la solicitud...")
    
    driver = Driver(
        proxy="socks5://127.0.0.1:9050",  # Configura el proxy para TOR
        headless=False,   
        uc=True  
    )
    return driver

def setup_browser_SCRAPERAPI():
    # Configuración de ScraperAPI


    driver = Driver(
        proxy=SCRAPERAPI_PROXY,  
        headless=False,   
        uc=True  
    )
    return driver


    
if __name__ == "__main__":
    url=f"https://www.idealista.com/inmueble/103547208/"

    #url = "https://api.ipify.org"  # Reemplaza con la url del EXCEL

    #for _ in range(5):  # Realiza 5 solicitudes con IPs diferentes
    
    
    navega(url)
 