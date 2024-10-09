FILEPATH = "Data.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(my_todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(my_todos)


# in this example the print function will execute only when you run the
# functions modules otherwise print won't be executed for instance use
# this modules in other modules (import it)

#__name__ is a hide python variable
if __name__ == "__main__":
    print("python and go are brothers")
