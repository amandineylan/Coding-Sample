#Program that reduces an image size by 3 through pixalisation

#libary imports
from PIL import Image 
from math import ceil, sqrt

#opening image file
im1 = Image.open("Drawing.png") 
nW = int(ceil(im1.width/3))
nH = int(ceil(im1.height/3))
im2 = Image.new("RGB", (nW, nH)) #creating second image placeholder


#Variable Declarations
r = 0
g = 0
b = 0
MeanVarT = 0

#For block of 3x3 pixels
for y in range(0, im1.width-1,3):
 for x in range(0, im1.height-1,3):

   #Temporarily store each of the 9 pixels
   p1 = im1.getpixel((x,y))
   p2 = im1.getpixel((x-1,y-1))
   p3 = im1.getpixel((x-1,y))
   p4 = im1.getpixel((x-1,y+1))
   p5 = im1.getpixel((x,y-1))
   p6 = im1.getpixel((x,y+1))
   p7 = im1.getpixel((x+1,y-1))
   p8 = im1.getpixel((x+1,y))
   p9 = im1.getpixel((x+1,y+1))

   #Find the Mean colour for 3x3 pixels, we could look at other features like Variance

   r = round((p1[0]+p2[0]+p3[0]+p4[0]+p5[0]+p6[0]+p7[0]+p8[0]+p9[0])/9)
   v = round((p1[1]+p2[1]+p3[1]+p4[1]+p5[1]+p6[1]+p7[1]+p8[1]+p9[1])/9)
   b = round((p1[2]+p2[2]+p3[2]+p4[2]+p5[2]+p6[2]+p7[2]+p8[2]+p9[2])/9)
   
   # Calculating arbitrary Measure of variance for overall image by new pixel

   MeanVar=(sqrt((r^2)/9+(v^2)/9+(b^2)/9)/3)
   MeanVarT= (MeanVarT+MeanVar/(nW*nH))

   #Place new colours in pixels of new image
   im2.putpixel((int(ceil(x/3)),int(ceil(y/3))),(r,v,b))

#saving new image
im2.save("Pixalated Image.png")

print("MeanVAr for each new pixel was:", MeanVarT)
