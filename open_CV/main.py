import cv2

img =  cv2.imread("C:\\Users\\LENOVO\\OneDrive\\Pictures\\images\\download.jpg")
cv2.imshow('image', img)
cv2.waitKey(2000)

print("The height and width of the image is:", img.shape)

w = int(input("Enter the new width (to remain unchanged enter 0): "))
h = int(input("Enter the new height (to remain unchanged enter 0): "))

if w == 0:
    w = img.shape[1]
if h == 0:
    h = img.shape[0]

dim = (w, h)

resized_img = cv2.resize(img, dim)
cv2.imshow('image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 