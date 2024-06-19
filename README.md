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

- **path**: Your file location (absolute path) needs double backslashes. You can also use the desktop shortcut created by Steam.

- **clicks**: Click count.

When configuration is complete, rename the file from `config.example.json` to `config.json`.

## Start

open `start.bat`, then wait until end.