# Name (ID): Vu Tuong Nguyen (30305839)
# Tutorial: 14

from SimpleGraphics import *

#asking chart information
name = input("Enter the chart name: ")

bar_name1 = str(input("Enter name for bar 1: "))
num1 = int(input("Enter number for bar 1 in pixel (maximum250): "))
bar_color1 = input("Enter color of bar 1: ")
    
barcolor1 = bar_color1.lower()



bar_name2 = str(input("Enter name for bar 2: "))
num2 = int(input("Enter number for bar 2 in pixel (maximum250): "))
bar_color2 = input("Enter color of bar 2: ")

barcolor2 = bar_color2.lower()


bar_name3 = str(input("Enter name for bar 3: "))
num3 = int(input("Enter number for bar 3 in pixel (maximum250): "))
bar_color3 = input("Enter color of bar 3: ")

barcolor3 = bar_color3.lower()



#asking for the position of chart
x = int(input("Enter the x-coordinate of the chart: "))
y = int(input("Enter the y-coordinate of the chart: "))


#drawing columns
setFill(barcolor1)
rect(x+30,y-num1,100,num1)

setFill(barcolor2)
rect(x+160,y-num2,100,num2)

setFill(barcolor3)
rect(x+290,y-num3,100,num3)

#x-axis and y-axis
line(x,y-300,x,y) #x
line(x,y,x+400,y) #y


#chart title
setFont("Garamond",16,"bold")
text(x+200,y-285,name,"s")

#adding labels to axes
setFont("TimesNewRomance",10,"bold")
text(x+80,y-(num1+7),bar_name1,"c")

setFont("TimesNewRomance",10,"bold")
text(x+210,y-(num2+7),bar_name2,"c")

setFont("TimesNewRomance",10,"bold")
text(x+340,y-(num3+7),bar_name3,"c")

#attaching values of each columns on top of them
setFont("TimesNewRomance",10,"bold")
text(x+80,y-(num1/2),num1,"c")

setFont("TimesNewRomance",10,"bold")
text(x+210,y-(num2/2),num2,"c")

setFont("TimesNewRomance",10,"bold")
text(x+340,y-(num3/2),num3,"c")