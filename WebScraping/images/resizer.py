from PIL import Image


paragraphs = 6

im = Image.open('./images/body0.png')

print(im.size)

#for i in range(paragraphs):
#    im = Image.open('./images/body' + str(i) +'.png')

#    im.show()

#    resized_im = im.resize((round(im.size[0]*2), round(im.size[1]*2)))

#    resized_im.show()

#    resized_im.save('./images/body' + str(i) +'.png')