import streamlit as st
import importlib

# ---------- Session State Setup ----------
if "current_app" not in st.session_state:
    st.session_state.current_app = None

def reset_to_dashboard():
    st.session_state.current_app = None

# ---------- Page Config ----------
st.set_page_config(page_title="Operations Dashboard", layout="wide")
st.markdown("""
    <style>
        button {
            height: 100px !important;
            width: 100% !important;
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- App List ----------
APPS = {
    "Stock Order": "stock_order",
    "Part Lookup": "part_lookup",
    "Another Module": "another_module"
}

# ---------- Show App if Selected ----------
if st.session_state.current_app:
    # Top-left return button
    with st.container():
        st.markdown("""
            <div style="position: fixed; top: 10px; left: 10px; z-index: 999;">
                <a href="#" onclick="window.location.reload()" style="text-decoration: none; font-weight: bold;">← Dashboard</a>
            </div>
        """, unsafe_allow_html=True)

    # Load and run selected module
    try:
        module_name = st.session_state.current_app
        app_module = importlib.import_module(f"apps.{module_name}")
        app_module.run()
    except Exception as e:
        st.error(f"Failed to load app: {e}")

# ---------- Show Dashboard if No App Selected ----------
else:
    st.title("📦 Operations Dashboard")
    st.markdown("### Choose an app:")

    # Grid layout for tiles (2 per row)
    cols = st.columns(2)
    for i, (app_label, app_module) in enumerate(APPS.items()):
        col = cols[i % 2]
        with col:
            if st.button(app_label, key=f"button_{app_module}"):
                st.session_state.current_app = app_module
                st.experimental_rerun()
