# swim-stay-clock (circuitpython)

### About
This is the electronics/code setup for a Raspberry Pi Pico (running circuitPython) to do the following:
1. Connect to local WiFi
1. Set the correct board time
1. Fetch a static website
1. Parse the website for specific data (using regex)
1. Set a servo position based on the data (Yes/No/Help)
1. Sleep for the remainder of the hour

## References

This is a project using circuitPython - info here: https://circuitpython.org/

It also uses Adafruit circuitPython bundle - info here: https://circuitpython.org/libraries

## Setup
To get the clock working it needs to know the wifi name and password, and the beach name it's checking water quality for, all this comes from a file named `settings.toml`, and it should look like this:

```
CLOCK_WIFI_SSID = "my_WiFi_name"
CLOCK_WIFI_PASSWORD = "my_secret_password"
CLOCK_BEACH_NAME = "Gyllingvase"
```

## Deployment

### Raspberry Pi Pico
To update the Raspberry Pi Pico, mount it as a USB drive, then copy the files `code.py` and `settings.toml` (with correct WiFi settings).
Also copy over the whole `modules` and `lib` folders.

### Use with VS Code
1. Install the CircuitPython extension:
1. use `Shift + Command + P (Mac) / Ctrl + Shift + P (Windows/Linux)` to open the command palette.
1. run circuitpython.openSerialMonitor from the command palette
1. in the open terminal window, choose the board that is connected
1. CTRL-D to reload terminal

 
