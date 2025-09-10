<!-- AZCompiler README -->

<div align="center">

# 🔐 **AZCompiler**  
### 💻 Secure Python Code Obfuscator & Interactive Runner  

_A Python code protection system with advanced encryption, a hacking-themed console interface, and interactive execution._

![Version](https://img.shields.io/badge/Version-1.8.0-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.7%2B-green.svg)  
![License](https://img.shields.io/badge/License-MIT-orange.svg)  

</div>

---

## 🌟 **Overview**

> **AZCompiler** is a **powerful Python-based encryption and execution tool**.  
> It converts your standard `.py` scripts into **encrypted `.az` files** to prevent direct reading or tampering.  
> With its **modern, hacker-style console** and **interactive shell**, AZCompiler is ideal for developers who need **lightweight code protection** or a stylish way to manage script execution.  

---

## ✨ **Key Features**

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🔒 **Secure Encryption**| XOR-based cipher with PBKDF2-HMAC-SHA256 key derivation for password-based encryption |
| 🎨 **Professional UI**  | Custom AZTheme console output with ANSI colors for a hacking-style experience |
| ⚡ **Interactive Mode** | Real-time command processing with auto-complete-like behavior                |
| 🚀 **Dual Operation**   | Supports both **CLI arguments** and **interactive shell**                    |
| 📁 **Format Conversion**| Seamless `.py` → `.az` compilation and execution                             |
| 🔧 **Extensible Design**| Modular architecture for adding future encryption methods or UI improvements  |

---

## 📸 **Screenshots (Concept)**

```
┌─────────────────────────────────────────┐
│       AZCompiler Interactive Shell      │
├─────────────────────────────────────────┤
│     ╔═╗╔═╗╔╦╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗            |
│     ╠═╝╠═╣║║║║║║║ ║╚═╗ ║ ╚═╗            |
│     ╩  ╩ ╩╩ ╩╩ ╩╚═╝╚═╝ ╩ ╚═╝            |
│   Advanced Console Interface v1.0       |
│   Warning: Authorized Access Only       |
│                                         |
│  [Interactive Mode] Type 'compile ...   |
│  [Exit] Type 'exit' to quit             |
│  [INPUT] AZCompiler>                    │
└─────────────────────────────────────────┘
```

---

## 🏁 **Quick Start**

### 📥 **Installation**
```bash
git clone https://github.com/yourusername/AZCompiler.git
cd AZCompiler
```

### ▶ **Basic Usage**

#### 🔧 **Compile a Python file**
```bash
python az_compiler.py compile your_script.py yourpassword
```

#### ▶ **Run an encrypted file**
```bash
python az_compiler.py run your_script.az yourpassword
```

#### 💻 **Interactive Mode**
```bash
python az_compiler.py
```
```
AZCompiler> compile example.py mypassword  
AZCompiler> run example.az mypassword  
AZCompiler> exit
```

---

## 📂 **Project Structure**
```text
AZCompiler/
├── AZtheme.py          # Custom console theme and output formatting
├── az_compiler.py      # Main compiler and runner application
├── test_script.py      # Example script for testing
└── README.md           # This document
```

---

## 📋 **Requirements**
- 🐍 **Python 3.7+**  
- 📦 **Standard library only** – no external dependencies required  

---

## 🔧 **How It Works**

### 🗜 **Compilation**
1. Reads your Python source code  
2. Derives an encryption key from your password using **PBKDF2-HMAC-SHA256**  
3. Encrypts the content using an **XOR cipher**  
4. Encodes the encrypted data with **Base64**  
5. Outputs an encrypted `.az` file  

### ▶ **Execution**
1. Reads the `.az` file  
2. Decodes the Base64 content  
3. Regenerates the encryption key from your password  
4. Decrypts the data using the XOR cipher  
5. Executes the decrypted code within the AZCompiler environment  

---

## ⚠️ **Important Notes**
> ❗ **Not Military-Grade Encryption** – AZCompiler offers **basic obfuscation** for casual protection.  
> 🔑 **Password Recovery Is Impossible** – Always keep backups and remember your passwords.  
> ✅ **For Legitimate Use Only** – Do not use for malicious purposes.  
> 🧪 **Test Thoroughly** – Complex scripts may need modifications before encryption.  

---

## 📄 **License**
Licensed under the **MIT License** – Use, modify, and distribute responsibly.  

---

## 🤝 **Contributing**
Contributions are welcome!  
- 🛠 Submit pull requests for new encryption methods, UI improvements, or performance optimizations.  
- 🌱 Ensure all contributions align with **ethical and legal practices**.  

---

<div align="center">
✨ _Made with ❤️ to protect your Python projects and elevate your console experience._ ✨  
</div>
