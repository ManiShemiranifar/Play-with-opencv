import cv2 as cv 
import numpy as np


def create(sensivity,number_of_zeros,px_size):

        img = np.zeros((number_of_zeros, number_of_zeros, 3))
        x = number_of_zeros
        y = number_of_zeros
        points = []

        try:
        
                for i in range(1,sensivity+1):
                        points.append(int(x*(i/sensivity)))
            
                for point_up_to_down in points:
                        cv.line(img, (point_up_to_down,y), (point_up_to_down,0), (255,0,0), px_size)
                        cv.imwrite("Output.jpg",img)

                for point_right_to_left in points:
                        cv.line(img, (0,point_right_to_left), (x,point_right_to_left), (255,0,0), px_size)
                        cv.imwrite("Output.jpg",img)

                for point_up_to_left in points:
                        cv.line(img, (0,point_up_to_left), (point_up_to_left,0), (0,0,255), px_size)
                        cv.imwrite("Output.jpg",img)
            
                for point_up_to_right in points:
                        cv.line(img, (x,point_up_to_right), (point_up_to_right,y), (254,0,0), px_size)
                        cv.imwrite("Output.jpg",img)

                for point_right_to_down in points:
                        cv.line(img, (0,point_right_to_down), (point_up_to_right,y), (253,0,0), px_size)
                        cv.imwrite("Output.jpg",img)

                for point_left_to_down in points:
                        cv.line(img, (point_left_to_down,0), (point_up_to_right,y), (252,0,0), px_size)
                        cv.imwrite("Output.jpg",img)

                print("Successfully done!!")

        except:
                print("Something went wrong!!")


create(300,1000,1)