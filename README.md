# Description

This is an application that enables the mouse to automatically click on screen whenever it sees pixels matching any images in a folder, it can also automate the mouse and keyboard.

# Build

To build (single .exe with setting.json to control it):
`pyinstaller --onefile ./main.py`

then move `settings.json` file and `imgs` folder to dist

# To use
To use the application simply edit the settings.json to do what you want (e.g. click on specific pictures and/or automate mouse keyboard with specific macros).
Next, either double click the .exe file if it's already built and there or run `python main.py`
