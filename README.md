# 🌲 PineShell

PineShell is a lightweight, customizable, theme-enabled terminal emulator built using **Python + PyQt5**.  
It acts as a wrapper around the system shell, allowing you to define your own commands, environment variables, and visual themes.

PineShell is designed to be simple, hackable, and easy to extend.

---

## ✨ Features

### 🔹 Custom Command Mapping  
Define PineShell commands that translate into real system commands.  
Example:
- `ls` → `dir`  
- `mk file name.txt` → `type nul > name.txt`

### 🔹 Environment Variables  
You can assign your own "shortcuts" to executables:

```

pine set gcc: "C:/mingw/bin/gcc.exe"
gcc test.c -o test.exe

```

### 🔹 Themes  
Switch between built-in themes instantly:

```

pine theme neon
pine theme amber
pine theme pine

````

### 🔹 Full Output Printing  
PineShell prints:
- stdout  
- stderr  
- translated command preview  
- built-in messages  

### 🔹 Resizable UI  
The interface dynamically scales with the window.

---

## 📦 Requirements

Make sure you have:

- Python 3.8+
- PyQt5 installed

```bash
  pip install PyQt5
```

---

## ▶️ Running PineShell

Run the script:

```bash
python PineShell.py
```

A GUI window will open with an input bar and a scrolling terminal output region.

---

## 🧩 Built-in Commands

### Theme switching

```
pine theme <name>
```

Available themes:

* `pine`
* `neon`
* `amber`

### Environment variables

```
pine set <name>: "<path>"
```

### Custom mapped commands

* `ls` → `dir`
* `mk file` → `type nul >`
* `rm` → `del`
* `clr` → `cls`
* `sys info` → `systeminfo`

---

## 🛠 How It Works

PineShell uses:

* `CMD_MAP` → maps PineShell keywords to real commands
* `ENV` → stores environment variable shortcuts
* `translate_cmd()` → rewrites user input into a real shell command
* `subprocess.run()` → executes commands
* PyQt5 UI components for the display and input system

---

## 📁 File Structure

```
PineShell.py
README.md
```

(You can expand later with plugins, themes folder, history, etc.)

---

## 🚀 Future Improvements

* Command history (`↑` and `↓`)
* Autocomplete
* Multiple tabs
* Plugin system
* Syntax highlighting
* Integrated file explorer
* Async execution for long-running commands

---

## 📜 License

MIT License 

---




