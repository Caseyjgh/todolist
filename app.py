import streamlit as st

# Apply custom CSS styles
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .stTextInput > div > input {
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .todo-item {
        font-size: 18px;
        padding: 8px 0;
        border-bottom: 1px solid #eee;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1 style='text-align: center;'>📝 My Styled To-Do List</h1>", unsafe_allow_html=True)

# Initialize session state for the to-do list
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# Input form
st.markdown('<div class="main">', unsafe_allow_html=True)
new_item = st.text_input("Add a new task:")
if st.button("Add"):
    if new_item:
        st.session_state.todo_list.append(new_item)
        st.success(f'Added: "{new_item}"')
    else:
        st.warning("Please enter a task.")
st.markdown('</div>', unsafe_allow_html=True)

# Show to-do list
if st.session_state.todo_list:
    st.markdown("### ✅ Current Tasks:")
    for i, item in enumerate(st.session_state.todo_list, 1):
        st.markdown(f"<div class='todo-item'>{i}. {item}</div>", unsafe_allow_html=True)
else:
    st.info("Your to-do list is empty.")
