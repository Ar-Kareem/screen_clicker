# Description

This is an application that enables the mouse to automatically click on screen whenever it sees pixels matching any images in a folder, it can also automate the mouse and keyboard.

# Build

To build:

1- `pyinstaller --icon=clocks.ico --onefile ./main.py`
This will make a single .exe file in folder `dist` which will be about `~300 MB`

2- move `settings.json` and `imgs` folder into `./dist/`. 
Now everything is done. Running the `.exe` will read from the `settings.json` file and execute from it.

# To use
To use the application, download the latest release, unzip it, and edit the settings.json to do what you want (e.g. click on specific pictures and/or automate mouse keyboard with specific macros).
Next, either double click the .exe file.
