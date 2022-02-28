import cv2
import numpy as np
import math
from download_img import downloadImage


def processImageForGreenCover( locid, id , lat, long, zoom):
    
    basepath = '../greencanopy/'
    filename = 'static/'+str(locid)+'/'+str(id)+'_' + 'google_img.jpg'
    filenameout = 'static/'+ str(locid)+'/'+str(id)+'_' + 'gray_img.jpg'

    print(filename)
    downloadImage(lat, long, zoom, basepath +  filename )

    ## Read
    img = cv2.imread(filename)

    ## greyscale image
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    mask = cv2.inRange(hsv, (30, 40, 40), (140, 255,255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    green_grayed = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)


    dimensions = green_grayed.shape
    #print(dimensions)

    count = 0
    x = dimensions[0]
    y = dimensions[0]

    x = x - 1
    y = y - 1


   # print(green_grayed[10,0])

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            value = green_grayed[i][j]
            if value>0:
                #print(value)
                count = count + 1


    print("Count is " + str(count))

    total_pixels = x*y

    #cv2.imshow("green", green)
  #  cv2.waitKey(0)
   # cv2.imshow("grayimg", green_grayed)
   # cv2.waitKey(0)


    # cv2.imwrite("green2.png", green)
    cv2.imwrite(filenameout, green)

    print(zoom)
    print(type(lat))
    #length_of_pixel = 156543.03392 * math.cos(18.444665 * math.pi / 180) / math.pow(2, 8)
    length_of_pixel = (math.cos(float(lat) * math.pi/180) * 2 * math.pi * 6378137) / (256 * math.pow(2, int(zoom))) 

    total_area = 400*400 * length_of_pixel * length_of_pixel/1000000

    area_green = count * length_of_pixel * length_of_pixel / 1000000 

    print("Total area in km^2 is", total_area)

    percent = count*100 / total_pixels
    print("\nPercentage of greenery is ", percent)

    d = dict()
    d['percentage'] = percent
    d['greenarea'] = area_green
    d['totalarea'] = total_area
    d['in_image'] = filename
    d['out_image'] = filenameout

    return d