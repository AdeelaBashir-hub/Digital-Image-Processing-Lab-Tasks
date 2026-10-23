# Exercise 1: Variables and Data Types

width = 640
height = 480
image_name = "sample.png"
is_color = True

print("Width:", width)
print("Height:", height)
print("Image name:", image_name)
print("Is color:", is_color)

print(type(width))
print(type(height))
print(type(image_name))
print(type(is_color))

print("Total pixels:", width * height)
# Exercise 2: If-Else Conditions

intensity = 256

if intensity < 0 or intensity > 255:
    print("Invalid")
elif intensity >= 128:
    print("Bright pixel")
else:
    print("Dark pixel")
# Exercise 3: For Loop
for intensity in range(0, 256, 50):
    print("Pixel intensity:", intensity)
# Exercise 3: While Loop

intensity = 0

while intensity <= 255:
    print("Intensity:", intensity)
    intensity += 50

# Exercise 4: Functions

def is_bright(pixel, threshold=128):
    if pixel >= threshold:
        return True
    else:
        return False

print("Pixel 100 is bright:", is_bright(100))
print("Pixel 150 is bright:", is_bright(150))
print("Pixel 200 is bright:", is_bright(200))
print("Pixel 100 with threshold 80:", is_bright(100, 80))
# Exercise 5: Lists and Tuples

pixel_values = [10, 50, 100, 150, 200, 255]

print("Pixel values:", pixel_values)
print("First pixel:", pixel_values[0])
print("Last pixel:", pixel_values[-1])
print("Number of pixels:", len(pixel_values))

pixel_values.append(75)
print("After adding a pixel:", pixel_values)

image_info = (640, 480)
print("Image dimensions:", image_info)
print("Image width:", image_info[0])
print("Image height:", image_info[1])
# Exercise 6: Dictionaries

image = {
    "name": "sample.png",
    "width": 640,
    "height": 480,
    "color": True
}

print("Image details:", image)
print("Image name:", image["name"])
print("Image width:", image["width"])
print("Image height:", image["height"])
print("Is color image:", image["color"])

image["width"] = 800
print("Updated width:", image["width"])




