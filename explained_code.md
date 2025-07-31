# Code Explained – Port Ghosting Detector

This document explains, line by line, how the `ghost_detect.py` script works.

---

## Imports

```python
import subprocess
import re
from colorama import Fore, Style, init
```

- `subprocess`: lets Python run system commands like `nmap` and `ss`.
- `re`: regular expressions (used to find patterns in text).
- `colorama`: lets us print colored text in the terminal.

---

## Initialize Colorama

```python
init(autoreset=True)
```

- Automatically resets colors after each `print()`, so we don’t have to do it manually (trust me, it's way better like this).

---

## print_banner()

```python
def print_banner():
    ...
```

- Prints a colorful ASCII banner when the program starts (just for funsies tbh)

---

## scan_open_ports()

```python
def scan_open_ports():
    ...
```

- Runs `nmap` to scan all TCP ports on your localhost.
- Collects all ports reported as "open".
- Uses regex to find the open ports in `nmap`’s output.

---

## get_listening_ports()

```python
def get_listening_ports():
    ...
```

- Runs `ss -tln` to get a list of ports your computer is *actually* listening on.
- Parses that list and extracts the port numbers.

---

## Compare the Two

```python
ghosted_ports = [port for port in open_ports if port not in listening_ports]
```

- This line compares the two lists.
- If a port is seen by `nmap` but not in `ss`, it's considered “ghosted”.

---

## Final Output

```python
if ghosted_ports:
    ...
else:
    ...
```

- If ghosted ports exist, show a warning with red ⚠️
- If no ghosted ports, show a green success message ✅

---

## Error Handling

The script will also catch and report if:
- `nmap` is not installed to make your troubleshooting easier (you're welcome)
- `ss` is not installed (same here)
- Any unexpected error happens

---

## Example Output

```
[+] Scanning localhost using nmap...
[✓] Open ports found by nmap: [12345]
[✓] Listening ports found by ss: [12345]

✅ No ghosted ports found. Your system looks good!
```

---

## Why This File Exists

I am still learning and I always appreciate any kind of knowledge I receive by other coders.
Wanted to return the favor to the community ;-)
