def m_to_rectangle(measures, width, height):
    
    key = list(measures)
    screen = []

    for i in range(height):
        row = []
        for j in range(width):
            row.append(".")
        screen.append(row)

    for i, obdelnik in enumerate(measures):
        if width < measures[obdelnik]["width"] + measures[obdelnik]["left"] or any(measures[obdelnik][x] < 0 for x in measures[obdelnik])\
            or height < measures[obdelnik]["height"] + measures[obdelnik]["top"]:
            print(obdelnik, i, "nemá správnou velikost")
            continue
        for row in screen[measures[obdelnik]["top"]:measures[obdelnik]["top"] + measures[obdelnik]["height"]]:
            for cell in range(measures[obdelnik]["width"]):
                row[measures[obdelnik]["left"] + cell] = str(i)

     rectangle = []
    for row in screen:
        row = "".join(row)
        rectangle.append(row)

    return "\n".join(rectangle)


width1 = 120
height1 = 30
m1 = {
        "console_input": {
            "left": 0,
            "top": 27,
            "width": 120,
            "height": 3
        },
        "fight": {
            "left": 0,
            "top": 0,
            "width": 80,
            "height": 27
        },
        "entities": {
            "left": 80,
            "top": 0,
            "width": 120,
            "height": 9
        },
        "inventory": {
            "left": 80,
            "top": 9,
            "width": 120,
            "height": 9
        },
        "history": {
            "left": 80,
            "top": 18,
            "width": 120,
            "height": 9
        },
        }

print(m_to_rectangle(m1, width1, height1))

"""
        vyskatop = measures[key[0]]["top"]
        vyskaheight = measures[key[0]]["height"]

        rectangle = "\n"
        while vyskatop > 0:
            rectangle += (" " * measures[key[0]]["left"])
            rectangle += "\n"
            vyskatop -= 1

        while vyskaheight > 0:
            rectangle += ("0" * measures[key[0]]["width"])
            rectangle += "\n"
            vyskaheight -= 1
            """

    


