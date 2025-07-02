import FreeSimpleGUI.window
import Functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=Functions.get_todos(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-do App", 
                   layout=[[label], [input_box, add_button], [list_box, edit_button]], 
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1,event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window['todos'].Update(values=todos)
            
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = Functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            Functions.write_todos(todos)
            window['todos'].Update(values=todos)
        
        case'todos':
            window['todo'].Update(value=values['todos'][0])
        
        case sg.WIN_CLOSED:
            break

window.close()
