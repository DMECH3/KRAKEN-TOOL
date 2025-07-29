import os
import subprocess
from pystyle import Colorate, Colors
import base64 as b6
import json
from getpass import getpass
import time
import socket
from datetime import datetime


Interface= r"""
__    __  _______    ______   __    __  ________  __    __ 
  \  /  \|       \  /      \ |  \  /  \|        \|  \  |  \
 $$ /  $$| $$$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$$| $$\ | $$
 $$/  $$ | $$__| $$| $$__| $$| $$/  $$ | $$__    | $$$\| $$
 $$  $$  | $$    $$| $$    $$| $$  $$  | $$  \   | $$$$\ $$
 $$$$$\  | $$$$$$$\| $$$$$$$$| $$$$$\  | $$$$$   | $$\$$ $$
 $$ \$$\ | $$  | $$| $$  | $$| $$ \$$\ | $$_____ | $$ \$$$$
 $$  \$$\| $$  | $$| $$  | $$| $$  \$$\| $$     \| $$  \$$$
\$$   \$$ \$$   \$$ \$$   \$$ \$$   \$$ \$$$$$$$$ \$$   \$$


            ╔═══(0) Quit
            ╠════(1) Ping
            ╠═════(2) Port Scanner 
            ╠══════(3) IP Scanner
            ╠═══════(4) File Manager  
            ╠════════(5) PlaceHolder 
            ╠═════════(6) Base64 Encoder/Decoder 
            ╠══════════(7) Creds  
            ╚═══════════(8) Reset Password
                                                                """
shell=f"""
            ┌──(user@KRAKEN)-[~/]
            │                      
            └─$> """
dir = os.path.dirname(os.path.abspath(__file__))
passwrdJSON = os.path.join(dir, 'Data', 'passwd.json')

def newPass(passwrdJSON):
    new_password = getpass(Colorate.Horizontal(Colors.blue_to_purple,'Input new password: '))
    Encrypt1 = b6.b64encode(new_password.encode()).decode()
    data = {"password": Encrypt1}
    with open(passwrdJSON, 'w') as f:
        json.dump(data, f)
    print(Colorate.Horizontal(Colors.blue_to_purple,"New password saved!"))

passwrdJSON = os.path.join(dir, 'Data', 'passwd.json')

if not os.path.isfile(passwrdJSON):
    print(Colorate.Horizontal(Colors.blue_to_purple,'Password file not found, add json file named "passwd.json" to folder "Data" to be able to access the program.'))
    input(Colorate.Horizontal(Colors.blue_to_purple,'Press enter to exit...'))
with open(passwrdJSON, 'r') as f:
    stored_password = json.load(f)["password"]

CMD = Colorate.Horizontal(Colors.blue_to_red, shell)
Menu = Colorate.Horizontal(Colors.blue_to_red, Interface)

password = getpass(Colorate.Horizontal(Colors.blue_to_purple,'Enter Password: '))
Encrypt1 = b6.b64encode(password.encode()).decode()
decoded1 = b6.b64decode(Encrypt1)


if Encrypt1 == stored_password:
    print(Colorate.Horizontal(Colors.blue_to_purple,"✅ Access Granted."))
    print(Menu)
else:
    print(Colorate.Horizontal(Colors.blue_to_purple,"❌ Access Denied."))
    input(Colorate.Horizontal(Colors.blue_to_purple,'press enter to exit'))
    exit()
