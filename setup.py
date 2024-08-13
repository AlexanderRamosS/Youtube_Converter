import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os","re","sys"], "includes": ["PyQt5", "yt_dlp"]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Youtube_to_mp3",
    version = "0.1",
    description = "Baixa videos do youtube e os converte em mp3 ou mp4",
    options = {"build_exe": build_exe_options},
    executables  = [Executable("main.py", base=base)]
)