import socket

def get_website_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None
print ("\033[0;35m+++++++++++++++++++++++++++")
print ("\033[0;35m+  \033[0;33m Cek IP situs web      \033[0;35m+")
print ("\033[0;35m+++++++++++++++++++++++++++")
print ("\033[0;36m---------------------------")
print ("\033[0;36m- \033[0;35mcontoh : google.com     \033[0;36m-")
print ("\033[0;36m---------------------------")
if __name__ == '__main__':
    domain = input('\33[0;33mEnter the domain name:\33[0;36m ')
    ip = get_website_ip(domain)
    if ip:
        print(f'\33[0;31mThe IP address of \33[0;32m{domain} is  \33[0;33m{ip}')
    else:
        print(f'\33[0;31mFailed to retrieve the IP address of \33[0;32m{domain}')

#cara install di terminal
# apt update && apt upgrade -y
# pkg install python3
# pkg install git
# git clone https://github.com/MaulanaDevtech422/ipceker
# cd ipceker
# jalankan script dengan perintah
# python3 ipceker.py
# selesai dan masukkan domain setiap webseit contoh: google.com, Facebook.com dan lain2
