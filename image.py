import glob
from PIL import Image

#Retriving all image names and it's path with .jpg extension from given directory path in imageNames list
imageNames = glob.glob(r"C:\Users\Me\Desktop\test\*.jpg")

#Defining width and height of image
#new_width  = 800
#new_height = 600

#Count variable to show the progress of image resized
count=0

#Creating for loop to take one im
age from imageNames list and resize
for i in imageNames:
    img = Image.open(i)
    img = img.resize((img.width//2, img.height//2))
    img.save(r"C:\Users\Me\Desktop\test\small\\"+str(count)+".jpg")
    count+=1
    print("Images Resized " +str(count)+"/"+str(len(imageNames)),end='\r')
