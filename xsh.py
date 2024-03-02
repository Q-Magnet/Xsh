from pywifi import PyWiFi, const
from time import strftime, localtime # strftime localtime
from getpass import getuser
from socket import gethostname
import os
from colorama import Back, Fore, init
from sys import argv
from platform import platform, system
from psutil import sensors_battery


init()
def fg_color(_fgc):
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
    elif _fgc == 'black':
        out = Fore.BLACK
    elif _fgc == 'white':
        out = Fore.WHITE
    elif _fgc == 'lblack':
        out = Fore.LIGHTBLACK_EX
    elif _fgc == 'lred':
        out = Fore.LIGHTRED_EX
    elif _fgc == 'lblue':
        out = Fore.LIGHTBLUE_EX
    elif _fgc == 'lgreen':
        out = Fore.LIGHTGREEN_EX
    elif _fgc == 'lyellow':
        out = Fore.LIGHTYELLOW_EX
    elif _fgc == 'lcyan':
        out = Fore.LIGHTCYAN_EX
    elif _fgc == 'lmagneta':
        out = Fore.LIGHTMAGENTA_EX
    return out
def bg_color(_bgc):
    if _bgc == 'red':
        out = Back.RED  
    elif _bgc == 'blue':
        out = Back.BLUE  
    elif _bgc == 'green':
        out = Back.GREEN  
    elif _bgc == 'reset':
        out = Back.RESET  
    elif _bgc == 'yellow':
        out = Back.YELLOW  
    elif _bgc == 'cyan':
        out = Back.CYAN  
    elif _bgc == 'magneta':
        out = Back.MAGENTA  
    elif _bgc == 'black':
        out = Back.BLACK  
    elif _bgc == 'white':
        out = Back.WHITE  
    elif _bgc == 'lblack':
        out = Back.LIGHTBLACK_EX  
    elif _bgc == 'lred':
        out = Back.LIGHTRED_EX  
    elif _bgc == 'lblue':
        out = Back.LIGHTBLUE_EX  
    elif _bgc == 'lgreen':
        out = Back.LIGHTGREEN_EX  
    elif _bgc == 'lyellow':
        out = Back.LIGHTYELLOW_EX  
    elif _bgc == 'lcyan':
        out = Back.LIGHTCYAN_EX  
    elif _bgc == 'lmagneta':
        out = Back.LIGHTMAGENTA_EX
    return out
def text(text, _fgc, _bgc='reset'):
    _fgc = _fgc.lower()
    _bgc = _bgc.lower()
    tx = text
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
    elif _fgc == 'black':
        out = Fore.BLACK
    elif _fgc == 'white':
        out = Fore.WHITE
    elif _fgc == 'lblack':
        out = Fore.LIGHTBLACK_EX
    elif _fgc == 'lred':
        out = Fore.LIGHTRED_EX
    elif _fgc == 'lblue':
        out = Fore.LIGHTBLUE_EX
    elif _fgc == 'lgreen':
        out = Fore.LIGHTGREEN_EX
    elif _fgc == 'lyellow':
        out = Fore.LIGHTYELLOW_EX
    elif _fgc == 'lcyan':
        out = Fore.LIGHTCYAN_EX
    elif _fgc == 'lmagneta':
        out = Fore.LIGHTMAGENTA_EX
    else:
        print('E')
    if _bgc == 'red':
        out = out + Back.RED + tx
    elif _bgc == 'blue':
        out = out + Back.BLUE + tx
    elif _bgc == 'green':
        out = out + Back.GREEN + tx
    elif _bgc == 'reset':
        out = out + Back.RESET + tx
    elif _bgc == 'yellow':
        out = out + Back.YELLOW + tx
    elif _bgc == 'cyan':
        out = out + Back.CYAN + tx
    elif _bgc == 'magneta':
        out = out + Back.MAGENTA + tx
    elif _bgc == 'black':
        out = out + Back.BLACK + tx
    elif _bgc == 'white':
        out = out + Back.WHITE + tx
    elif _bgc == 'lblack':
        out = out + Back.LIGHTBLACK_EX + tx
    elif _bgc == 'lred':
        out = out + Back.LIGHTRED_EX + tx
    elif _bgc == 'lblue':
        out = out + Back.LIGHTBLUE_EX + tx
    elif _bgc == 'lgreen':
        out = out + Back.LIGHTGREEN_EX + tx
    elif _bgc == 'lyellow':
        out = out + Back.LIGHTYELLOW_EX + tx
    elif _bgc == 'lcyan':
        out = out + Back.LIGHTCYAN_EX + tx
    elif _bgc == 'lmagneta':
        out = out + Back.LIGHTMAGENTA_EX + tx
    return out + Fore.RESET
