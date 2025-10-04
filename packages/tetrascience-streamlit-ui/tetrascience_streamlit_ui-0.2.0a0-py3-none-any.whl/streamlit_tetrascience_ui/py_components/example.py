import streamlit as st
from my_component import my_component
from histogram_component import HistogramComponent

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
# name_input = st.text_input("Enter something via Streamlit and see it work with React?", value="Streamlit")
# num_clicks = my_component(name_input, key="foo")
# st.markdown("From the component: You've clicked %s times!" % int(num_clicks))

HistogramComponent(name="Histogram Component", key="foo")
