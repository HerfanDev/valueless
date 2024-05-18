import cv2
class Image:
    def __init__(self, src : str , onSrcChangedFunc = None):
        self.__src:str = src
        self.__h,self.__w,self.__c=cv2.imread(self.__src).shape
        self.__onSrcChangedFunc = onSrcChangedFunc
    
    @property
    def HeightPX(self):
        return self.__h
    
    @property
    def WidthPX(self):
        return self.__w
    
    @property
    def ChannelsCount(self):
        return self.__c
    @property
    def Src(self):
        return self.__src
    
    @Src.setter
    def Src(self,src:str):
        self.__src = src
        self.__h,self.__w,self.__c=cv2.imread(self.__src).shape
        if self.__onSrcChangedFunc!=None:
            self.__onSrcChangedFunc(self.Src)