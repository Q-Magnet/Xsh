from getpass import getuser
from socket import gethostname
import os
from colorama import Back, Fore, init
import sys

init()
def text(text, _fgc, _bgc=0):
    
    out = ''
    if _fgc == 'red':
        out = Fore.RED
    elif _fgc == 'blue':
        out = Fore.BLUE
    elif _fgc == 'green':
        out = Fore.GREEN
    elif _fgc == 'reset':
        out = Fore.RESET
    elif _fgc == 'yellow':
        out = Fore.YELLOW
    elif _fgc == 'cyan':
        out = Fore.CYAN
    elif _fgc == 'magneta':
        out = Fore.MAGENTA
    if _bgc == 'red':
        out = out + Back.RED
    elif _bgc == 'blue':
        out = out + Back.BLUE
    elif _bgc == 'green':
        out = out + Back.GREEN
    elif _bgc == 'yellow':
        out = out + Back.YELLOW
    elif _bgc == 'cyan':
        out = out + Back.CYAN
    elif _bgc == 'magneta':
        out = out + Back.MAGENTA
    return out + text + Fore.RESET + Back.RESET

uin = '' # User Input
pwd = 'C:\\' 
username = getuser()
if '-set-root' in sys.argv:
    username = 'root'
print('What a wonderful ' + text('bash', 'red') + '!')
while True:
    if pwd[-1] != '\\':
        pwd = pwd + '\\'
    prompt = f'{text(username+"@"+gethostname(), "green")} {text(pwd, "blue")} {text("$", "yellow")} '
    uin = input(prompt).split(' ')
    if '.' in uin:
        for j in range(len(uin)):
            for i in range(len(uin[j])):
                if uin[j][i] == '.':
                    if len(uin[j]) > 1 and uin[j][i-1] == '.':
                        0
                    elif len(uin[j]) > i+1 and uin[j][i+1] == '.':
                        0
                    else:
                        uin[j] = list(uin[j])
                        uin[j][i] = pwd
                        uin[j] = ''.join(uin[j])
    if uin[0] == 'cd':
        pwd_b = pwd + ''
        if len(uin) == 2 and len(uin[1]) >= 1 and uin[1][0] == '\\':
            print('Unsupported linux-like directory')
        elif len(uin) == 2 and len(uin[1]) >= 2 and uin[1][1] == '\\':
            pwd = uin[1]
        elif len(uin) == 2 and len(uin[1]) == 2 and uin[1] == '..':
            if pwd[-1] != '\\':
                pwd = pwd.split('\\')
                pwd.pop()
                pwd = '\\'.join(pwd)
            else:
                pwd = pwd.split('\\')
                pwd.pop()
                pwd.pop()
                pwd = '\\'.join(pwd)
        else:
            if pwd[-1] == '\\':
                pwd = pwd + uin[1]
        if not os.path.exists(pwd):
            print('cd: no such file or directory: ' + uin[1])
            pwd = pwd_b
    elif uin[0] == 'echo':
        if len(uin) > 1:
            print(' '.join(uin[1:]))
    elif uin[0] == 'exit':
        exit()
    elif uin[0] == 'ls':
        files = os.listdir(pwd)
        file = []
        dirs = []
        for i in files:
            if os.path.isfile(pwd + i):
                #print(i, end=' ')
                if ' ' in i:
                    i = '"' + i + '"'
                file.append(text(i, 'green'))
            else:
                #print(i, end=' ')
                if ' ' in i:
                    i = '"' + i + '"'
                dirs.append(text(i, 'blue'))
        print(' '.join(dirs) + ' '.join(file))
    elif uin[0] == 'clear':
        os.system('cls')
    elif uin[0] == 'ping':
        os.system('ping ' + ' '.join(uin[1:]))
    elif uin[0] == 'cat':
        if len(uin) == 2:
            with open(pwd + uin[1], 'r') as f:
                print(f.read())
        else:
            print('usage: cat <file>')
    elif uin[0] == 'cp':
        if not '-r' in uin:
            if len(uin) == 3:
                with open(uin[2], 'r') as file:
                    cont = file.read()
                with open(uin[3], 'w') as file:
                    file.write(cont)
            else:
                print('usage: cp [-r] <file> <destination>')
        else:
            if len(uin) == 4:
                uin.remove('-r')
                os.system(f'cd {pwd} & xcopy {uin[1]} {uin[2]} /E /H /C /I')
            else:
                print('usage: cp [-r] <file> <destination>')
    elif uin[0] == 'rm':
        if '-rf' in uin and len(uin) == 3:
            uin.remove('-rf')
            os.system(f'cd {pwd} & rd /s /q {uin[1]}')
        elif '-rf' in uin:
            print('usage: rm [-rf] <Filename>')
        elif len(uin) == 2:
            os.system(f'cd {pwd} & rd /q {uin[1]}')
        else:
            print('usage: rm [-rf] <Filename>')
    elif uin[0] == 'mkdir':
        if len(uin) == 2:
            os.system(f'cd {pwd} & md {uin[1]}')
        else:
            print('usage: md <Name>')
    elif uin[0] == 'touch':
        if len(uin) == 2:
            with open(pwd + uin[1], 'w') as file:
                file.write('')
    else:
        if uin[0][0:2] == '.\\' and (os.path.isfile(pwd + uin[0]) or os.path.isfile(pwd + uin[0] + '.exe')):
            os.system('cd ' + pwd + ' & start ' + uin[0])
        elif os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0]) or os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0] + '.exe'):
            os.system('cd ' + os.path.dirname(__file__) + '\\exec\\ & ' + uin[0])
        else:
            print('Unsupported Command: ' + uin[0])