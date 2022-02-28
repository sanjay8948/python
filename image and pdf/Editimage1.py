from PIL import Image,ImageEnhance
img1=Image.open('SS.jpg')

#Sharpness**************************************************

#enhancer=ImageEnhance.Sharpness(img1)
#enhancer.enhance(1).save('Editted.jpg')


#color******************************************************

#enhancer=ImageEnhance.Color(img1)
#enhancer.enhance(4).save('Editted.jpg')


#Brightness*************************************************

#enhancer=ImageEnhance.Brightness(img1)
#enhancer.enhance(2).save('Editted.jpg')


#contrast***************************************************

enhancer=ImageEnhance.Contrast(img1)
enhancer.enhance(2).save('Editted.jpg')



