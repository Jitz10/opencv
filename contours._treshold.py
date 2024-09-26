import cv2

# Load the image
image = cv2.imread('Photos/cat1.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Count the number of contours
number_of_contours = len(contours)

print(f"Number of contours: {number_of_contours}")

# Optionally, you can draw the contours on the image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Show the result
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
