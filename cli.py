import functions
import time
now = time.strftime("%b-%d-%Y %H:%M:%S")
print("it's the time:"+now)
while True:
    userAction = input("Type add, show, edit, complete or exit: ")
    userAction = userAction.strip()

    if userAction.lower().startswith("add") or userAction.lower().startswith("new"):
        todo = userAction[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif userAction.lower().startswith("show"):
        todos = functions.get_todos()

        newTodos = [item.strip('\n') for item in todos]  # using list comprehension
        for index, item in enumerate(newTodos):
            print(f"{index + 1}. {item}")

    elif userAction.lower().startswith("edit"):
        todos = functions.get_todos()
        try:
            userNumber = int(userAction[5:])
            todos[userNumber - 1] = input("Write new todo text:") + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("your command is invalid!!")
            continue
    elif userAction.lower().startswith("exit"):
        break
    elif userAction.lower().startswith("complete"):
        try:
            todos = functions.get_todos()
            userNumber = int(userAction[9:])
            # we used strip() method because if we don't do that the output will print in 2 lines when we want to
            # print it
            todoToRemoved = todos[userNumber - 1].strip()

            todos.pop(userNumber - 1)
            functions.write_todos(todos)
            print(f"The todo {todoToRemoved} was removed from the list successfully")
        except ValueError:
            print("your command is invalid")
            continue
        except IndexError:
            print("The number is out of range!!")
    else:
        print("Hey, your command is invalid")

print("Bye...")
