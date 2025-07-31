import subprocess
import re
from colorama import Fore, Style, init

# Automatically reset colors after each print
init(autoreset=True)

def print_banner():
    print(Fore.MAGENTA + Style.BRIGHT + "\n╔═══════════════════════════════════════╗")
    print("║       Linux Port Ghosting Detector   ║")
    print("╚═══════════════════════════════════════╝\n")

def scan_open_ports():
    print(Fore.CYAN + "[+] Scanning localhost using nmap...\n")
    try:
        result = subprocess.run(
            ["nmap", "-p-", "127.0.0.1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(Fore.YELLOW + "[!] Error running nmap:", result.stderr)
            return []

        open_ports = []
        for line in result.stdout.splitlines():
            match = re.match(r"^(\d+)/tcp\s+open", line)
            if match:
                open_ports.append(int(match.group(1)))

        print(Fore.GREEN + f"[✓] Open ports found by nmap: {open_ports}\n")
        return open_ports

    except FileNotFoundError:
        print(Fore.RED + "[!] nmap is not installed. Install it with: sudo apt install nmap")
        return []


def get_listening_ports():
    print(Fore.CYAN + "[+] Getting actual listening ports using ss...\n")
    try:
        result = subprocess.run(
            ["ss", "-tln"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(Fore.YELLOW + "[!] Error running ss:", result.stderr)
            return []

        listening_ports = []
        for line in result.stdout.splitlines()[1:]:
            parts = line.split()
            if len(parts) >= 5:
                address_port = parts[4]
                if ':' in address_port:
                    port = address_port.split(':')[-1]
                    if port.isdigit():
                        listening_ports.append(int(port))

        print(Fore.GREEN + f"[✓] Listening ports found by ss: {listening_ports}\n")
        return listening_ports

    except FileNotFoundError:
        print(Fore.RED + "[!] ss command not found. Install it with: sudo apt install iproute2")
        return []


if __name__ == "__main__":
    print_banner()

    open_ports = scan_open_ports()
    listening_ports = get_listening_ports()

    ghosted_ports = [port for port in open_ports if port not in listening_ports]

    if ghosted_ports:
        print(Fore.RED + Style.BRIGHT + "\n⚠️  Ghosted Ports Detected:")
        for port in ghosted_ports:
            print(Fore.RED + f"    ⚠ Port {port} appears open but has no listening service.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "\n✅ No ghosted ports found. Your system looks good!")

    print("\n" + Fore.MAGENTA + "🛡️  Scan complete.")
