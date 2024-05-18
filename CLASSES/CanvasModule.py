from .ImageModule import Image
import cv2

class Canvas:
    def f(self,strSrc : str):
        self.redraw()

    def __init__(self,imagePath = str):
        self.__ObjImage = Image(imagePath,self.f)
        self.redraw()

    @property
    def Picture(self):
        return self.__ObjImage
    
    @Picture.setter
    def Picture(self,imgObject:Image):
        self.__ObjImage = imgObject;

    def redraw(self):
        matlike = cv2.imread(self.Picture.Src)
        cv2.imshow('valueless windows',matlike)
        cv2.waitKey()
        cv2.destroyAllWindows()