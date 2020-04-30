import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img=cv2.imread("news.jpg")

grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img,
                                    scaleFactor=1.5,
                                    minNeighbors=3)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

resized=cv2.resize(img,(img.shape[1]//3,img.shape[0]//3))


cv2.imshow("Grey",img)
cv2.waitKey(0)
cv2.destroyAllWindows()