import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style
import os


colorama.init()


def program():

    hash_cod = input('Input Hash: ')
    longitud = len(hash_cod)

    url = 'https://hashes.com/en/tools/hash_identifier'



    csrf = requests.get(url=url)
    csrf = csrf.text


    soup = BeautifulSoup(csrf, 'html.parser')
    csrf_input = soup.find('input', {'name': 'csrf_token'})
    csrf_token = csrf_input['value']



    url = '	https://hashes.com/en/tools/hash_identifier'


    data = f'csrf_token={csrf_token}&hashes={hash_cod}&submitted=true'

    headers = {
        
        "Host": "hashes.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://hashes.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://hashes.com/en/tools/hash_identifier",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
        
        }


    client = requests.post(url=url, headers=headers, data=data)

    result = client.text
    


    if 'Possible algorithms' in result:
        
        soup = BeautifulSoup(result, 'html.parser')
        div_text = soup.find('div', {'class': 'py-1'}).text
        cod = div_text.split(' - ')[1]
        possible_algorithm = div_text.split(' - Possible algorithms: ')[1]
        
        valor_bit = int(longitud) * 8
    
        



        clear_terminal()
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"-------------------𝐻𝑎𝑠ℎ 𝑖𝑑𝑒𝑛𝑡𝑖𝑓𝑖𝑐𝑎𝑑𝑜𝑟------------\n\n---------------Code By @Criftcking_Real | GhostHat_Real---------------"+Fore.RESET)
        print("\n")


        

        
        print(Fore.BLUE+"Hash: "+Fore.LIGHTRED_EX+hash_cod+Fore.RESET)
        print(Fore.BLUE+"Longitud: "+Fore.LIGHTRED_EX+str(longitud)+Fore.RESET)
        print(Fore.BLUE+"Valor en Bits: "+Fore.LIGHTRED_EX+str(valor_bit)+' (8 Bytes)'+Fore.RESET)
        print()
        print(Fore.BLUE+'Posible algoritmo: '+Fore.LIGHTRED_EX+possible_algorithm+Fore.RESET)
        if 'Possible algorithms' in cod:
            print(Fore.BLUE+"Valor Codificado: "+Fore.LIGHTRED_EX+"No decifrado"+Fore.RESET)
        else:
            print(Fore.BLUE+"Valor Codificado: "+Fore.LIGHTRED_EX+cod+Fore.RESET)

    elif 'Could not identify' in result:
        print(Fore.RED+"Error: "+"Hash No identificado"+Fore.RESET)
    else:
        print("Error Desconocido")



def clear_terminal():
    if os.name == 'posix':  # Linux
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print("No se pudo determinar el sistema operativo.")

clear_terminal()



print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"-------------------𝐻𝑎𝑠ℎ 𝑖𝑑𝑒𝑛𝑡𝑖𝑓𝑖𝑐𝑎𝑑𝑜𝑟------------\n\n---------------Code By @Criftcking_Real | GhostHat_Real---------------"+Fore.RESET)
print("\n\n\n\n")

program()