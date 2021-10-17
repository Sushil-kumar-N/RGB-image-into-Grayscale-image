from PIL import Image

image = Image.open("E:\money heist.jpg")
#Display RGB image
image.show()

image = Image.open("E:\money heist.jpg").convert('L')
#Display Grayscale image
image.show()

#Save image
image.save("E:\money heist_gs.jpg")