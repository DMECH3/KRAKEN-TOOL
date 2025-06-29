import socket
from datetime import datetime

def port_scanner(target, start_port=1, end_port=1024):
    print(f"\nStarting scan on {target}")
    print(f"Scanning ports {start_port} to {end_port}...\n")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # short timeout for quick scanning

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
    target_ip = input("Enter target IP or hostname: ")
    try:
        start = int(input("Start port [default 1]: ") or 1)
        end = int(input("End port [default 1024]: ") or 1024)
        port_scanner(target_ip, start, end)
    except ValueError:
        print("Invalid port number.")
input("press enter to exit...")