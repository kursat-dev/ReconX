<div align="center">

# 🕵️ ReconX

**Automated Web Reconnaissance Tool for Penetration Testers**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/CLI-Rich-purple.svg)](https://pypi.org/project/rich/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Modules](#-modules) • [Disclaimer](#-disclaimer)

</div>

---

## 📖 Overview

**ReconX** is a modular, automated reconnaissance tool designed to kickstart your pentesting workflow. It gathers essential information about a target domain, including subdomains, open ports, and the underlying technology stack, all wrapped in a beautiful CLI interface.

It leverages passive sources like Certificate Transparency logs for stealthy subdomain enumeration and performs active checks for port scanning and tech detection.

## ✨ Features

- 🔍 **Subdomain Enumeration**: Rapidly find subdomains using Certificate Transparency logs (crt.sh).
- 📡 **Port Scanning**: Check for common open ports (80, 443, 8080, 22, etc.).
- 🛠️ **Tech Stack Detection**: Analyze HTTP headers to identify server software and frameworks.
- 📄 **JSON Reporting**: Automatically generate detailed JSON reports for your tools.
- 🎨 **Beautiful CLI**: Polished output using the `rich` library.

## 🛠 Tech Stack

- **Language**: Python 3
- **Libraries**: 
  - `requests` (API & HTTP interaction)
  - `rich` (Terminal, formatting)
  - `socket` (Port scanning)

## 📦 Installation

To get ReconX up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or higher
- pip

### 1. Clone the Repo

```bash
git clone https://github.com/kursat-dev/ReconX.git
cd reconx
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the tool against your target domain.

```bash
python reconx.py example.com
```

### Options

- `domain`: The target domain (required).
- `-o`, `--output`: Specify the output JSON file path (default: `report.json`).

Example with custom output:
```bash
python reconx.py google.com -o results.json
```

## 🧩 Modules

| Module | Description |
|--------|-------------|
| **Subdomains** | Queries `crt.sh` to find subdomains without direct interaction (Passive). |
| **Ports** | Connects to top TCP ports to determine accessibility (Active). |
| **Tech** | inspects HTTP response headers (`Server`, `X-Powered-By`, Cookies) to fingerprint the stack. |


## ⚠️ Disclaimer

> [!CAUTION]
> **USE RESPONSIBLY.**
> 
> - **ReconX** is intended for educational purposes and authorized penetration testing only.
> - **DO NOT** use this tool on systems you do not own or have explicit permission to test.
> - The author is not responsible for any illegal use or damage caused by this tool.

## 📝 License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
