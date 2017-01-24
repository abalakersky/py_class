def c2f(celsius):
    """Convert from celsius to fahrenheit"""
    if celsius < -273.15:
        return "You gave temperature that is way too low"
    else:
        fahrenheit = celsius*1.8+32
        return fahrenheit

print(c2f(-280))

