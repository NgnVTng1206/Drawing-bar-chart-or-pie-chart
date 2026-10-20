from SimpleGraphics import*

first_x = 200
first_y = 300
env_width = 400
env_heigth = 200


setFill("sandy brown")
setOutline("brown")
rect(first_x,first_y,env_width,env_heigth)

polygon(first_x,first_y,first_x + env_width/2,first_y-env_heigth/2,first_x+env_width,first_y)

imagename = "stamp.gif"
image = loadImage(imagename)
drawImage = (image,200,500)