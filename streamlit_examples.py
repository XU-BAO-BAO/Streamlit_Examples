
# import necessary libraries
import streamlit as st

# Set page configuration
# This sets the page title, icon, and layout
st.set_page_config(page_title="STREAMLIT TEST", page_icon=":guardsman:", layout="wide")

# .streamlit/config.toml
base="dark"
primaryColor="#F63366"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"

# Test page content
st.title("Streamlit Test Page")
st.write("This is a test page for Streamlit.") 
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar content.")
st.button("Click Me", key="test_button")
st.text_input("Enter some text", key="test_input")
st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"], key="test_selectbox")
st.checkbox("Check this box", key="test_checkbox")
st.radio("Select one", ["Choice A", "Choice B", "Choice C"], key="test_radio")
st.slider("Slide to select a value", 0, 100, 50, key="test_slider")
st.text_area("Write something here", key="test_textarea")
st.date_input("Select a date", key="test_date")
st.time_input("Select a time", key="test_time")
st.file_uploader("Upload a file", type=["txt", "pdf"], key="test_file_uploader")
st.color_picker("Pick a color", "#00f900", key="test_color_picker")
st.spinner("Loading...")  # Example of a spinner
st.balloons()  # Example of a fun effect
st.success("This is a success message!")
st.error("This is an error message!")
st.warning("This is a warning message!")
st.info("This is an informational message!")
st.markdown("## Markdown Section")
st.markdown("This is a **bold** text and this is *italic* text.")
st.latex(r"E = mc^2")  # Example of LaTeX rendering
st.json({"key": "value", "number": 42, "list": [1, 2, 3]})  # Example of JSON rendering
st.image("https://via.placeholder.com/150", caption="Placeholder Image")  # Example of an image
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # Example of audio
st.dataframe({"Column 1": [1, 2, 3], "Column 2": ["A", "B", "C"]})  # Example of a dataframe
st.table({"Column 1": [1, 2, 3], "Column 2": ["A", "B", "C"]})  # Example of a table
st.code("print('Hello, Streamlit!')", language='python')  # Example of code rendering
st.markdown("---")  # Horizontal line
st.caption("This is a caption for the page.")
st.sidebar.markdown("### Sidebar Markdown")
st.sidebar.caption("This is a caption for the sidebar.")
st.sidebar.button("Sidebar Button", key="sidebar_button")
st.sidebar.text_input("Sidebar Text Input", key="sidebar_text_input")
st.sidebar.selectbox("Sidebar Selectbox", ["Option A", "Option B"], key="sidebar_selectbox")
st.sidebar.checkbox("Sidebar Checkbox", key="sidebar_checkbox")
st.sidebar.radio("Sidebar Radio", ["Choice X", "Choice Y"], key="sidebar_radio")
st.sidebar.slider("Sidebar Slider", 0, 10, 5, key="sidebar_slider")