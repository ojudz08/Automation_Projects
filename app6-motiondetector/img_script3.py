import cv2
import glob

images = glob.glob("*.jpg")

# open all images in the current directory and resize it to 300x300
for image in images:
    img = cv2.imread(image,1)
    re = cv2.resize(img,(300,300))
    cv2.imshow(image,re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    #cv2.imwrite("resized_"+image,re)