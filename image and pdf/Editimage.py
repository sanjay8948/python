from PIL import Image
import os

#change extension**********************************************

img1=Image.open('akhil.jpg')

img1.save('Akhil.png')
img1.save('Akhil.pdf')
img1.show()

#Resize*****

#MAX_SIZE=(250,250)
#img1.thumbnail(MAX_SIZE)
#img1.save('Akhilsmall.jpg')


#change extension and size using loop*********************************
  
#for item in os.listdir():
#    if item.endswith('.jpg'):
#        img1=Image.open(item)
#        filename,extension=os.path.splitext(item)
#        img1.save(f'{filename}.png')


#MAX_SIZE=(250,250)
#for item in os.listdir():
#    if item.endswith('.jpg'):
#        img1=Image.open(item)
#        img1.thumbnail(MAX_SIZE)
#        filename,extension=os.path.splitext(item)
#        img1.save(f'{filename}small.{extension}')


      
