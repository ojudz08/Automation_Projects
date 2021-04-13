import cv2
import os

# open all images in the current directory and resize it to 300x300
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        print(filename)
        img = cv2.imread(filename, 1)
        resized_img = cv2.resize(img, (300, 300))
        cv2.imshow(filename, resized_img)
        cv2.waitKey(500)
        #cv2.destroyAllWindows()