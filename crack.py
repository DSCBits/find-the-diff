#pip3 install opencv-python
import cv2

#Enter image name of first image cimage to compare
imagename = ""

#Enter image name of second image newimage to compare
imagename2 = ""
img = cv2.imread(imagename)
img2 = cv2.imread(imagename2)

(length, breadth, color) = img.shape

for i in range(length):
    for j in range(breadth):
        if img[i, j].all() != img2[i, j].all():
            print(img2[i,j])

cv2.waitKey(0)
cv2.destroyAllWindows()
