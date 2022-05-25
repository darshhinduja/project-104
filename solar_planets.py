import cv2
from cv2 import FONT_HERSHEY_COMPLEX
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "mercury",
            (100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "venus",
            (200,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "earth",
            (300,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "mars",
            (400,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "jupiter",
            (500,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "saturn",
            (750,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "uranus",
            (950,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "neptune",
            (1100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))



cv2.imshow("output",img)
cv2.waitKey(0)

