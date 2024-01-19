import cv2
#webcam 1 -> 0 idx
#webcam 2 -> 1 idx
camera = cv2.VideoCapture(0)
while camera.isOpened():
    state, frame = camera.read() #frame -> image captiured, state -> boolean
    if not state:
        print("Could not access camera")
        break
    cv2.imshow('Camera window', frame)
    if cv2.waitKey(1) == ord('q'): #if q is predded stop the loop
       break
camera.release()
cv2.destroyAllWindows()