import cv2

cap = cv2.VideoCapture(0)  # Alternate value depending on camera number

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video Frame', frame)
    # cv2.imshow('Video Frame', gray)  # convert to grayscale
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()