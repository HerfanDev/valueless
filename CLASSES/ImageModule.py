import cv2
class Image:
    def __init__(self, src : str):
        self.src:str = src
        self.__h,self.__w,self.__c=cv2.imread(self.src).shape
