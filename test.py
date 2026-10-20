# Name (ID): <Your Name> (<Your ID>)
# Tutorial: <Your Tutorial Number>
# <Your Name> did about 100% of the work.

# This program asks the user whether they want a pie chart or a bar chart,
# reads the information needed for that chart, and draws it with SimpleGraphics.

from SimpleGraphics import *

# Text settings
FONT_NAME = "Arial"
TITLE_FONT_SIZE = "20"
TEXT_FONT_SIZE = "12"
TEXT_GAP = 15

# Colours as (red, green, blue). Sector or bar i uses colour i, so no two match.
CHART_COLOURS = [(231, 76, 60), (52, 152, 219), (46, 204, 113),
                 (241, 196, 15), (155, 89, 182), (230, 126, 34)]
OUTLINE_COLOUR = "black"
GRID_COLOUR = "light gray"

# Pie chart layout
PIE_DIAMETER = 320
PIE_TITLE_GAP = 40
FIRST_SECTOR_ANGLE = 90
LEGEND_BOX_SIZE = 20
LEGEND_SPACING = 30
LEGEND_GAP = 30

# Bar chart layout
MARGIN = 100
MAX_BAR_VALUE = 400
BAR_WIDTH_FRACTION = 0.5

# Black is used for all outlines and text, except the gridlines
setOutline(OUTLINE_COLOUR)

# Get the chart type and the title (the same question for both charts)
chart_type = input("Enter the chart type (pie or bar): ").lower()
title = input("Enter the title of the chart: ")

if "pie" in chart_type:
    # Get the information for the pie chart
    num_sectors = int(input("Enter the number of sectors (2 to 6): "))
    total = float(input("Enter the total value of the pie chart: "))

    labels = []
    values = []
    remaining = total
    for i in range(num_sectors - 1):
        labels.append(input(f"Enter the label of sector {i + 1}: "))
        value = float(input(f"Enter the value of sector {i + 1}: "))
        values.append(value)
        remaining -= value

    # The last sector is whatever is left of the total
    labels.append(input(f"Enter the label of sector {num_sectors}: "))
    values.append(remaining)

    # Put the pie in the centre of the window
    centre_x = getWidth() / 2
    centre_y = getHeight() / 2
    pie_left = centre_x - PIE_DIAMETER / 2
    pie_top = centre_y - PIE_DIAMETER / 2

    # Draw the title, centred above the pie
    setFont(FONT_NAME, TITLE_FONT_SIZE, "bold")
    text(centre_x, pie_top - PIE_TITLE_GAP, title)
    setFont(FONT_NAME, TEXT_FONT_SIZE)

    # Draw one sector per value, working around the pie from the top
    start_angle = FIRST_SECTOR_ANGLE
    for i in range(num_sectors):
        sector_angle = values[i] / total * 360
        setFill(*CHART_COLOURS[i])
        pieSlice(pie_left, pie_top, PIE_DIAMETER, PIE_DIAMETER,
                 start_angle, sector_angle)
        start_angle += sector_angle

    # Draw the legend to the right of the pie, centred vertically
    legend_x = pie_left + PIE_DIAMETER + LEGEND_GAP
    legend_top = centre_y - num_sectors * LEGEND_SPACING / 2
    for i in range(num_sectors):
        box_y = legend_top + i * LEGEND_SPACING
        setFill(*CHART_COLOURS[i])
        rect(legend_x, box_y, LEGEND_BOX_SIZE, LEGEND_BOX_SIZE)

        label_x = legend_x + LEGEND_BOX_SIZE + TEXT_GAP
        label_y = box_y + LEGEND_BOX_SIZE / 2
        text(label_x, label_y, labels[i], "w")

else:
    # Get the information for the bar chart
    num_bars = int(input("Enter the number of bars (2 to 6): "))
    grid_interval = int(input("Enter the horizontal gridline interval (10 to 100): "))
    y_label = input("Enter the label for the y-axis: ")

    labels = []
    values = []
    for i in range(num_bars):
        labels.append(input(f"Enter the label of bar {i + 1}: "))
        value = float(input(f"Enter the value of bar {i + 1}: "))
        values.append(value)

    # Work out where the chart goes, leaving a margin around it
    chart_left = MARGIN
    chart_right = getWidth() - MARGIN
    chart_top = MARGIN
    chart_bottom = getHeight() - MARGIN
    chart_centre = (chart_left + chart_right) / 2
    pixels_per_unit = (chart_bottom - chart_top) / MAX_BAR_VALUE

    # Draw the title, centred above the chart
    setFont(FONT_NAME, TITLE_FONT_SIZE, "bold")
    text(chart_centre, chart_top / 2, title)
    setFont(FONT_NAME, TEXT_FONT_SIZE)

    # Draw the gridlines, with their values on the right side of the chart
    for grid_value in range(grid_interval, MAX_BAR_VALUE + 1, grid_interval):
        grid_y = chart_bottom - grid_value * pixels_per_unit
        setOutline(GRID_COLOUR)
        line(chart_left, grid_y, chart_right, grid_y)
        setOutline(OUTLINE_COLOUR)
        text(chart_right + TEXT_GAP, grid_y, str(grid_value), "w")

    # Spread the bars evenly: each bar is centred in its own slot of the x-axis
    slot_width = (chart_right - chart_left) / num_bars
    bar_width = slot_width * BAR_WIDTH_FRACTION

    # Draw each bar with its value above it and its label below the x-axis
    for i in range(num_bars):
        bar_height = values[i] * pixels_per_unit
        bar_left = chart_left + i * slot_width + (slot_width - bar_width) / 2
        bar_top = chart_bottom - bar_height
        bar_centre = bar_left + bar_width / 2

        setFill(*CHART_COLOURS[i])
        rect(bar_left, bar_top, bar_width, bar_height)
        text(bar_centre, bar_top - TEXT_GAP, f"{values[i]:g}")
        text(bar_centre, chart_bottom + TEXT_GAP, labels[i])

    # Draw the y-axis and x-axis as one line. The y-axis label goes in the left
    # margin, centred vertically, with one word per line so long labels fit.
    line(chart_left, chart_top, chart_left, chart_bottom,
         chart_right, chart_bottom)
    text(chart_left / 2, (chart_top + chart_bottom) / 2,
         y_label.replace(" ", "\n"))