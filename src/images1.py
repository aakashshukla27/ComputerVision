import cv2

img = cv2.imread('Images/lena.jpg', 0)  # Read grayscale
# img = cv2.imread('Images/lena.jpg', 1)  # Read as color
# img = cv2.imread('Images/lena.jpg', -1)  # Load image as it is
print(img)

cv2.imshow('image', img)
# cv2.waitKey(5000) # if 0 window will wait till closed

k = cv2.waitKey(0) & 0xFF
if k == 27:  # Pressed escape key
    cv2.destroyAllWindows()
elif k == ord('s'):  # if s is pressed save image
    cv2.imwrite('Images/lena_copy.png', img)


