#
# Copy the file code.py, settings.toml, lib/ and modules/ onto the RPi-pico board that is running circuitPython
#
# In VSCode Use as:
# Ctrl+Shift+P to open command palette
# circuitpython.openSerialMonitor
# choose the board that is connected
# CTRL-D to reload terminal
#

import os
import time
import microcontroller
import modules.get_water_quality as water_quality
import modules.set_servo as set_servo

data_url = "https://www.securetransaction.uk/sas/map/map-code.php"
beachName = os.getenv('BEACH_NAME')

# DEVELOPMENT / DEBUGGING SETTINGS OVERRIDE
# data_url = "https://www.adafruit.com/api/quotes.php"
# beachName = "Benllech"

while True:
    try:
        # SET SERVO TO "WORKING"
        set_servo.set("WORKING")
        #  FETCH NEW DATA
        can_swim = water_quality.return_water_quality(data_url, beachName)
        # print(can_swim["new_beach_rating"])
        if can_swim["new_beach_rating"] == 1:
            # SET SERVO TO "SWIM"
            set_servo.set("YES")
        else:
            # SET SERVO TO "SEWAGE"
            set_servo.set("NO")
        # delays for 300 seconds @TODO - delay for remiander of hour
        time.sleep(300)
    except Exception as e:
        # SET SERVO TO "ERROR"
        set_servo.set("ERROR")
        print("Error:\n", str(e))
        print("Resetting microcontroller in 3600 seconds // 1 hour")
        time.sleep(3600)
        microcontroller.reset()
