import cv2
import math

for x in range(5):

  if x == 0:
    imgPath = 'A.png'
  elif x == 1:
    imgPath = 'B.png'
  elif x == 2:
    imgPath = 'C.png'
  elif x == 3:
    imgPath = 'D.png'
  else:
    imgPath = 'E.png'

  img = cv2.imread(imgPath)

  # convert image to grayscale image
  gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # convert the grayscale image to binary image
  ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

  print(ret)

  # calculate moments of binary image
  M = cv2.moments(thresh)

  # calculate x,y coordinate of center
  cX = int(M["m10"] / M["m00"])
  cY = int(M["m01"] / M["m00"])

  # put text and highlight the center
  cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
  cv2.putText(img, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

  # display the image
  cv2.imshow("Image", img)
  cv2.waitKey(0)

  # Read image as grayscale image
  im = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

  # Threshold image
  _, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

  # Calculate Moments
  moments = cv2.moments(im)

  # Calculate Hu Moments
  huMoments = cv2.HuMoments(moments)

  # Log scale hu moments
  for i in range(0,7):
    huMoments[i]=-1*math.copysign(1.0, huMoments[i])*math.log10(abs(huMoments[i]))
    print(huMoments[i])