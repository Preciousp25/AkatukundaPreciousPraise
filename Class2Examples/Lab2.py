 # multiple patterns in one case
Light_color = input("Please enter the traffic light color (red, yellow, green): ")
match Light_color:
    case "red" | "yellow":
        action = "Stop"
    case "green":
        action = "Go"
    case _:
        action = "Invalid traffic light color"
print(action)