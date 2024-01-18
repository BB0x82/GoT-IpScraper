import os
import re
import ctypes
import requests
from colorama import Fore, init
import threading
import time

ctypes.windll.kernel32.SetConsoleTitleW("GoT-Ipscrape Tool PREMIUM          |          Credit: 0x.82          |          Version: 1.0")

def extract_ips(text):
    ips = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', text)
    return ips

def filter_ips(url, ip_type, include_ports):
    try:
        response = requests.get(url)
        ips = extract_ips(response.text)
        filtered_ips = [ip.split(":") for ip in ips]

        folder_name = f'{ip_type}_GoT-ips'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        filename = 'GoT-ips_med_ports.txt' if include_ports else 'GoT-ips_uden_ports.txt'
        file_path = os.path.join(folder_name, filename)

        with open(file_path, 'a') as file:
            for ip, port in filtered_ips:
                if not include_ports:
                    ip = ip.rstrip(':')
                file.write(f'{ip}{":" + port if include_ports else ""}\n')

        num_ips = len(filtered_ips)
        print(Fore.WHITE + f"   Scraped "f"{Fore.LIGHTGREEN_EX}{num_ips} {ip_type}"f" IPs " f"{Fore.RED}IK GLEM CREDIT DIN HUND!")
    except Exception as e:
        print(Fore.RED + f"   Der skete en fejl ved scraping af {url}: {e}")

def check_proxy(proxy, ip_type, working_folder, non_working_folder, total_ips, checked_ips, working_count, non_working_count):
    try:
        proxies = {ip_type: f'{ip_type}://{proxy}'}
        response = requests.get('http://www.google.com', proxies=proxies, timeout=5)

        checked_ips[0] += 1

        if response.ok:
            with open(os.path.join(working_folder, f'online_{ip_type}_proxies.txt'), 'a') as file:
                file.write(f'{proxy}\n')
                working_count[0] += 1
                print(Fore.GREEN + f'Proxy {proxy} er online.')
        else:
            with open(os.path.join(non_working_folder, f'offline_{ip_type}_proxies.txt'), 'a') as file:
                file.write(f'{proxy}\n')
                non_working_count[0] += 1
                print(Fore.RED + f'Proxy {proxy} er offline.')


        progress = int((checked_ips[0] / total_ips) * 100)
        remain_count = total_ips - checked_ips[0]
        ctypes.windll.kernel32.SetConsoleTitleW(f"GoT-Ipscrape Tool PREMIUM | Progress: {progress}% | Online: {working_count[0]} | Offline: {non_working_count[0]} | Tilbage: {remain_count}")

    except requests.RequestException:
        checked_ips[0] += 1

def check_proxies(file_path, ip_type, num_threads):
    try:
        with open(file_path, 'r') as file:
            ips = [line.strip() for line in file]

        working_folder = f'online_{ip_type}_proxies'
        non_working_folder = f'offline_{ip_type}_proxies'

        if not os.path.exists(working_folder):
            os.makedirs(working_folder)

        if not os.path.exists(non_working_folder):
            os.makedirs(non_working_folder)

        checked_ips = [0]
        working_count = [0]
        non_working_count = [0]
        total_ips = len(ips)


        num_threads = min(num_threads, 20)
        threads = []

        for i in range(num_threads):
            for j in range(i, total_ips, num_threads):
                ip = ips[j]
                thread = threading.Thread(target=check_proxy, args=(ip, ip_type, working_folder, non_working_folder, total_ips, checked_ips, working_count, non_working_count))
                threads.append(thread)
                thread.start()
                time.sleep(0.1)  


        for thread in threads:
            thread.join()

        num_ips = len(ips)
        num_working = len(os.listdir(working_folder))
        num_non_working = len(os.listdir(non_working_folder))
        print(Fore.RED + f"Checked {num_ips} {ip_type} proxies")
        print(Fore.GREEN + f"Online Proxies: {num_working}")
        print(Fore.RED + f"Offline Proxies: {num_non_working}")

    except Exception as e:
        print(Fore.RED + f"Der skete en fejl ved checking af {file_path}: {e}")




