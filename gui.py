import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("Data.txt"):
    with open("Data.txt" , 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text('',key="clock")
label = sg.Text("Type a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add",size=15,mouseover_colors='LightBlue2')
exit_button = sg.Button("Exit",mouseover_colors='LightBlue2')
complete_button = sg.Button("Complete",mouseover_colors='LightBlue2')
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45, 12))
edit_button = sg.Button("Edit",mouseover_colors='LightBlue2')
window = sg.Window('To-Do',
                   layout=[[clock],[label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    # event will get the value of 'Add' and value will get {'todo' : 'Buy food'}
    event, value = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b-%d-%Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            if len(value['todo'].strip()) > 0:
                todos.append(value['todo'] + '\n')
            else:
                sg.popup("please write a task", font=("Helvetica", 12))
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo = value['todos'][0]
                new_todo = value['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item", font=("Helvetica", 12))
        case "Complete":
            try:
                todo = value['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item", font=("Helvetica", 12))
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
