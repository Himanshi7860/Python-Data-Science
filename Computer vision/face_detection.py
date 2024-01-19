import cv2, os
import mediapipe as mp

file = r'computer vision/sample_vid2.mp4'  

if not os.path.exists(file):
    print('video file not found')
camera = cv2.VideoCapture(file) 

with mp.solutions.face_detection.FaceDetection(
    model_selection=1, 
    min_detection_confidence=.5) as fd:
    while True:
        state, frame = camera.read() 
        if not state:
            print("Could not access video")
            break
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = fd.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.detections:
            cv2.putText(frame,f'{len(results.detections)} faces',
                        (10, 30), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0,255,0), 2)
            for detection in results.detections:
                mp.solutions.drawing_utils.draw_detection(frame, detection)
        cv2.imshow('camera window', frame)
        if cv2.waitKey(20) == ord('q'): 
            break
    camera.release()
    cv2.destroyAllWindows()