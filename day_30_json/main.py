try :
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open ("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} That key does not exists.")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    raise KeyError ("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3 :
    raise ValueError ("Human height should not be over 3 meters")
bmi = weight/ height * height
print(bmi) 

