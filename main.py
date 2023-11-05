# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
import cv2
import numpy as np
import move

def opencv_track_white_ball():
    cam = cv2.VideoCapture(0)

    print('cam has image : %s' % cam.read()[0])

    if cam.read() is False:
        cam.open()

    if not cam.isOpened():
        print('Cannot open camera')
        return;

    move.setup()

    while (True):
        lowerBound = np.array([0, 0, 150])  # Lower HSV values
        upperBound = np.array([180, 55, 200])  # Upper HSV values
        ret, img = cam.read()
        img = cv2.resize(img, (340, 220))[0: 220, 25: -40]
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ksize = (5, 5)
        blurred_image = cv2.GaussianBlur(imgHSV, ksize, 0)
        mask2 = cv2.inRange(blurred_image, lowerBound, upperBound)

        kernelOpen = np.array([[0, 0, 1, 0, 0],
                               [0, 1, 1, 1, 0],
                               [1, 1, 1, 1, 1],
                               [0, 1, 1, 1, 0],
                               [0, 0, 1, 0, 0]], dtype=np.uint8)

        maskOpen = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernelOpen)
        kernelClose = np.ones((20, 20))
        maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)
        maskFinal = maskClose
        conts, h = cv2.findContours(
            maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, conts, -1, (255, 0, 0), 3)

        # Initialize variables to store the total X and Y coordinates
        total_x = 0
        total_y = 0
        total_points = 1  # Total number of points in all contours

        # Loop through each contour
        for contour in conts:
            for point in contour:
                x, y = point[0]  # Extract X and Y coordinates of the point
                total_x += x
                total_y += y
                total_points += 1

        # Calculate the average X and Y coordinates
        average_x = total_x / total_points
        average_y = total_y / total_points

        print("Average Point (X, Y): ({}, {})".format(average_x, average_y))
        if(average_y != 0 and average_x != 0):
            average_y /= 2.2
            if(average_y < 33):
                average_y += 33
            if(average_y > 66):
                average_y -= 33
            move.move(average_y, average_y)
            if(average_x > 120):
                move.kickFront()
            else:
                move.kickBack()
        else:
            move.move(50, 50)

        cv2.imshow("hsv version", imgHSV)
        cv2.imshow("blurry", blurred_image)
        cv2.imshow("mask", mask2)
        cv2.imshow("maskOpen", maskOpen)
        cv2.imshow("maskClose", maskClose)
        cv2.imshow("cam", img)



        #playerGoalPostLeft = (261.8181818181818, 128.6)
        #playerGoalPostRight = (265.0, 79.5)

        # Calculate the slope (m) of the line
        #m = (playerGoalPostRight[1] - playerGoalPostLeft[1]) / \
          #E  (playerGoalPostRight[0] - playerGoalPostLeft[0])

        #if average_y - playerGoalPostLeft[1] >= m * (average_x - playerGoalPostLeft[0]):
         #   print("GOALGOALGOALGOAL COMPUTER GOT GOAL.")

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        cv2.waitKey(10)


def opencv_test():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, image = cap.read()
        cv2.imshow("Example", image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opencv_track_white_ball()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/