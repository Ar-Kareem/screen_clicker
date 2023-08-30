This is an application that enables the mouse to automatically click on screen whenever it sees pixels matching any images in a folder, it can also automate the mouse and keyboard.
To use simply edit the settings.json in the "exe" folder to do what you want (e.g. click on specific pictures and/or automate mouse keyboard with specific macros) then simply double click the .exe file and that's it.

To build (single .exe with setting.json to control it):
pyinstaller --onefile ./main.py

then move "settings.json" file and "imgs" folder to dist