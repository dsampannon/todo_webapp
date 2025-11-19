import streamlit as st
import functions

# to start the webapp type in terminal:
# streamlit run web.py


todo_list = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo)
    functions.write_todos(todo_list)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo_item in enumerate(todo_list):
    checkbox =st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state[todo_item]
        st.rerun()


#st.text_input(label="Enter a todo")
st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

#st.session_state