import interface.home.main_logo as main_logo
import interface.home.main_menu as main_menu
import interface.installer.inst_logo as inst_logo
import interface.installer.inst_menu as inst_menu
from passwordgenerator import pwgenerator
from time import sleep
from faker import Faker
from colorama import Fore
import requests
import pprint
import os
import socket
import sys
import time

color_blue = Fore.BLUE
color_red = Fore.RED
color_magenta = Fore.MAGENTA
color_green = Fore.GREEN
color_white = Fore.WHITE
color_cyan = Fore.CYAN
color_yellow = Fore.YELLOW

user = 'root'
password = 'root'
user_input = str(input(f'{color_green}User{color_yellow}: '))
password_input = str(input(f'{color_green}Password{color_yellow}: '))

sleep(1)
os.system('cls')

clock = time.strftime('%H:%M:%S')



def returnf():
    print('\n')
    print(f'{color_white}▀' * 81)
    sleep(1)
    main()


def returnins():
    inst_logo.installer_logo()
    inst_menu.installer_menu()


def otheroption():
    print('the selected option does not exist')
    sleep(2)
    os.system('cls')
    returnf()


def req_ip():
    try:
        sleep(0.5)
        os.system('cls')
        API_KEY = 'kBtOz67nfvQq8t8HN6fA'
        ip_input = str(input(f'{color_green}IP{color_yellow}>'))
        req = requests.get(f'https://extreme-ip-lookup.com/json/{ip_input}?key={API_KEY}')
        req_json = req.json()
        sleep(0.5)
        pprint.pprint(req_json)
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def ping():
    try:
        sleep(0.5)
        os.system('cls')
        hostname = input(f'{color_green}Host{color_yellow}> ')
        response = os.system(f'ping {hostname}')
        if response == 0:
            print(f'{color_white}Status: {color_green}Online')
        else:
            print(f'{color_white}Status: {color_red}Offline')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def pwgen():
    try:
        sleep(0.5)
        os.system('cls')
        passw = pwgenerator.generate()
        sleep(0.5)
        print(f'{color_white}password: {color_green}{passw}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def faken():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        name = fake.name()
        sleep(0.5)
        print(f'{color_white}fake name: {color_green}{name}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def fakeaddr():
    try:
        sleep(0.5)
        os.system('cls')
        fake = Faker()
        addr = fake.address()
        print(f'{color_white}fake address: {color_green}{addr}')
        returnf()
    except KeyboardInterrupt:
        print('Program interrupted')


def speedt():
    sleep(0.5)
    os.system('cls')
    os.system('speedtest --secure')
    returnf()


def dmlookup():

    domain = input(f'{color_green}domain{color_yellow}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'nslookup {domain}')
    returnf()


def flushdns():
    sleep(0.5)
    os.system('cls')
    os.system('ipconfig /flushdns')
    returnf()


def portscan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input(f'{color_green}IP{color_yellow}> ')
    range_port = int(input(f'{color_green}Range{color_yellow}> '))
    for ports in range(range_port):
        connect = s.connect_ex((host, ports))
        if connect == 0:
            print(f'{color_white}Port: {color_green}{ports} opened')
            s.close()
        else:
            print(f'{color_white}Port: {color_yellow}{ports} closed')
            s.close()
    returnf()


def tracing():
    host = input(f'{color_green}Host{color_yellow}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'tracert {host}')
    returnf()


def backupf():
    archive = input(f'{color_green}Archive/folder path{color_yellow}>')
    new_path = input(f'{color_green}Backup path{color_yellow}>')
    sleep(0.5)
    os.system('cls')
    os.system(f'robocopy {archive} {new_path}')
    returnf()


def exitl():
    os.system('cls')
    confirm = input(
        f'{color_white}Are you sure you want to leave? [{color_green}Y{color_white}/{color_yellow}N{color_white}]>'
    ).strip().upper()

    if confirm == 'Y':
        print(f'{color_white}departure time:{color_green}{clock}')
        sleep(2)
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        main()

def openvpn():
    os.system('winget install openvpn')


def vscodium():
    os.system('winget install -e --id VSCodium.VSCodium')


def chrome():
    os.system('winget install -e --id Google.Chrome')


def operagx():
    os.system('winget install -e --id Opera.OperaGX')


def vscode():
    os.system('winget install -e --id Microsoft.VisualStudioCode')


def discord():
    os.system('winget install -e --id Discord.Discord')


def steam():
    os.system('winget install -e --id Valve.Steam')


def hyper():
    os.system('winget install -e --id Zeit.Hyper')


def wireshark():
    os.system('winget install -e --id WiresharkFoundation.Wireshark')


def whatsapp():
    os.system('winget install -e --id WhatsApp.WhatsApp')


def vmware():
    os.system('winget install -e --id VMware.WorkstationPlayer')


def vlc():
    os.system('winget install -e --id VideoLAN.VLC')


def main():
    try:
        if user_input == user and password_input == password:
            main_logo.logo()
            main_menu.menu()
            choice = int(input(f'{color_yellow}({color_green}root@root{color_yellow}){color_yellow}> '))
            match choice:
                case 1:
                    req_ip()
                case 2:
                    ping()
                case 3:
                    faken()
                case 4:
                    fakeaddr()
                case 5:
                    speedt()
                case 6:
                    dmlookup()
                case 7:
                    flushdns()
                case 8:
                    portscan()
                case 9:
                    tracing()
                case 10:
                    backupf()
                case 11:
                    sleep(0.5)
                    inst_logo.installer_logo()
                    inst_menu.installer_menu()
                    choice_installer = int(input(f'{color_yellow}({color_green}root@root{color_yellow}){color_yellow}> '))
                    match choice_installer:
                        case 1:
                            openvpn()
                        case 2:
                            vscodium()
                        case 3:
                            chrome()
                        case 4:
                            operagx()
                        case 5:
                            vscode()
                        case 6:
                            discord()
                        case 7:
                            steam()
                        case 8:
                            hyper()
                        case 9:
                            wireshark()
                        case 10:
                            whatsapp()
                        case 11:
                            vmware()
                        case 12:
                            vlc()
                        case 0:
                            os.system('cls')
                            main()
                        case _:
                            otheroption()
                case 0:
                    exitl()
                case _:
                    otheroption()
        else:
            print(f'{color_yellow} User or Password is invalid!')
    except KeyboardInterrupt:
        print('Program interrupted')


main()
