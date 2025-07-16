def convert_temperature(value, unit):
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        value (float): The temperature value to convert.
        unit (str): The unit of the input temperature ('C' or 'F').

    Returns:
        float: The converted temperature value.
        str: The unit of the converted temperature.
    """
    if unit.upper() == 'C':
        # Celsius to Fahrenheit
        converted = (value * 9/5) + 32
        return converted, 'F'
    elif unit.upper() == 'F':
        # Fahrenheit to Celsius
        converted = (value - 32) * 5/9
        return converted, 'C'
    else:
        raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    try:
        temp =