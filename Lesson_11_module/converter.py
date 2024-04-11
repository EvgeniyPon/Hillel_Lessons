from user_input import temperature_get, conversion_type_get
from cels_to_fahren import *
from fahren_to_cels import *

temperature = temperature_get()
conversion_type = conversion_type_get()
def converter(temperature: float, conversion_type: str) -> str:
    if conversion_type == '1':
        return f'{temperature} C = {celsius_to_fahrenheit(temperature)} F'
    elif conversion_type == '2':
        return f'{temperature} F = {fahrenheit_to_celsius(temperature)} C'