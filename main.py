from CLASSES.CanvasModule import Canvas
from CLASSES.ImageModule import Image

strPath1 = r'C:\Users\BURUJ\Desktop\github\prj2\valueless\IMAGES\1.jpg'
strPath2 = r'C:\Users\BURUJ\Desktop\github\prj2\valueless\IMAGES\2.jpg'
strPath3 = r'C:\Users\BURUJ\Desktop\github\prj2\valueless\IMAGES\3.jpg'

def GetInfoOfCanvasImage(objCanvas : Canvas):
    print('\tcanvas image source :',objCanvas.Picture.Src)
    print('\tcanvas image width  :',objCanvas.Picture.WidthPX)
    print('\tcanvas image height :',objCanvas.Picture.HeightPX)
    print('\tcanvas image channels count :',objCanvas.Picture.ChannelsCount)

objCanvas = Canvas(strPath1)    #create a object from Canvas class
objCanvas.Picture.Src = strPath2