sudo apt-get install tor
sudo /etc/init.d/tor restart
tor --hash-password 12345
sudo vim /etc/tor/torrc
#### PONER ESTO EN EL TORRC
ControlPort 9051
HashedControlPassword 16:C4067B4AF8FB4EBE60DB39ACE563ACC8DDD676274EAF8CE706EF5E2507
CookieAuthentication 1
###
sudo /etc/init.d/tor restart
### si hay problemas al habilitar el servicio ejecuta:
tor --controlport 9051 &
###### para que quede backgrpund el servicio

pip install stem 


#####################
sudo dpkg -i expressvpn_3.78.0.0-1_amd64.deb 

expressvpn activate

EXELTBV5TRSUYK4D93DBV5R

expressvpn preferences set send_diagnostics false

sudo apt install openvpn openvpn-systemd-resolved

expressvpn install-chrome-extension

expressvpn preferences set network_lock off




