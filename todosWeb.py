import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("Mi App de Tareas")
st.subheader("Bienvenido a la App de Tareas")
st.write("Esta app esta hecha para ayudar a tener una mejor")
st.write("organizacion con tus actividades, tareas y/o pendientes")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Escribe tu pendiente', label_visibility="hidden",
              placeholder='Escribe una tarea...', on_change=add_todo,
              key='new_todo')
