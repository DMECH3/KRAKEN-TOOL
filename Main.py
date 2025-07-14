import os
import subprocess
from pystyle import Colorate, Colors
import base64 as b6
import json


Interface= r"""

             __    __  _______    ______   __    __  ________  __    __ 
            |  \  /  \|       \  /      \ |  \  /  \|        \|  \  |  
            | $$ /  $$| $$$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$$| $$\ | $$
            | $$/  $$ | $$__| $$| $$__| $$| $$/  $$ | $$__    | $$$\| $$
            | $$  $$  | $$    $$| $$    $$| $$  $$  | $$  \   | $$$$\ $$
            | $$$$$\  | $$$$$$$\| $$$$$$$$| $$$$$\  | $$$$$   | $$\$$ $$
            | $$ \$$\ | $$  | $$| $$  | $$| $$ \$$\ | $$_____ | $$ \$$$$
            | $$  \$$\| $$  | $$| $$  | $$| $$  \$$\| $$     \| $$  \$$$
             \$$   \$$ \$$   \$$ \$$   \$$ \$$   \$$ \$$$$$$$$ \$$   \$$



                ╒═══════════════════╦══════════
                │ │0│ Quit          ║ │5│ reset password
                │ │1│ Ping          ║
                │ │2│ Port Scanner  ║
                │ │3│ Base64 En/De  ║
                │ │4│                
                │                   
                │                   
                                                                                  """
shell="""
        
        ┌──(user@KRAKEN)-[~/Gurt]
        │                      
        └─$> """
dir = os.path.dirname(os.path.abspath(__file__))


def newPass(passwrdJSON):
    new_password = input('Input new password: ')
    Encrypt1 = b6.b64encode(new_password.encode()).decode()
    data = {"password": Encrypt1}
    with open(passwrdJSON, 'w') as f:
        json.dump(data, f)
    print("New password saved!")


passwrdJSON = os.path.join(dir, 'Data', 'passwd.json')


if not os.path.isfile(passwrdJSON):
    print('Password file not found, please set a new password.')
    newPass(passwrdJSON)


with open(passwrdJSON, 'r') as f:
    stored_password = json.load(f)["password"]


CMD = Colorate.Horizontal(Colors.blue_to_purple, shell)
Menu = Colorate.Horizontal(Colors.blue_to_purple, Interface)

password = 'Enter Password: '
passwordColor = Colorate.Horizontal(Colors.blue_to_purple, password)
password = input(passwordColor)
Encrypt1 = b6.b64encode(password.encode()).decode()
decoded1 = b6.b64decode(Encrypt1)


if Encrypt1 == stored_password:
    print("✅ Access Granted.")
    print(Menu)
else:
    print("❌ Access Denied.")
    input('press enter to exit')
    exit()


passwrdJSON = os.path.join(dir, 'Data', 'passwd.json')


while True:
    os.system('cls')
    print(Menu)
    shell = input(CMD)
    if shell.isdigit():
        shell= int(shell)
        if shell == 1:
            subprocess.run([f'python', dir + '//scripts//Ping.py'])
        elif shell == 2:
            subprocess.run([f'python', dir + '//scripts//PortScanner.py'])
        elif shell == 3:
            subprocess.run([f'python', dir + '//scripts//EN.py'])    
        elif shell == 4:
            print("Option 4 not implemented yet.")
            input("Press Enter to return...")
            subprocess.run([f'python', dir + '//scripts//'])
        elif shell == 5:
            newPass(passwrdJSON)
            input("Password reset. Press Enter to continue...")
        
        elif shell == 0:
            break












