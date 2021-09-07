import cv2
from time import time
from vision import Vision
from windowcapture import WindowCapture

wincap = WindowCapture('METIN2')
vision_test = Vision('test.jpg')
vision_alchimist = Vision('alchimist.jpg')


fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
vid = cv2.VideoWriter('record.avi', fourcc, 8, (500, 490))



loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    #cv2.imshow("Capture", screenshot)
    points = vision_alchimist.find(screenshot, 0.5, 'rectangles')
    points = vision_test.find(screenshot, 0.5, 'rectangles')




    #fps debug
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()


#exit program
    key = cv2.waitKey(1)
    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()




#click on screen
#pyautogui.click(button="left")
#time.sleep(0.5)

