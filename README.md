# RokuTV-Night-Day

This project was designed for people with Roku TVs who use their device as a night light while they sleep. Usually, you would have to flip through several menus on the TV to reduce the brightness before bed, and then repeat the process once again in the morning to increase the brightness. This project simplifies that process by taking advantage of the [Roku External Control Protocol](https://developer.roku.com/docs/developer-program/debugging/external-control-api.md).


## Usage

```python
from RokuTV import RokuClient

tv = RokuClient("192.168.1.56")

# sends a user specified sequence of commands to the TV
# perhaps to reduce brightness and to mute
tv.night_mode()
...
# sometime later, activate day mode
tv.day_mode()

```
The "commands.txt" file is where night mode and day mode retrieve the list of key presses to send to the TV. Instructions and an example setup are provided within the file, but here is a preview: 

>#Day Mode commands
Info,Down,Left,Down,Down,Right,Right,Info,VolumeMute

>#Night Mode commands
Info,Down,Right,Down,Down,Left,Left,Info,VolumeMute



## Disclaimer

This code is fully functional, however, it was developed for learning purposes and may not offer the full functionality or error handling as may be seen in other software.
