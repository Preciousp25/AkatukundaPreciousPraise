#score = int(input("Please enter the student's score: "))
#if score >= 90:
    #print(" A")
    #message = "Excellent"
#elif score >= 80:
    #print(" B")
    #message = "Good"
#elif score >= 70:
    #print(" C")
    #message = "Satisfactory"
#   elif score >= 60:
    #print(" D")
    #message = "You need to work harder"
#else:
   # print(" F")
   # message = "Failed"
#print(f"The student's score is: {score}")
#print(message)


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