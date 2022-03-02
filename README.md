# EZ Presence
EZ Presence is a GUI-Python app which makes it easy to set any custom Discord Rich Presence.

# Using the App
### How to Run
Since the app is in it's BETA stage, many features are changing very fast and the code will be kinda raw. It is recommended to run in terminal or command prompt as any runtime errors will appear there.

### Steps to Run
If you are on Windows, you can just download the source code and run with Python. If you are on a GNU/Linux machine, it is recommended to use `git clone` to download the files. On a GNU system, run these commands in terminal.
```shell
cd /path/to/folder
```
```shell
git clone https://github.com/notsniped/ez-presence/
```
After downloading the repository, locate `app.py` path and run this in terminal.
```shell
python /path/to/file
```
The GUI should load and you can now set your own rich presence!

# Requirements/Dependencies
Run `pip install -r requirements.txt` for quick install.
> Python 3 or higher,
> Pypresence (pip install pypresence),
> TKinter (sudo pacman -S tk) or (sudo apt-get tk) on GNU/Linux

# Troubleshooting
### "Failed to initalize GUI" error
![](https://github.com/notsniped/ez-presence/blob/main/assets/Screenshot_20220301_110912.png)

This error may occur in GNU/Linux systems. To fix this issue, try installing `tk` for your specific distro. Information for Debian/Ubuntu and Arch Linux are already provided in the message. If that does not solve the problem, try installing tk using pip:
```shell
pip install tk
```
Now the app should run without issues.

### "Python: command not found" error
This most likely means that you do not have python installed in your system. This can apply to both Windows and GNU/Linux, but it is less common in GNU. If you see this error when trying to run, download the latest version of python from [here](https://www.python.org/downloads/).

# Known Issues
`Party size` and `Max party size` don't do anything and will most likely be removed in a later version.