time.sleep(1)
os.system('cls')
if __name__ == "__main__":
    while True:
        os.system('cls')
        print(Menu)
        shell = input(CMD)
        if shell.isdigit():
            shell= int(shell)
            if shell == 0:
                break
            elif shell == 1:
                ip = " Input the ip -> "
                Ip_Color = Colorate.Horizontal(Colors.blue_to_purple, ip)
                ip = input(Ip_Color)
                subprocess.run(f"ping " + ip)
                input("press enter to complete...")
                #Cyssym
            elif shell == 2:
                def port_scanner(target, start_port=1, end_port=1024):
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"\nStarting scan on {target}"))
                    print(Colorate.Horizontal(Colors.blue_to_purple, f"Scanning ports {start_port} to {end_port}...\n"))
                    start_time = datetime.now()

                    for port in range(start_port, end_port + 1):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.5)
                        try:
                            result = s.connect_ex((target, port))
                            if result == 0:
                                print(f"[+] Port {port} is OPEN")
                            s.close()
                        except KeyboardInterrupt:
                            print("\nScan interrupted by user.")
                            break
                        except socket.gaierror:
                            print("Hostname could not be resolved.")
                            break
                        except socket.error:
                            print("Couldn't connect to server.")
                            break

                    end_time = datetime.now()
                    duration = end_time - start_time
                    print(f"\nScan completed in {duration}")
                if __name__ == "__main__":
                    target = input(Colorate.Horizontal(Colors.blue_to_purple,"Enter target IP or hostname: "))
                    try:
                        start = int(input(Colorate.Horizontal(Colors.blue_to_purple, "Start port [default 1]: ")) or 1)
                        end = int(input(Colorate.Horizontal(Colors.blue_to_purple, "End port [default 1024]: ")) or 1024)
                        port_scanner(target, start, end)
                    except ValueError:
                        print("Invalid port number.")
                input("press enter to exit...")

            elif shell == 3:
                firstNumber = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'Enter first number of range: ')))
                secondNumber = int(input(Colorate.Horizontal(Colors.blue_to_purple, 'Enter second number of range: ')))

                for ip in range(firstNumber, secondNumber + 1):
                    ip_address = f'192.168.1.{ip}'
                    print(Colorate.Horizontal(Colors.blue_to_purple, f'Testing {ip_address}'), end='\r')

                    # Use subprocess to ping
                    result = subprocess.Popen(['ping', '-n', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, _ = result.communicate()
                    if b'TTL=' in output:
                        print(Colorate.Horizontal(Colors.blue_to_purple, f'{ip_address} is UP     '))
                    else:
                        print(Colorate.Horizontal(Colors.blue_to_purple, f'{ip_address} is DOWN   '))

                input(Colorate.Horizontal(Colors.blue_to_purple, 'Press Enter to exit...'))   
            elif shell == 4:
                LocalDirectory = os.getcwd()
                CDrive = os.path.abspath("C:\\")
                
                print(Colorate.Horizontal(Colors.blue_to_purple,'\n     File Management Started'))
                print(Colorate.Horizontal(Colors.blue_to_purple,'\n     Type HELP to Show commands'))
                while True:
                    cmdShell = Colorate.Horizontal(Colors.blue_to_purple,f"""
                ┌──(user@KRAKEN)-[~/{LocalDirectory}]
                │                      
                └─$> """)
                    Directory = ''
                    cmd = input(cmdShell)
                    if cmd == 'help':
                        print(Colorate.Horizontal(Colors.blue_to_purple,'''
                dir: List files/Directories
                cd <dir>: Change Directory
                mkdir <name>: Make new Directory
                rd <dir>: Remove Directory
                del <file>: Delete File
                ren <old> <new>: Rename File
                exit: Exit the program'''))
                    elif cmd == 'exit':
                        break
                    elif cmd == 'dir':
                        for item in os.listdir(LocalDirectory):
                            print(item)

                    elif cmd.startswith('cd '):
                        try:
                            path = cmd[3:].strip()
                            os.chdir(path)
                            Directory = os.getcwd()
                            LocalDirectory = os.path.abspath(Directory)
                        except Exception as e:
                            print(f"Error changing directory: {e}")
                    elif cmd == 'cd ..':
                        try:
                            os.chdir('..')
                            Directory = os.getcwd()
                            LocalDirectory = os.path.abspath(Directory)
                        except Exception as e:
                            print(f"Error changing to parent directory: {e}")
                    elif cmd.startswith('mkdir ') or cmd.startswith('md '):
                        try:
                            folder = cmd.split(' ', 1)[1]
                            os.mkdir(folder)
                        except Exception as e:
                            print(f"Error making directory: {e}")

                    elif cmd.startswith('rd ') or cmd.startswith('rdmir '):
                        try:
                            folder = cmd.split(' ', 1)[1]
                            os.rmdir(folder)
                        except Exception as e:
                            print(f"Error removing directory: {e}")

                    elif cmd.startswith('del '):
                        try:
                            file = cmd.split(' ', 1)[1]
                            os.remove(file)
                        except Exception as e:
                            print(f"Error deleting file: {e}")

                    elif cmd.startswith('ren '):
                        try:
                            _, old, new = cmd.split(' ', 2)
                            os.rename(old, new)
                        except Exception as e:
                            print(f"Error renaming file: {e}")
                    else:
                        print('No command known')
                        input('press enter to exit file management...')

            elif shell == 5:
                print(Colorate.Horizontal(Colors.blue_to_purple,'No program attached!'))
                input(Colorate.Horizontal(Colors.blue_to_purple,'Press enter to exit...'))
            elif shell == 6:
                print(Colorate.Horizontal(Colors.blue_to_purple, 'Encode or decode'))
                decide = input("")
                if decide == "encode":
                    encode = input(Colorate.Horizontal(Colors.blue_to_purple,"Enter the text to encode: "))
                    try:
                        encoded_bytes = b6.b64encode(encode.encode())
                        encoded_str = encoded_bytes.decode()   
                        print(Colorate.Horizontal(Colors.blue_to_purple,f"Encoded: {encoded_str}"))
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.blue_to_purple,f"Error encoding: {e}"))
                    input('press enter to stop...')
                if decide == "decode":
                    decode = input(Colorate.Horizontal(Colors.blue_to_purple,"Enter the base64 to decode: "))
                    try:
                        decoded_bytes = b6.b64decode(decode)
                        decoded_str = decoded_bytes.decode()
                        print(Colorate.Horizontal(Colors.blue_to_purple,f"Decoded: {decoded_str}"))
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.blue_to_purple,f"Error decoding: {e}"))
                    input(Colorate.Horizontal(Colors.blue_to_purple,'press enter to stop...'))
            elif shell == 7:
                print(Colorate.Horizontal(Colors.blue_to_purple,'https://github.com/DMECH3/KRAKEN-TOOL'))
                input(Colorate.Horizontal(Colors.blue_to_purple,'Press enter to exit...'))
            elif shell == 8:
                newPass(passwrdJSON)
                input(Colorate.Horizontal(Colors.blue_to_purple,"Password reset. Press Enter to continue..."))











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
