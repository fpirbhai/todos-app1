import streamlit as st
import functions

todos = functions.read_file()

def add_todo():
    new_todo = st.session_state['inp_addtodo']+'\n'
    todos.append(new_todo)
    functions.update_file(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.update_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    




st.text_input(label = "", placeholder="Add a todo", 
              on_change=add_todo, key = 'inp_addtodo')

print('Running the webpage')

st.session_state