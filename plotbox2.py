import cv2
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from distutils.sysconfig import get_python_lib

base_path = get_python_lib()

# base function
def drawline(img,pt1,pt2,color,thickness=1,style='dotted',gap=5):
    dist =((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**.5
    pts= []
    for i in  np.arange(0,dist,gap):
        r=i/dist
        x=int((pt1[0]*(1-r)+pt2[0]*r)+.5)
        y=int((pt1[1]*(1-r)+pt2[1]*r)+.5)
        p = (x,y)
        pts.append(p)

    if style=='dotted':
        for p in pts:
            cv2.circle(img,p,thickness,color,-1)
    elif style=='dotted_1':
        s=pts[0]
        e=pts[0]
        i=0
        for p in pts:
            s=e
            e=p
            if i%2==1:
                cv2.line(img,s,e,color,thickness)
            i+=1

def drawpoly(img,pts,color,thickness=1,style='dotted',):
    s=pts[0]
    e=pts[0]
    pts.append(pts.pop(0))
    for p in pts:
        s=e
        e=p
        drawline(img,s,e,color,thickness,style)

def drawrect_(img,pt1,pt2,color,thickness=1,style='dotted'):
    pts = [pt1,(pt2[0],pt1[1]),pt2,(pt1[0],pt2[1])] 
    drawpoly(img,pts,color,thickness,style)



def change_cv2_draw(image,strs,local,sizes,colour,font="en_1"):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    # font = ImageFont.truetype("./font_lib/ch/youyuan1.ttf",sizes, encoding="utf-8")
    if font == 'en_1':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/Futura Lt BT.ttf",sizes, encoding="utf-8")
    elif font == 'en_2':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/AvantGarGotItcTEE.ttf",sizes, encoding="utf-8")
    elif font == 'en_3':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/HomeStoreRegular.ttf",sizes, encoding="utf-8")

    elif font == 'cn_1':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/kaitiGB2312.ttf",sizes, encoding="utf-8")
    elif font == 'cn-2':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/Microsoft-Yahei-UI-Light.ttc",sizes, encoding="utf-8")
    elif font == 'cn_3':
        font_ = ImageFont.truetype(base_path+"/plotbox/font/youyuan.TTF",sizes, encoding="utf-8")


    draw.text(local, strs, colour, font=font_)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

    return image

def drawRect(img,pt1,pt2,color,thickness=1,style='dotted'):
    '''
    param
       img: cv2 image
       pt1: (x_min,y_min)
       pt2: (x_max,y_max)
       color: the color of line
       thickness: the width of line
       style: the shape of the line in ['dotted','dotted_1','solid']

    '''
    if style in ["dotted","dotted_1"]:
        drawrect_(img,pt1,pt2,color,thickness=thickness,style=style)
    else:
        cv2.rectangle(img, pt1,pt2,color,thickness=thickness)



def drawText(image,strs,local,sizes,colour,font="en_1"):
    '''
    image: cv2 image
    strs: text
    local: start point
    size: text size
    colour: text colour
    font: test font in ['en_1',"en_2","en_3","cn_1","cn_2","cn_3"]

    '''
    
    image = change_cv2_draw(image,strs,local,sizes,colour,font)

    return image



if __name__ == "__main__":
    # pass

    
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
    image = drawText(image,myText, (pt1[0],pt1[1] - t_size[1] - 20),font_size,(0,0,0))


    cv2.imshow('image',image)
    cv2.imwrite("./demo1.jpg",image)
    cv2.waitKey()    


    # text_cn
    myText = '莱娜:97%'
    font_size = 20

    t_size = cv2.getTextSize(myText, 0, fontScale=0.2, thickness=2)[0]
 
    new_pt2 = (pt1[0]+15*len(myText), pt1[1] - t_size[1]+10)
    new_pt2 = (pt1[0] + len(myText)*15), pt1[1] - t_size[1] - 20
    
    cv2.rectangle(image, pt1, new_pt2, (0,0,255), -1)  # filled
    image = drawText(image,myText, (pt1[0],pt1[1] - t_size[1] - 15),font_size,(0,0,0),font='cn_3')


    cv2.imshow('image',image)
    cv2.imwrite("./demo2.jpg",image)
    cv2.waitKey()    



    
