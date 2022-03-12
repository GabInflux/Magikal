import requests
from time import sleep
from os import system
from pystyle import Colorate, Colors, Center

boucle1 = True
boucle2 = True

header_final = """
       \  |               _)  |            | 
      |\/ |   _` |   _` |  |  |  /   _` |  | 
      |   |  (   |  (   |  |    <   (   |  | 
     _|  _| \__,_| \__, | _| _|\_\ \__,_| _| 
                   |___/                     
  V 1.0 - Gab_#8440 - discord.gg/BtNrFc45B7\n\n\n\n"""

while boucle1:
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] Token ↓"))
    token = input("")
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] Channel ID ↓"))
    try:
        channel_id = int(input(""))
        boucle1 = False
    except:
        system('cls')
        print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Please insert a valid number ! "))
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] Command to bump ↓"))
    command = input("")

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : token
    }

while boucle2:
    requests.post(
            f"https://discord.com/api/channels/{channel_id}/messages",
            headers = headers,
            json = {"content" : command}
        )
    system('cls')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "Server bumped !"))
    print(Colorate.Horizontal(Colors.purple_to_blue, "Waiting for the next bump... !"))
    sleep(121 * 60)