from PIL import Image
import os

size_300 = (300,300)
# image1 = Image.open('img2.jpg')
# image1.save('img2.png')
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn,ftext = os.path.splitext(f)
#         i.save(f"images/{fn}.png")
# os.makedirs('300')
# image1 = Image.open('img2.jpg')
# image1.save('img2.png')
for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn,ftext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save(f"300/{fn}_300{ftext}")
