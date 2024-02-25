import time as t
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
def createprompt():
    prompt = prompt_rule
    prompt = prompt.replace('$u', username)
    prompt = prompt.replace('$h', gethostname())
    prompt = prompt.replace('$p', pwd)
    prompt = prompt.replace('$t', t.strftime('%Y-%m-%d %H:%M:%S', t.localtime()))
    prompt = prompt.replace('$T', t.strftime('%H:%M:%S', t.localtime()))
    prompt = prompt.replace('$P', str(os.getpid()))

    #if IsAdmin:
    #    prompt = prompt.replace('$a', 'Administrator')
    #else:
    #    prompt = prompt.replace('$a', 'User')
    return prompt
with open(os.path.dirname(__file__) + '\\style.txt', 'r') as file:
    prompt.rule = file.read()
#prompt_rule = f
'''
┌── Wsh {text('$u', 'green')}{text('@$h', 'green')} {text('$p', 'blue')} {text('PID:$P', 'red')}
└─ 
'''
uin = '' # User Input
pwd = 'C:\\' 
username = getuser()
if '-set-root' in sys.argv:
    username = 'root'
print(text('bash', 'red') + ' type "xcat help" to get a list of usable commands')
while True:
    if pwd[-1] != '\\':
        pwd = pwd + '\\'
    #prompt = f'{text(username+"@"+gethostname(), "green")} {text(pwd, "blue")} {text("$", "yellow")} '
    prompt = createprompt()
    uin = input(prompt).split(' ')
    for i in range(len(uin)):
        uin[i] = uin[i].replace('.', pwd[:-1])
    # i really dont know whats this
    #if '.' in uin:
    #    for j in range(len(uin)):
    #        for i in range(len(uin[j])):
    #            if uin[j][i] == '.':
    #                if len(uin[j]) > 1 and uin[j][i-1] == '.':
    #                    0
    #                elif len(uin[j]) > i+1 and uin[j][i+1] == '.':
    #                    0
    #                else:
    #                    uin[j] = list(uin[j])
    #                    uin[j][i] = pwd
    #                    uin[j] = ''.join(uin[j])
    if uin[0] == 'cd':
        pwd_b = pwd + ''
        
        obj1 = uin[1]
        if obj1[1] == '"': # Fix Space in Dir Bug
            try:
                for i in range(99999):
                    obj1 = obj1 + uin[i+2]
                    if obj1[-1] == '"':
                        break
            except:
                print('Bad directory')
        if len(uin) == 2 and len(uin[1]) >= 1 and uin[1][0] == '\\':
            print('Unsupported linux-like directory')
        elif os.path.exists(' '.join(uin[1:])) and not os.path.isfile(' '.join(uin[1:])):
            pwd = ' '.join(uin[1:])
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
        print(' '.join(dirs) + ' ' + ' '.join(file))
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

    # Other Commands
    elif uin[0] == 'do':
        if len(uin) < 2:
            print('usage: do <arg1> <arg2> ...')
        else:
            if os.system(' '.join(uin[1:])) == 1:
                print(f'Successfully executed {" ".join(uin[i:])} via system terminal')
    elif uin[0] == 'xcat':
        if len(uin) < 2:
            print('usage: xcat <filename>')
        else:
            if uin[1] == 'help':
                uin[1] = os.path.dirname(__file__) + "\\help.color"
            with open(uin[1]) as file:
                catcon = file.read()
            replacestr = ['$RED.', '$GRE.', '$BLU.', '$YEL.', ' /']
            replaceto =  [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET]
            for i in replacestr:
                catcon = catcon.replace(i, replaceto[replacestr.index(i)])
            print(catcon)
    elif uin[0] == 'sudo':
        if len(uin) < 2:
            print('usage: sudo <EXE file> <argvs> ...')
        else:
            os.system(f'mshta vbscript:CreateObject("Shell.Application").ShellExecute("{" ".join(uin[1:])}","/c %~s0 ::","","runas",1)(window.close)')
    elif ' '.join(uin) == '':
        0
    else:
        if uin[0][:2] == '.\\' and (os.path.isfile(pwd + uin[0][2:] or os.path.isfile(pwd + uin[0][2:] + '.exe') or os.path.isfile(pwd + uin[0][2:] + '.bat') or os.path.isfile(pwd + uin[0][2:] + '.cmd') or os.path.isfile(pwd + uin[0][2:] + '.com'))):
            os.system('cd ' + pwd + ' & start ' + uin[0][2:])
        elif os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0]) or os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0] + '.exe'):
            os.system('cd ' + os.path.dirname(__file__) + '\\exec\\ & ' + uin[0])
        elif os.path.isfile(' '.join(uin)) or os.path.isfile(' '.join(uin) + '.bat') or os.path.isfile(' '.join(uin) + '.exe') or os.path.isfile(' '.join(uin) + '.cmd') or os.path.isfile(' '.join(uin) + '.com'):
            os.system(' '.join(uin))
        else:
            print('Unsupported Command: ' + uin[0])