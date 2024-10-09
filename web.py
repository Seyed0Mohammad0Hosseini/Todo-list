import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos = get_todos()
    todos.append(todo_local)
    write_todos(todos)


st.title("My todo app")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        st.session_state["new_todo"] = ""
        write_todos(todos)
        del st.session_state[todo]

        st.rerun()

st.text_input(label="",
              placeholder="Add new todo",
              on_change=add_todo,
              key='new_todo')

