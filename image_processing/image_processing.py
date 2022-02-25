import cv2
import numpy as np
import math

## Read
img = cv2.imread("google_img.jpg")

## greyscale image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (30, 40, 40), (70, 255,255))

## slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

green_grayed = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)


dimensions = green_grayed.shape
print(dimensions)

count = 0
x = dimensions[0]
y = dimensions[0]

x = x - 1
y = y - 1


print(green_grayed[10,0])

for i in range(dimensions[0]):
    for j in range(dimensions[1]):
        value = green_grayed[i][j]
        if value>0:
            print(value)
            count = count + 1


print("Count is " + str(count))

total_pixels = x*y

#cv2.imshow("green", green)
cv2.waitKey(0)
cv2.imshow("grayimg", green_grayed)
cv2.waitKey(0)


# cv2.imwrite("green2.png", green)
# cv2.imwrite("grayimg.png", imgray)


length_of_pixel = 156543.03392 * math.cos(18.444665 * math.pi / 180) / math.pow(2, 8)

total_area = count * length_of_pixel * length_of_pixel

print("Total area in m^2 is")
print(total_area)

percent = count*100 / total_pixels
print("\nPercentage of greenery is ", percent)


cv2.destroyAllWindows()