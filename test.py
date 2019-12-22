from plotbox import *
import cv2

image = cv2.imread("./test.jpg")
pt1=(60,45)
pt2=(430,500)
# plot box
drawRect(image,pt1,pt2,(0,0,255),thickness=1,style='solid')

# text_en
myText = 'Lena:97%'
font_size = 20
t_size = cv2.getTextSize(myText, 0, fontScale=0.2, thickness=2)[0]

new_pt2 = (pt1[0]+15*len(myText), pt1[1] - t_size[1]+10)
new_pt2 = (pt1[0] + len(myText)*10), pt1[1] - t_size[1] - 10

cv2.rectangle(image, pt1, new_pt2, (0,0,255), -1)  # filled
image = drawText(image,myText, (pt1[0],pt1[1] - t_size[1] - 20),font_size,(0,0,0),'en_1')

cv2.imshow('image',image)
# cv2.imwrite("./demo2.jpg",image)
cv2.waitKey()    
