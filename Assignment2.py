from SimpleGraphics import*

font_name = "Arial"
chart_colors = ["red","green","blue","yellow","orange","pink"]


while True:

    chart_type = input("Do you want to draw a bar chart or a pie chart?: ").lower()
    
    if "pie" in chart_type:
        # position of the pie 
        diameter = 400
        center_x = 400
        center_y = 300
        pie_left = 200
        pie_top = 100
        pie_right = 600
        pie_bottom = 500


        # ask for chart's information
        chart_name = input("Enter the title of the chart: ")
        total = float(input("Enter the total value of the chart: "))
        num_sector = int(input("Enter the number of sectors (2 to 6): "))

        sector_label = []
        sector_value = []
        remaining = total

        for i in range (num_sector-1):
            label = input(f"Enter the label for sector {i+1}: ")
            sector_label.append(label)
            num = float(input(f"Enter the value for sector {i+1}: "))
            sector_value.append(num)
            remaining = remaining - num

        # The last sector is whatever is left of the total
        sector_label.append(input(f"Enter the label of sector {num_sector}: "))
        sector_value.append(remaining) 

        # chart's title
        setFont(font_name,18,"bold")
        text(center_x,pie_top/2,chart_name)

        # drawing the pie chart
        start_angle = 90
        for i in range(num_sector):
            sector_angle = (sector_value[i]/total)*360
            setFill(chart_colors[i])
            pieSlice(pie_left,pie_top,diameter,diameter,start_angle,sector_angle)
            start_angle += sector_angle

        # drawing the legend
        legend_x = pie_right + 30
        legend_top = center_y - 80
        box_size = 20
        for i in range(num_sector):
            box_x = legend_x
            box_y = legend_top + i*30
            setFill(chart_colors[i])
            rect(box_x,box_y,box_size,box_size)

            label_x = legend_x + box_size + 15
            label_y = box_y + box_size/2
            setFont(font_name,10,"bold")
            text(label_x,label_y,sector_label[i],"w")
        
        break
    elif "bar" in chart_type:
        bar_max = 400
        margin = 100
        # position of the chart
        chart_left = margin
        chart_right = 800 - margin 
        chart_top = margin
        chart_bottom = 600 - margin

        # asking for chart's information
        chart_name = input("Enter the title of the chart: ")
        no_bar = int(input("Enter the number of bars (2 to 6): "))
        y_axis = input("Enter the label for the y-axis: ")
        grid_interval = int(input("Enter the grid interval for y-axis(10 to 100): "))

        bar_name = []
        bar_num = []
        
        for i in range (no_bar):
            name = input(f"Enter the label for bar {i+1}: ")
            bar_name.append(name)
            num = float(input(f"Enter the value for bar {i+1}: "))
            bar_num.append(num)
            bar_space = 600/(no_bar*2)

        # x-axis and y-axis
        line(chart_left,chart_top,chart_left,chart_bottom) #x
        line(chart_left,chart_bottom,chart_right,chart_bottom) #y

        # chart title and y-axis label
        setFont(font_name,18,"bold")
        text((chart_right+chart_left)/2,chart_top-20,chart_name,"s")
        text(chart_left-5,(chart_bottom+chart_top)/2,y_axis,"e")

        # drawing bars and their labels
        for i in range (no_bar):
            bar_height = bar_num[i]
            bar_left = chart_left+(bar_space/2 + ( 2*(i+1) - 2)*bar_space)
            bar_width = bar_space
            bar_top = chart_bottom - bar_height

            setFill(chart_colors[i])
            rect(bar_left,chart_bottom - bar_height,bar_width,bar_height)
            text(bar_left + bar_width/2,bar_top - 10,bar_height,"c")
            text(bar_left + bar_width/2,chart_bottom + 10,bar_name[i],"c")

        # drawing horizontal gridlines and the corresponding gridline values
        for grid_value in range (grid_interval,bar_max+1,grid_interval,):
            setFont("light gray",12)
            text(chart_right+5,chart_bottom-grid_value,grid_value,"w")

        break
    else:
        print("Type of chart is not valid, please try again!")
