# ⚡ Python Script Runner 🐍

> A terminal-based tool to **run any Python script** — either from your local machine or directly from a GitHub repository!  
> Designed to be simple, smart, and ✨ interactive.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green)
[![Author](https://img.shields.io/badge/Made%20by-Avro-9cf?logo=github)](https://github.com/AvroHere)

---

## 🧩 Features

- 📂 Select and run any **local Python file**
- 🌐 Clone a **GitHub repo** and auto-run `main.py`
- 🧪 Automatically detect `requirements.txt` and check packages
- ✅ Optional one-by-one package install if anything is missing
- 🖥️ Opens scripts in a **new terminal window**
- 🧼 Cleans and resets repos if already cloned
- 🔧 Simple menu system with clear prompts

---

## 🖼️ Demo Screenshot / GIF

> *(Insert your demo screenshot or gif below 👇)*

![Demo](https://user-images.githubusercontent.com/your-screenshot.gif)

---

## 💾 Installation

Clone the repo and run it:

```bash
git clone https://github.com/AvroHere/python-script-runner.git
cd python-script-runner
python main.py
```

---

## 🧠 How to Use

### 🏠 Offline Mode (Run Local Script)

```bash
1️⃣ Choose option 1 from the menu
📁 Select any `.py` file on your system
🚀 It runs in a new terminal window
```

### 🌍 Online Mode (Run from GitHub)

```bash
2️⃣ Choose option 2 from the menu
🔗 Paste a GitHub repo URL
🧾 It shows all files — auto-runs `main.py` if available
```

> 🧙 It also checks and installs missing dependencies if `requirements.txt` exists!

---

## 📁 Folder Structure

```
📦 python-script-runner/
 ┣ 📜 main.py
 ┣ 📄 README.md
 ┗ 📃 requirements.txt
```

---

## 🛠 Built With

- 🐍 Python 3.x
- 📦 `os`, `sys`, `subprocess`
- 🧰 `tkinter` for file dialog
- 🔗 `git` CLI for repo cloning
- 🧪 `pkg_resources` for dependency checks

---

## 🚧 Roadmap

- 🖼️ Add GUI-based version
- 💬 Multi-script launcher with preview
- 📦 ZIP-based GitHub fallback
- 🪄 One-click batch install for requirements

---

## ❓ FAQ

**Q: What if `requirements.txt` is missing in the repo?**  
🅰️ No worries! The tool will still run and skip the package check.

**Q: Can I use this on Linux/macOS?**  
🅰️ Yup! It automatically detects your OS and uses the right terminal commands.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — free for personal and commercial use 🎉

---

## 👨‍💻 Author

**Avro** — Python developer & automation enthusiast  
🔗 [GitHub Profile](https://github.com/AvroHere)

> 🧠 _"Make tools for your future self."_  
Feel free to ⭐ star the repo or fork for your own use!

---
