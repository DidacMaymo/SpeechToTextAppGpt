from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="speechToText",
    version="1.0",
    description="With use of GPT3 for ARCHERS episodes",
    executables=executables
)
