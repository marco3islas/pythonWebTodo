import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if (todo := f"{st.session_state['new_todo']}\n") not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        st.toast("Ya existe esa tarea en la lista!")
    st.session_state["new_todo"] = ""


st.title("Mi App de Tareas")
st.subheader("Bienvenido a la App de Tareas")
st.write("Esta app esta hecha para ayudar a tener una mejor")
st.write("organizacion con tus actividades, tareas y/o pendientes")

for index, todo in enumerate(todos):

    checkbox = st.checkbox(todo)
    if checkbox:
        del todos[index]
        functions.write_todos(todos)
        st.rerun()

st.text_input(label='Escribe tu pendiente', label_visibility="hidden",
              placeholder='Escribe una tarea...', on_change=add_todo,
              key='new_todo')
