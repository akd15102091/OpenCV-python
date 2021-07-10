import cv2

#--------------------------------Read Image------------------------------------
# img = cv2.imread("robo.jpg")
# print(img.shape)
# img = cv2.resize(img,(700,500))
#
# cv2.imshow("image",img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#------------------------------------------------------------------------------


cap = cv2.VideoCapture("road.mp4")
cap.set(3,512)
cap.set(4,512)
while cap.isOpened():
    flag, frame = cap.read()
    print(frame.shape)
    cv2.imshow("camera",frame)

    k = cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()