def createprompt():
    prompt = prompt_rule
    prompt = prompt.replace('$u', username)
    prompt = prompt.replace('$h', gethostname())
    prompt = prompt.replace('$p', pwd)
    prompt = prompt.replace('$t', strftime('%Y-%m-%d %H:%M:%S', localtime()))
    prompt = prompt.replace('$T', strftime('%H:%M:%S', localtime()))
    prompt = prompt.replace('$P', str(os.getpid()))
    prompt = prompt.replace('$o', platform())
    p = sensors_battery().percent
    prompt = prompt.replace('$b', str(p))
    if p < 10:
        b = '  '
    elif p < 40:
        b = '  '
    elif p < 60:
        b = '  '
    elif p < 80:
        b = '  '
    elif p <= 100:
        b = '  '
    prompt = prompt.replace('$B', b)
    
    wifi = PyWiFi().interfaces()[0]
    if wifi.status == const.IFACE_DISCONNECTED:
        w = '󰖪 '
    else:
        w = '󰖩 '
    prompt = prompt.replace('$w', w)
    #if IsAdmin:
    #    prompt = prompt.replace('$a', 'Administrator')
    #else:
    #    prompt = prompt.replace('$a', 'User')
    if system() == 'Windows':
        prompt = prompt.replace('$os', ' Windows')
    elif system() == 'Linux':
        prompt = prompt.replace('$os', ' Linux')
    else:
        prompt = prompt.replace('$os', '? Unknown')
    return prompt
#with open(os.path.dirname(__file__) + '\\style.txt', 'r') as file:
#    prompt.rule = file.read()
#prompt_rule = f'┌── {text("", "white")}{text(" Wsh", "green", "white")} {text('$u@$h', 'green', "white")} {text('$p', 'cyan', "white")} {text('PID:$P', 'lred', "white")} {text(' Windows', 'lblue', "white")} {text('$B$b%', 'yellow', "white")} {text('$w', 'magneta', "white")} {text("", "white")}\n└── '
prompt_rule = ''.join(['┌── ',
                       text("", "red"),
                       text(" Xsh ", "white", "red"),
                       text("", "red", "lcyan"),
                       text(' $p ', 'black', "lcyan"),
                       text("", "lcyan", "lgreen"),
                       text(' $u@$h ', 'black', "lgreen"),
                       text("", "lgreen", "white"),
                       text(' PID:$P  ', 'lred', "white"),
                       text('$o  ', 'lblue', "white"),
                       text('$B$b%  ', 'yellow', "white"),
                       text('$w', 'black', "white"),
                       text("", "white"),
                       '\n└── '])
uin = '' # User Input
pwd = 'C:\\' 
username = getuser()
if '-set-root' in argv:
    username = 'root'
while True:
    if pwd[-1] != '\\':
        pwd = pwd + '\\'
    #prompt = f'{text(username+"@"+gethostname(), "green")} {text(pwd, "blue")} {text("$", "yellow")} '
    prompt = createprompt()
    uin = input(prompt).split(' ')
    for i in range(len(uin)):
        try:
            if uin[i+1] != '.':
                uin[i] = uin[i].replace('.', pwd[:-1])
        except:
            0
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
            print(0)
            print('Unsupported linux-like directory')
        elif len(uin) == 2 and uin[1] == '..':
            pwd = pwd.split('\\')
            pwd.pop()
            pwd.pop()
            pwd = '\\'.join(pwd)
        elif os.path.exists(' '.join(uin[1:])) and not os.path.isfile(' '.join(uin[1:])):
            pwd = ' '.join(uin[1:])
        elif len(uin) == 2 and len(uin[1]) >= 2 and uin[1][1] == '\\':
            pwd = uin[1]
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
            os.system('cd ' + pwd + ' & ' + uin[0][2:])
        elif os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0]) or os.path.isfile(os.path.dirname(__file__) + '\\exec\\' + uin[0] + '.exe'):
            os.system('cd ' + os.path.dirname(__file__) + '\\exec\\ & ' + uin[0])
        elif os.path.isfile(' '.join(uin)) or os.path.isfile(' '.join(uin) + '.bat') or os.path.isfile(' '.join(uin) + '.exe') or os.path.isfile(' '.join(uin) + '.cmd') or os.path.isfile(' '.join(uin) + '.com'):
            os.system(' '.join(uin))
        else:
            print('Unsupported Command: ' + uin[0])