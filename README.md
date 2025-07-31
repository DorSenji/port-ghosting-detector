
# Port Ghosting Detector (Linux)

> A simple Python tool to detect *ghosted* ports — ports that appear open to scanners like `nmap` but have no service actually listening.

---

## What Is Port Ghosting?

**Port ghosting** occurs when a port appears open to external scans (due to firewall/NAT misconfigurations) but no actual application is listening on that port. This can be a sign of:

- Misconfigured firewall rules
- Security vulnerabilities
- Unexpected network behavior

This tool helps detect such ports on your **local Linux machine**.

---

## Features

- Scans all TCP ports using `nmap`
- Lists actual listening ports with `ss`
- Compares both lists and reports ghosted ports

---

## ⚙️ Requirements

- Python 3.6+
- `nmap` (for scanning)
- `ss` (comes with `iproute2`)
- `colorama` (for terminal colors)

Install dependencies:
```bash
pip install -r requirements.txt
```

Install system tools if needed:
```bash
sudo apt install nmap iproute2
```

---

## Usage

Run the script:

```bash
python3 ghost_detect.py
```

Example output:

```
[+] Scanning localhost using nmap...
[✓] Open ports found by nmap: [22, 8080]
[+] Getting actual listening ports using ss...
[✓] Listening ports found by ss: [22]

⚠️  Ghosted Ports Detected:
    ⚠ Port 8080 appears open but has no listening service.

🛡️  Scan complete.
```
Here is a brief test I did where I purposely opened the port 12345:

<img width="588" height="353" alt="image" src="https://github.com/user-attachments/assets/f243d8a3-5440-43e7-a7a2-fb3e867f2ca8" />

---

## Why I Made This

This is a small project I built to:
- Learn more about Linux networking and sockets
- Practice Python and system scripting
- Share something useful and security-related
- I was bored on a random thursday evening

---

## Project Structure

```
port-ghosting-detector/
├── ghost_detect.py         # Main script to run
├── requirements.txt        # Python dependency for colorama if needed
└── README.md               # Description of everything
```

---

## Contributing

Pull requests welcome if you want to improve the tool or add features like:
- JSON report output
- Remote IP scanning
- Cron job integration

---

## License

MIT License. Free for personal and professional use.

---
