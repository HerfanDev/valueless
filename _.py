class Door:
    def __init__(self, stateChanged = None):
        self.__isClose = True
        self.__stateChanged = stateChanged
        pass
    @property
    def IsClose(self):
        return self.__isClose
    
    @IsClose.setter
    def IsClose(self,state:bool):
        self.__isClose = state
        if self.__stateChanged != None :
            self.__stateChanged(self.__isClose)
        
class House:
    def __f(self,state):
        print(f'I am House and Understand state of door changed to {'Close' if state else 'Open'}!')

    def __init__(self):
        self.__door = Door(self.__f)

    @property
    def DoorOfHouse(self):
        return self.__door
    
    @DoorOfHouse.setter
    def DoorOfHouse(self,newDoor : Door):
        self.__door = newDoor

myHouse = House()
myHouse.DoorOfHouse.IsClose = True
myHouse.DoorOfHouse.IsClose = False

def OnCloseOpenChanged(state):
    print('Changed to ',state)

d = Door(OnCloseOpenChanged)
d.IsClose = False
d.IsClose = True

door2 = Door()
door2.IsClose = False
door2.IsClose = True