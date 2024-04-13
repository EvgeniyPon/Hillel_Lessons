def temperature_get() ->float:
    temperature_str = input("Please enter degree of temperature to convert: ")
    if not temperature_str.isdigit():
        raise ValueError('the input has to be only numbers')
    return float(temperature_str)

def conversion_type_get():
    conversion_type = input("Please select conversion type:"
                            " \n('1' for Celsius to Fahrenheit, '2' for Fahrenheit to Celsius): ")
    if conversion_type not in ('1', '2'):
        raise ValueError('You should print 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius')
    return conversion_type
