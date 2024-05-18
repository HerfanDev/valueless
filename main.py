path1 = r'C:\Users\BURUJ\Desktop\github\prj2\valueless\IMAGES\1.jpg'
path2 = r'C:\Users\BURUJ\Desktop\github\prj2\valueless\IMAGES\2.jpg'
from CLASSES.ImageModule import Image

objImage = Image(path1)
print(objImage.Src)
print('c : ',objImage.ChannelsCount)
print('w : ',objImage.WidthPX)
print('h : ',objImage.HeightPX)
objImage.Src = path2
print(objImage.Src)
print('c : ',objImage.ChannelsCount)
print('w : ',objImage.WidthPX)
print('h : ',objImage.HeightPX)
