import cv2
img=cv2.imread("cv.tif",1)
box=cv2.boxFilter(img,-1,(4,4))
blur=cv2.blur(img,(4,4))
gaus=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("original",img)
cv2.imshow("output1",box)
cv2.imshow("output2",blur)
cv2.imshow("output3",gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


