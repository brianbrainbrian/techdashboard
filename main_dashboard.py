import streamlit as st
import importlib

# Title and layout
st.set_page_config(page_title="Dashboard", layout="centered")
st.title("📦 Operations Dashboard")

# App selection
app_choice = st.selectbox(
    "Choose an app to launch:",
    ("Select...", "Stock Order", "Part Lookup", "Another Module")
)

# Import and run the selected app
if app_choice != "Select...":
    module_name = app_choice.lower().replace(" ", "_")
    try:
        app_module = importlib.import_module(f"apps.{module_name}")
        app_module.run()  # All app files must have a `run()` function
    except ModuleNotFoundError:
        st.error(f"Module apps/{module_name}.py not found.")
    except AttributeError:
        st.error(f"Function `run()` not found in {module_name}.py")
