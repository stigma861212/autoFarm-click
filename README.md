# autoFarm-click

Automatically launch selected Steam games, initiate them upon opening, and enable multi-game setup to complete in one go.

## Install
```
pip install pyautogui
```
```
pip install psutil
```

## Config

Using config.example.json

You can set up multiple games. (see `config.example.json` content)

- **exe**: GameName (Without file extensions).

- **path**: Your file location (absolute path) needs double backslashes. You can also use the desktop shortcut created by Steam. If the game cannot be launched by directly executing the exe file and you do not want to create a shortcut, you can open it by entering steam://rungameid/gameid in the path, where gameid is the game's App ID, which can be found at [steamdb](<https://steamdb.info/>).

- **clicks**: Click count.

When configuration is complete, rename the file from `config.example.json` to `config.json`.

## Start

open `start.bat`, then wait until end.