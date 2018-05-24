from cx_Freeze import setup, Executable

base = None

executables = [Executable("chatbot.py", base=base)]
packages = ["copy","glob","random","os","aiml","re","string","sys","time","threading","xml.sax"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "ChatBot",
    options = options,
    version = "1.0",
    description = 'First Chat bot',
    executables = executables
)