import cv2

imagePath = input("Path to image: ")
scale_percent = int(input("Scale factor in %: "))

with open("text.txt", "w") as text:

    image = cv2.imread(imagePath)
    
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    
    grayImage = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    height, width = grayImage.shape[:2]

    scale_factor = 2

    for y in range(height):
        for sy in range(scale_factor):
            for x in range(width):
                brightnessValue = grayImage[y, x]
                if brightnessValue < 24:
                    text.write("@")
                elif brightnessValue < 48:
                    text.write("%")
                elif brightnessValue < 72:
                    text.write("#")
                elif brightnessValue < 96:
                    text.write("*")
                elif brightnessValue < 120:
                    text.write("+")
                elif brightnessValue < 144:
                    text.write("=")
                elif brightnessValue < 168:
                    text.write("-")
                elif brightnessValue < 192:
                    text.write(":")
                elif brightnessValue < 216:
                    text.write(".")
                else:
                    text.write(" ")
                text.write("    ")
            text.write("\n")