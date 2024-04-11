#
# Copy the file code.py onto the RPi-pico board that is running circuitPython
#
# In VSCode Use as:
# Ctrl+Shift+P to open Terminal
# circuitpython.openSerialMonitor
# Choose Board That is connected
# Press CTRL-D to reload teminal
#
# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# import time
# import microcontroller
import os
import ssl
import wifi
import socketpool
import adafruit_requests
import re

# from adafruit_motor import servo
# import modules.my_module as my_module

# #  adafruit quotes URL
# quotes_url = "https://www.adafruit.com/api/quotes.php"
# # quotes_url = "https://www.securetransaction.uk/sas/map/map-code.php"

# # WORKING
# # quotes_url = "https://zuaxlhjssfsjj2bcz74ubsokuq0yracq.lambda-url.eu-west-2.on.aws/?beachName=Gyllyngvase"
# # RETURNS :: {'description': 'No water quality alerts in place', 'name': 'Gyllyngvase', 'markertype': '1'}

#  connect to SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# while True:
#     try:
#         #  pings URL quotes
#         print("Fetching text from %s" % quotes_url)
#         #  gets the quote from adafruit quotes
#         response = requests.get(quotes_url)
#         # print(response.text)
#         # print(response.json())
#         # print(response.iter_content())
#         text = ""
#         result = ""
#         foundFlag = False
#         for i in response.iter_content(1, False):
#             if foundFlag == False:
#                 # print(i.decode('utf-8'))
#                 thisChar = i.decode('utf-8')
#                 text = text + thisChar

#                 if '\n' in text:
#                     if keyword in text:
#                         if beachName in text:
#                             # UNCOMMENT NEXT LINE IF YOU WANT A FASTER PERFORMANCE, WILL BREAK AFTER BEACH IS FOUND
#                             foundFlag = True
#                             result = text

#                         # UNCOMMENT THIS IF YOU WANT A LIST OF ALL AVAILABLE BEACHES (CONSOLE LOG)
#                         # match = re.search(r".*markertype = \'(.*?)\'.*\>(.*?)\';", text)
#                         # newBeachName = match.group(2)
#                         # newBeachRating = match.group(1)
#                         # print(newBeachName, newBeachRating)
#                     text = ""
            
#         print("*" * 40)
#         print("Result")
#         match = re.search(r".*markertype = \'(.*?)\'.*\>(.*?)\';", result)
#         # newBeachName = match.group(2)
#         # newBeachRating = match.group(1)
#         # print(newBeachName, newBeachRating)
#         print("*" * 40)
#         print("-" * 40)
#         response.close()
#         #  delays for 5 minute

#         # HERE - SLEEP FOR THE REST OF THE HOUR
#         time.sleep(300)
#     # pylint: disable=broad-except
#     except Exception as e:
#         print("Error:\n", str(e))
#         print("Resetting microcontroller in 30 seconds")
#         time.sleep(30)
#         microcontroller.reset()


def return_water_quality(quotes_url, beachName):
    return { "beach_name": "test_beach", "new_beach_rating": 1 } # type: ignore
    try:
        #  pings URL quotes
        print("Fetching text from %s" % quotes_url)
        #  gets the quote from adafruit quotes
        response = requests.get(quotes_url)
        # print(response.text)
        # print(response.json())
        # print(response.iter_content())
        text = ""
        result = ""
        foundFlag = False
        for i in response.iter_content(1, False):
            if foundFlag == False:
                # print(i.decode('utf-8'))
                thisChar = i.decode('utf-8')
                text = text + thisChar

                if '\n' in text:
                    if keyword in text:
                        if beachName in text:
                            # UNCOMMENT NEXT LINE IF YOU WANT A FASTER PERFORMANCE, WILL BREAK AFTER BEACH IS FOUND
                            foundFlag = True
                            result = text

                        # UNCOMMENT THIS IF YOU WANT A LIST OF ALL AVAILABLE BEACHES (CONSOLE LOG)
                        # match = re.search(r".*markertype = \'(.*?)\'.*\>(.*?)\';", text)
                        # newBeachName = match.group(2)
                        # newBeachRating = match.group(1)
                        # print(newBeachName, newBeachRating)
                    text = ""
            
        print("*" * 40)
        print("Result")
        match = re.search(r".*markertype = \'(.*?)\'.*\>(.*?)\';", result)
        newBeachName = match.group(2)
        newBeachRating = match.group(1)
        print(newBeachName, newBeachRating)
        print("*" * 40)
        print("-" * 40)
        response.close()
        return { beach_name: newBeachName, new_beach_rating: newBeachRating }
    # pylint: disable=broad-except``
    except Exception as e:
        return { beach_name: "test_beach", new_beach_rating: 1 }
        # print("Error:\n", str(e))
        # print("Resetting microcontroller in 30 seconds")
        # time.sleep(30)
        # microcontroller.reset()