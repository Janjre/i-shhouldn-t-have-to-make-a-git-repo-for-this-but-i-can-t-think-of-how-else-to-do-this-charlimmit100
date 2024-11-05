from LCD1602 import LCD1602
import time

# Initialize the LCD (assuming the default I2C address and columns/rows)
lcd = LCD1602(0x27, 16, 2)

# Predefined custom character pixel patterns for the 5x8 dot matrix.
# Each list defines an 8-row binary pattern, where each bit represents a pixel in that row.
patterns = {
    "top_left": [0b10000, 0, 0, 0, 0, 0, 0, 0],
    "top_center": [0b01000, 0, 0, 0, 0, 0, 0, 0],
    "top_right": [0b00100, 0, 0, 0, 0, 0, 0, 0],
    "bottom_left": [0, 0, 0, 0, 0, 0, 0b10000, 0],
    "bottom_center": [0, 0, 0, 0, 0, 0, 0b01000, 0],
    "bottom_right": [0, 0, 0, 0, 0, 0, 0b00100, 0]
}

# Load the custom characters into the LCD
def load_patterns():
    lcd.create_char(0, patterns["top_left"])
    lcd.create_char(1, patterns["top_center"])
    lcd.create_char(2, patterns["top_right"])
    lcd.create_char(3, patterns["bottom_left"])
    lcd.create_char(4, patterns["bottom_center"])
    lcd.create_char(5, patterns["bottom_right"])

# Set a "pixel" at a specified character cell position and within that cell's grid.
# x and y are character-based coordinates for the 16x2 grid.
# sub_x and sub_y are pixel-based coordinates within each 5x8 character grid.
def set_pixel(x, y, sub_x, sub_y):
    # Map sub_x and sub_y to one of the custom patterns
    if (sub_x, sub_y) == (0, 0):
        char_code = 0  # top_left
    elif (sub_x, sub_y) == (2, 0):
        char_code = 1  # top_center
    elif (sub_x, sub_y) == (4, 0):
        char_code = 2  # top_right
    elif (sub_x, sub_y) == (0, 7):
        char_code = 3  # bottom_left
    elif (sub_x, sub_y) == (2, 7):
        char_code = 4  # bottom_center
    elif (sub_x, sub_y) == (4, 7):
        char_code = 5  # bottom_right
    else:
        print("Invalid sub-pixel coordinates")
        return

    # Display the custom character at the specified (x, y) character position
    lcd.setCursor(x, y)
    lcd.write(char_code)

# Clear the display
def clear_display():
    lcd.clear()

# Example usage
try:
    lcd.init_LCD()    # Initialize LCD
    load_patterns()   # Load custom character patterns

    clear_display()
    time.sleep(1)

    # Example: Turn on pixels in character cell (0,0)
    set_pixel(0, 0, 0, 0)    # Top left of the character
    time.sleep(0.5)
    set_pixel(0, 0, 2, 0)    # Top center of the character
    time.sleep(0.5)
    set_pixel(0, 0, 4, 0)    # Top right of the character
    time.sleep(0.5)
    set_pixel(0, 0, 0, 7)    # Bottom left of the character
    time.sleep(0.5)
    set_pixel(0, 0, 2, 7)    # Bottom center of the character
    time.sleep(0.5)
    set_pixel(0, 0, 4, 7)    # Bottom right of the character
    time.sleep(0.5)

    # Clear display after testing
    clear_display()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    lcd.backlight(0)
