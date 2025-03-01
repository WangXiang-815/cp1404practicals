# A constant dictionary with 10 color names and their corresponding hexadecimal codes
COLOR_NAME_TO_HEX = {
    "aliceBlue": "#f0f8ff", "antiqueWhite": "#faebd7", "aqua": "#00ffff", "azure": "#f0ffff",
    "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000", "blanchedAlmond": "#ffebcd",
    "blue": "#0000ff", "blueViolet": "#8a2be2"
}

# Loop to get color name input and return the corresponding hexadecimal code
colour_name = input("Enter a colour name: ").lower()  # Convert input to lowercase
while colour_name != "":
    hex_code = COLOR_NAME_TO_HEX.get(colour_name)
    if hex_code:
        print(f"The code for \"{colour_name.title()}\" is {hex_code}")
    else:
        print(f"Invalid colour name: \"{colour_name.title()}\"")

    # Ask the user to input another colour name or blank to stop
    colour_name = input("Enter a colour name: ").lower()  # Convert input to lowercase