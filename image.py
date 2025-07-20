from PIL import Image, ImageFilter

img= Image.open('./Pokedex/pikachu.jpg')
# bluring an image
filtered_img = img.filter(ImageFilter.BLUR)
# saving an image
filtered_img.save("blur.png", 'png')

# converting images
filtered_img2=img.convert('L')
filtered_img2.save("grey.png", 'png')
