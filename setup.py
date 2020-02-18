import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("script.py")
]
setup(
    name = "Funcoes_Economicas",
    version = "1.0",
    description = "O programa executa funcoes simples de economia",
    executables = executables
 )
