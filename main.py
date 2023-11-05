# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np


def opencv_track_white_ball():
    while(True):
        lowerBound = np.array([0, 0, 150])  # Lower HSV values
        upperBound = np.array([180, 55, 200])  # Upper HSV values
        cam = cv2.VideoCapture(0)
        ret, img = cam.read()
        img = cv2.resize(img, (340,220))
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ksize = (5, 5)  # Adjust the kernel size for stronger or weaker blurring
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
        conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

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

        # The (average_x, average_y) represents the centroid of all the points in the contours

        print("Average Point (X, Y): ({}, {})".format(average_x, average_y))

        cv2.imshow("cam", img)
        cv2.imshow("hsv version", imgHSV)
        cv2.imshow("blurry", blurred_image)
        cv2.imshow("mask", mask2)
        cv2.imshow("maskOpen", maskOpen)
        cv2.imshow("maskClose", maskClose)

        playerGoalPostLeft = (261.8181818181818, 128.6)
        playerGoalPostRight = (265.0, 79.5)

        # Calculate the slope (m) of the line
        m = (playerGoalPostRight[1] - playerGoalPostLeft[1]) / (playerGoalPostRight[0] - playerGoalPostLeft[0])

        # Define the point you want to check
        test_point = (x, y)  # Replace x and y with the coordinates of your point

        # Use the point-slope equation to check if the point is on or above the line
        if test_point[1] - playerGoalPostLeft[1] >= m * (test_point[0] - playerGoalPostLeft[0]):
            print("GOALGOALGOALGOAL COMPUTER GOT GOAL.")

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
