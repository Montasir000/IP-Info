import ipinfo
import os
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

logo= ('''
\033[1;33m __  __  ___  _   _ _____  _    ____ ___ ____                   |  \/  |/ _ \| \ | |_   _|/ \  / ___|_ _|  _ \                  | |\/| | | | |  \| | | | / _ \ \___ \| || |_) |                 | |  | | |_| | |\  | | |/ ___ \ ___) | ||  _ <                  |_|  |_|\___/|_| \_| |_/_/   \_\____/___|_| \_\                                                                                 \033[1;36m============================================================                                                                                                                          
 \033[1;92m[+] AUTHOR       :   Montasir Sabit             
 \x1b[1;92m[+] FACEBOOK     :   Montasir Sabit
 \x1b[1;92m[+] GITHUB       :   Montasir000 
 \033[1;92m[+] TOOLS        :   IP Information

\033[1;36m============================================================                                                          ''')

# IP Information
access_token = "d519c063eb21ef"  # Replace this with your actual access token

def print_ip_details(ip_address):
    handler = ipinfo.getHandler(access_token)
    try:
        details = handler.getDetails(ip_address)
        for key, value in details.all.items():
            print(green+f"{key}: {value}")
    except ipinfo.exceptions.RequestQuotaExceededError:
        print("Request quota exceeded. Please try again later.")
    except ipinfo.exceptions.RequestFailedError:
        print("Request to IPinfo failed. Please check your network connection.")
    except Exception as e:
        print("An error occurred:", e)

os.system("clear")
print(logo)
# Login System

user = "1234"
pwd = "1234"

while True:
    username = input(cyan+"Enter Username:")
    password = input(cyan+"Enter Password:")
    if user == username and pwd == password:
        print(green+"Login successful")
        break
    else:
        print(red+"Invalid username or password!")
os.system("clear")
print(logo)
# Prompt for IP Address and Show IP Information
ip_address = input(yellow+"Enter an IP address: ")
print_ip_details(ip_address)
