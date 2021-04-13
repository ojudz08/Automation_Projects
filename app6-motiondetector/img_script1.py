import cv2

img = cv2.imread("galaxy.jpg", 0)

print(img.shape)
# resized the image since it'll not fit in the whole window, the image size is  (1485, 990)
#     resized_img = cv2.resize(img, (1000, 800))
resized_img = cv2.resize(img, (int(img.shape[1]/0.9), int(img.shape[0]/1.8)))   # resized image from the size dimension of the image
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_rszd.jpg", resized_img)
cv2.waitKey(0)   # you may input 5000 --> 5 sec before closing the image
cv2.destroyAllWindows()