def main():
    default_url = "https://github.com/proxifly/free-proxy-list/blob/main/proxies/all/data.txt"

    http_url = "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt"
    http_url1 = "https://api.proxyscrape.com/?request=getproxies&proxytype=http"
    http_url2 = "https://openproxy.space/list/http"
    http_url3 = "https://api.proxyscrape.com/v2/?request=getproxies&proxytype=http"
    http_url4 = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    http_url5 = "https://api.openproxylist.xyz/http.txt"
    http_url6 = "https://alexa.lr2b.com/proxylist.txt"
    http_url7 = "https://multiproxy.org/txt_all/proxy.txt"
    http_url8 = "https://rootjazz.com/proxies/proxies.txt"
    http_url9 = "https://spys.me/proxy.txt"
    http_url0 = "https://proxyspace.pro/http.txt"

    socks4_url = "https://github.com/vakhov/fresh-proxy-list/raw/master/socks4.txt"
    socks4_url1 = "https://openproxy.space/list/socks4"
    socks4_url2 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4"
    socks4_url3 = "https://api.proxyscrape.com/v2/?request=getproxies&proxytype=socks4"
    socks4_url4 = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
    socks4_url5 = "https://proxyspace.pro/socks4.txt"

    socks5_url = "https://github.com/vakhov/fresh-proxy-list/raw/master/socks5.txt"
    socks5_url1 = "https://openproxy.space/list/socks5"
    socks5_url2 = "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5"
    socks5_url3 = "https://api.proxyscrape.com/v2/?request=getproxies&proxytype=socks5"
    socks5_url4 = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
    socks5_url5 = "https://proxyspace.pro/socks5.txt"
    socks5_url6 = "https://spys.me/socks.txt"


    while True:
        os.system('cls')
        init(autoreset=True)
        print("")
        print(f'{Fore.RED}'
              '                                       ██████╗  ██████╗ ████████╗   ██╗██████╗ \n'
              '                                      ██╔════╝ ██╔═══██╗╚══██╔══╝   ██║██╔══██╗\n'
              '                                      ██║  ███╗██║   ██║   ██║█████╗██║██████╔╝\n'
              '                                      ██║   ██║██║   ██║   ██║╚════╝██║██╔═══╝ \n'
              '                                      ╚██████╔╝╚██████╔╝   ██║      ██║██║     \n'
              '                                       ╚═════╝  ╚═════╝    ╚═╝      ╚═╝╚═╝     \n')
        print(f'{Fore.RED}                                 Bemærk at Proxy listen opdateres efter 5-10 minutter!')
        print(f'{Fore.RED}                                                Credits: GoT 0x.82')
        print("")
        print(f'{Fore.RED}  Vælg en handling:{Fore.RESET}')
        print(f'{Fore.GREEN}  1. Scrap IPs{Fore.RESET}')
        print(f'{Fore.GREEN}  2. Check Proxies{Fore.RESET}')
        print("")
        print(f'{Fore.LIGHTRED_EX}  3. Quit{Fore.RESET}')
        print("")

        choice = input(f'{Fore.WHITE}  Dit valg: {Fore.RESET}').lower().strip()

        if choice == '1':
            ip_type = input('  Type ip ('f'{Fore.GREEN}http, socks4, socks5' f'{Fore.RESET}): ').strip()
            include_ports = input('  Ports? ('f'{Fore.GREEN}ja/nej' f'{Fore.RESET}): ').lower().strip() == 'ja'

            if ip_type == 'http':
                urls = [http_url, default_url, http_url1, http_url2, http_url3, http_url4, http_url5, http_url6, http_url7, http_url8, http_url9, http_url0]
            elif ip_type == 'socks4':
                urls = [socks4_url, default_url, socks4_url1, socks4_url2, socks4_url3, socks4_url4, socks4_url5]
            elif ip_type == 'socks5':
                urls = [socks5_url, default_url, socks5_url1, socks5_url2, socks5_url3, socks5_url4, socks5_url5, socks5_url6]
            else:
                print(f'{Fore.RED}  Ugyldig indtastning. Vælg "http", "socks4", eller "socks5".{Fore.RESET}')
                continue

            for url in urls:
                filter_ips(url, ip_type, include_ports)

        elif choice == '2':
            ip_type = input('  Type ip ('f'{Fore.GREEN}http, socks4, socks5' f'{Fore.RESET}): ').strip()
            file_path = input(f'  Indtast stien til filen med {ip_type} proxies: ').strip()
            num_threads = int(input('  Threads(max 20): '))

            if not os.path.isfile(file_path):
                print(f'{Fore.RED}  Filen blev ikke fundet. Kontroller stien og prøv igen.{Fore.RESET}')
                continue

            check_proxies(file_path, ip_type, num_threads)

        elif choice == '3':
            exit()

        else:
            print(f'{Fore.RED}  ERROR. Vælg "1", "2", eller "3".')
            continue

if __name__ == '__main__':
    main()