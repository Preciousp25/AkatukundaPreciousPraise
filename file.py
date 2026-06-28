file_path = 'C:/Users/User/OneDrive/Desktop/Hackathon-1/task.py'
with open(file_path, "r") as file_object:
    content = file_object.read()
    print(content)

file_path = 'C:/Users/User/OneDrive/Desktop/Hackathon-1/task5.py'
with open(file_path, "r") as file_object:
    for line in file_object:
        print(line, end="")

