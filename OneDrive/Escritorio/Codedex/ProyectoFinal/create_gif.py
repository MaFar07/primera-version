#import imageio.v3 as iio 

#filenames= ['team-pic1.png','team-pic2.png']
#images=[]

#loop to go throught the file paths and read the images usin imagenio librarys
#for filename in filenames:
#    images.append(iio.imread(filename))
    
#the .imread method loads an image based on the file path.so now,our images variable has all the images
#lastle use the .imwrite() method to turn the images into a gif

#iio.imwrite('team.gif', images, duration = 500, loop= 0)

#this take four arguments
#team.gif this is the name we want to give to our new GIF file
#images, the list cointaining the image data
#duration, how long each picture should show in the GIF
#loop, how many times the GIF should repeat(0means it keeps looping forever)

import imageio.v3 as iio

filenames = [
    'C:\\Users\\aguil\\OneDrive\\Escritorio\\python\\dino1.png', 
    'C:\\Users\\aguil\\OneDrive\\Escritorio\\python\\chicklet1.png',
    'C:\\Users\\aguil\\OneDrive\\Escritorio\\python\\hippocorn1.png'
]
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration=500, loop=0)
   
