import os
import subprocess
from pystyle import Colorate, Colors

Interface="""

             __    __  _______    ______   __    __  ________  __    __ 
            |  \  /  \|       \  /      \ |  \  /  \|        \|  \  |  \\
            | $$ /  $$| $$$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$$| $$\ | $$
            | $$/  $$ | $$__| $$| $$__| $$| $$/  $$ | $$__    | $$$\| $$
            | $$  $$  | $$    $$| $$    $$| $$  $$  | $$  \   | $$$$\ $$
            | $$$$$\  | $$$$$$$\| $$$$$$$$| $$$$$\  | $$$$$   | $$\$$ $$
            | $$ \$$\ | $$  | $$| $$  | $$| $$ \$$\ | $$_____ | $$ \$$$$
            | $$  \$$\| $$  | $$| $$  | $$| $$  \$$\| $$     \| $$  \$$$
             \$$   \$$ \$$   \$$ \$$   \$$ \$$   \$$ \$$$$$$$$ \$$   \$$

             
                 RECON                
                ╒═══════════════════╦══════════
                │                   ║
                │ │1│ Ping          ║
                │ │2│ Port Scanner  ║
                │ │3│               ║
                │ │4│                
                │                   
                │                   
                                                                                  """
shell="""
        
        ┌──(user@KRAKEN)-[~/Gurt]
        │                      
        └─$> """

CMD = Colorate.Horizontal(Colors.blue_to_purple, shell)
Menu = Colorate.Horizontal(Colors.blue_to_purple, Interface)
print(Menu)
dir = os.path.dirname(os.path.abspath(__file__))
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
            subprocess.run([f'python', dir + '//scripts//'])    
        elif shell == 4:
            subprocess.run([f'python', dir + '//scripts//'])    














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
