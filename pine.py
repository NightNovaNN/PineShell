import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# -----------------------------
# COMMAND MAP (PineShell words -> real commands)
# -----------------------------
CMD_MAP = {
    "ls": "dir",
    "mk file": "type nul >",
    "rm": "del",
    "clr": "cls",
    "sys info": "systeminfo",
}

# -----------------------------
# THEMES
# -----------------------------
THEMES = {
    "pine": {
        "bg": "black",
        "fg": "lightgreen",
        "input_bg": "black",
        "input_fg": "white",
    },
    "neon": {
        "bg": "#001b29",
        "fg": "#00fff7",
        "input_bg": "#002a3d",
        "input_fg": "#00fff7",
    },
    "amber": {
        "bg": "#2b1900",
        "fg": "#ffb000",
        "input_bg": "#3a2400",
        "input_fg": "#ffb000",
    }
}

# -----------------------------
# ENV VAR STORAGE
# -----------------------------
ENV = {}

# -----------------------------
# COMMAND TRANSLATOR
# -----------------------------
def translate_cmd(cmd):
    tokens = cmd.split()

    # ENV var replacement
    if tokens and tokens[0] in ENV:
        tokens[0] = ENV[tokens[0]]
        cmd = " ".join(tokens)

    # Pine command mapping
    for pine_cmd in CMD_MAP:
        if cmd.startswith(pine_cmd):
            mapped = CMD_MAP[pine_cmd]
            rest = cmd[len(pine_cmd):].strip()
            return f"{mapped} {rest}".strip()

    return cmd

# -----------------------------
# RUN SYSTEM COMMAND
# -----------------------------
def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        out = result.stdout.strip()
        err = result.stderr.strip()

        final = ""

        if out != "":
            final += out
        if err != "":
            final += ("\n" + err)

        return final.strip()

    except Exception as e:
        return f"[error] {e}"


# -----------------------------
# MAIN GUI CLASS
# -----------------------------
class PineShellGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PineShell 🌲")
        self.resize(1000, 650)

        layout = QVBoxLayout()

        # Output box
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Consolas", 12))
        layout.addWidget(self.output, stretch=1)

        # Input box
        self.entry = QLineEdit()
        self.entry.setFont(QFont("Consolas", 12))
        self.entry.returnPressed.connect(self.handle)
        layout.addWidget(self.entry)

        self.setLayout(layout)

        self.apply_theme("pine")

    # -------------------------
    # Apply selected theme
    # -------------------------
    def apply_theme(self, theme_name):
        theme = THEMES.get(theme_name, THEMES["pine"])

        self.output.setStyleSheet(
            f"background:{theme['bg']}; color:{theme['fg']};"
        )
        self.entry.setStyleSheet(
            f"background:{theme['input_bg']}; color:{theme['input_fg']};"
        )

        self.output.append(f"[theme switched → {theme_name}]")
        self.output.append("")

    # -------------------------
    # Handle user input
    # -------------------------
    def handle(self):
        cmd = self.entry.text().strip()
        self.entry.clear()

        if cmd == "":
            return

        self.output.append(f">> {cmd}")

        # Built-in: theme change
        if cmd.startswith("pine theme"):
            theme = cmd.split("theme", 1)[1].strip()
            self.apply_theme(theme)
            return

        # Built-in: set env var
        if cmd.startswith("pine set"):
            try:
                rest = cmd[len("pine set"):].strip()
                name, value = rest.split(":", 1)
                name = name.strip()
                value = value.strip().strip('"')
                ENV[name] = value
                self.output.append(f"[env] {name} = {value}")
            except:
                self.output.append("[error] invalid format. Use: pine set var: \"value\"")
            self.output.append("")
            return

        # Translate command
        translated = translate_cmd(cmd)

        if translated != cmd:
            self.output.append(f"[run] {translated}")

        # Run command
        result = run_cmd(translated)

        if result == "":
            self.output.append("[no output]")
        else:
            self.output.append(result)

        self.output.append("")  # spacing


# -----------------------------
# RUN APP
# -----------------------------
app = QApplication([])
window = PineShellGUI()
window.show()
app.exec_()