#00GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGCCCCCCCCLLLLLfffffttt
#00GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGCCCCCCCCCCLLLLLffffftttt1t
#00GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGCCCCCCCCCCCLLLLLLfffffttttt11
#0GGGGGGGGGGGGGGGGGGGGGGGCf1ii@@@LGGGGGGGGGGGGGGGGCCCCCCCCCCCCCLLLLLffffftttttt11
#0GGGGGGGGGGGGGGGGGGGGG@t@:@@;@@:@@@GfCGGGGGGGGGGCCCCCCCCCCCCCLLLLLLffffttttttt11
#0GGGGGGGGGGGGGGGGGGGGC@@,,,:,,,,@@:@@CLGGCLCGGGGCCCCCCCCCCCCCLLLLLfffffttttttttt
#0GGGGGGGGGGGGGGGGGGGGGL@,,,,,,,:::,,@@@1,;@GGGfGCCCCCCCCCCCCCLLLLLfffffttttttttt
#0GGGGCGCCCCCCCGGGGGGGGG00Gt...,@@@@@@@@,,:@@C;fGLGCCGCCCCCCCCCLLLLLfffffffttfftf
#0GGGGGGCCCCCCCCCGGGGGGGGGGG@,,,@@@@@@@@@@@@@@;@;@GGt;LGCCCCCCCCLLLLLLLffffffffff
#0GGGGGCCCCCCCCCCCCGGGGGGGG0@,,@@@@@@@@@@@@@@@,,@Gt,,LGCCCCCCCCCCCLLLLLLLLLLfLffL
#00GGGGCCCCCCCCCCCCGGGGGGGG@@:@@@@@@@@@@@@;:@,,,@@@,1fGCCCCCCCCCCCLLLLLLLLLLLLLfL
#00GGGGCCCCCCCCCCCCCCGGGCLf1;@@@@@@ii@@@@@@@@@@,@@@:fGGCCCCftLCCCLLLLLLLLLLLLLLLL
#00GGGCCCCCCCCCCCCCCCCG@11@11@@@@@@@@@@@@@@@@@,...,.@GCCLi,:CCCCLLLLLLLLLLLLLLLLL
#0GGGGCCCCCCCCCCCCCCCG@@11@1@1@1@@;@,.,@@@@@@@.,,,@@C:,,..1CCCLLLLLLLLLLLLLLLLLLL
#00GGGCCCCCCCCCCCCCCCG@i1@@@@i@@@@@@@.,@@@@@@@@,@.@@:,,,,@CCCLLLLLLLLLLLLLLLLLLLL
#0GGGCCCCCCCCCCCCCCCCf@@,@@,:@,@@@@@@@.@@@@@@@@..,,,@@:,,;fCCLLLLLLLLLLLfffLLLLLL
#00GGCCftfCCCCCCCCCCf:,.,@,,,::,@@,:@@@@@@@@@@@,.,..,,,,:fLCCLLLLLLLLLLLfffLLLLLL
#00GGCCGf;,,;itttt1@:...,..,,,,:,...,::::,,,,,@@......,@CCCCftLLLLLLLLLLLfLLLLLLL
#00GGCC@i:...,,,,,,,....,,@@@@@@,.,,..........,....,,.@@@Li.;CLLLLLLLLLLLffLLLLLL
#0GGGCCC@1@11tti;i::,,:1CL@@@@i@@@,........,:@@;,...,::.....CCLLLLLLLfffLffffLLLL
#0GGCCCCLLLLLLLLLLLLLLLLC@@@@@@@.@,,,,,..,,,::;:::...,...,.@LtffLLLLLfffffffffLLL
#0GGCCLLLLLLLLLLLLLLLLLLC@;@:@:@@@@@@,,,@,,:,,@,,,:,,.,..@@@ti;@:;i1ffffffffffffL
#0GCCCLLLLLffffffffffffLL:,@@@@,@@@@@@@,,....,::;@:,.....@@CCLCCLti:,,;tffffffffL
#0GCCLLLffffffffffffffffL@,,:@,,..@@.......,::;;@@@@:..,,,@@:;;@LLLLf;,,:tfffffff
#0GCLLLfffffffttttttffft1;,::@,@.........,,:;;@;@;@@@@...@:..:fLLLLffft,,,1ftttff
#0GCLLLfffffttttttttff@@@@@@,,..........,,:@@@@@@@,,@@@......@LLLLfffff1,,,1ttttf
#0CCLLLfffffffffffff1@@@@@;,,,.,........,:@:i@@@@@@@,,@.....1fLLLfffffff@,.:1tttf
#0CCLLLfffffffffffL@:@@@@,,:@,,,,........,,:@@@@@@:@..,...,,i@fLLLffffff@..,:ttff
#GCCLLLLfffffffffL@@@,,.,,,.....,........,,,@:@:::,:,,@.:@,,;@LL1@Lfffff@,,.:ifff
#GCCLLLLffffffffLt,:,,..,.................,,.,......,@@@,.,@@,@. tfftf@@,,.,:;fff
#0CCLLLLLfffffffLt..,.......... .:,.................,,,,,,..,..,@@@@.@.,,,,,:;fff
#GCCLLLLfffffffffL@......... .ttfCL,...................,,@,,.,.,,.,.,.:..,:;,tfff
#GCCLLLLfffffffffff......... ,CLLLLL:...................,,.,,.,,,,,,,.,,:::,;ftff
#GCCLLLLffffffffffL;........ :LLLLLLLi..............................,,,,...;ttttt
#GCLffftfffffffffffL:...... ,LLLLLLfLLf;.................................:1tttttf
#@1;;;;;:,::;1i111tt@,..... @tt1tfLffLfLL1i............,@@........   .:@i;iii;:it
#@@1@;@:@:;@@@@,,...........;ti@:@@::@@111i@,.. ,::,,,,,@@,.........,,,,,,,,,,,,,
#@@@:,@@@i@@i@@i@:,@@@@@::,,:@@@;;::;@:,@,:,,,,,@..,,@@,.,@@,:::::::::::::::::;@:
#;@@@@@i@i1@;;@@@@:@@@@::;;;;;;;;::::::;::i;@;;;;;;;;@t1i;::::::;::::::::::::::::
#i@@@@@@@@@@@:@@@:i@@@@@@@@@i;i;@iiiii;@::::@@@::i;;;@;i;::;;::::@@::::,,:,,,,,,