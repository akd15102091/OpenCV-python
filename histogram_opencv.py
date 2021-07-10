import cv2
import matplotlib.pylab as plt

img = cv2.imread("data/butterfly.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(len(img.ravel()))
cv2.imshow("frame", img)

plt.hist(img.ravel(),256,(0,256))
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()