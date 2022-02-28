from PIL import image

img1=Image.open('sss.jpg')
img2=Image.open('Akhil.jpg')

img1.save('photo1_pdf.pdf','PDF',resolution=100.0,save_all=True,append_images=['img2'])


