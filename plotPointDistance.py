#!/usr/bin/python
import math
pointOne = input("Enter x1 and y1 for Point 1: ")
(x1,y1) = pointOne.split(",")
(x1,y1) = (float(x1.strip()), float(y1.strip()))
pointTwo = input("Enter x2 and y2 for Point 2: ")
(x2,y2) = pointTwo.split(",")
(x2,y2) = (float(x2.strip()), float(y2.strip()))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance between (%.1f, %.1f) and (%.1f, %.1f) is %.1f"\
% (x1, y1, x2, y2, distance))
