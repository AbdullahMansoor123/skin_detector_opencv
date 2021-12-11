import cv2

image = cv2.imread('jurassic-park-jeep.jpg')
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# # print the image dimension
# print(image.shape)

##Resizing##
#maintaing the aspect ration of the image
r= 100.0/image.shape[1]
dim = (100, int(image.shape[0]*r))

#show image after resizing
resized = cv2.resize(image,dim,cv2.INTER_AREA)
# cv2.imshow('resized', resized)
# cv2.waitKey(0)

##rotating the image##
(h,w) =image.shape[:2]
center = (w/2, h/2)

#rotating image by 180 degrees
M = cv2.getRotationMatrix2D(center,180,1.0)
rotated = cv2.warpAffine(image, M, (w,h))
# cv2.imshow('rotated', rotated)
# cv2.waitKey(0)

##Cropping a image
cropped = image[70:170, 440:540]
# cv2.imshow('cropped', cropped)
# cv2.waitKey(0)

#saving the processed image
# cv2.imwrite('someone.png', cropped)