import os
import time
from seleniumbase import Driver

# Función para conectar ExpressVPN a un servidor específico
def connect_expressvpn(server_location="smart"):
    print(f"Conectando a ExpressVPN ({server_location})...")
    os.system(f"expressvpn connect {server_location}")  # Conecta al servidor especificado
    time.sleep(10)  # Espera a que la conexión se establezca completamente

# Función para desconectar ExpressVPN
def disconnect_expressvpn():
    print("Desconectando ExpressVPN...")
    os.system("expressvpn disconnect")
    time.sleep(5)



def run_browser_with_vpn():
    try:
        connect_expressvpn("smart")  
        driver = Driver(uc=True,headless=False)  
        driver.uc_open_with_reconnect("https://api.ipify.org", 3) 
        #driver.get("https://api.ipify.org")  
      
        time.sleep(10)  
        driver.quit()
    except:
        disconnect_expressvpn()
    finally:
   
        disconnect_expressvpn()
        run_browser_with_vpn()

# Ejecutar el script
if __name__ == "__main__":
    run_browser_with_vpn()
