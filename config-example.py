from sys import platform    
from machine import Pin

try:
    from mqtt_as import config
except Exception:
    config = {}

def ledfunc(pin):
    pin = pin
    def func(v):
        pin(not v)  # Active low on ESP8266
    return func

# MQTT config
config['server'] = ''
config['port'] = 17021
config['user'] = ''
config['password'] = ''

# Wifi config
config['ssid'] = 'wifi'
config['wifi_pw'] = 'password'

# Other config
app_config = {}
app_config['sub_topic'] = ''
app_config['battery_led'] = 26
app_config['led_strip1'] = 15
app_config['led_strip2'] = 33
app_config['power_switch'] = 14
app_config['wifi_led'] = ledfunc(Pin(25, Pin.OUT, value = 0))  # Red LED for WiFi fail/not ready yet
app_config['battery_threshold'] = 3.6

