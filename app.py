import streamlit as st
import json
import os
from pages import home, products, places, settings

# Configure the page
st.set_page_config(
    page_title="Local Explorer",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_data():
    """Load data from data.json file"""
    try:
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                return json.load(f)
        else:
            # Return sample data if file doesn't exist
            return {
                "products": [],
                "places": [],
                "settings": {
                    "app_name": "Local Explorer",
                    "version": "1.0.0"
                }
            }
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return {}

def setup_sidebar():
    """Setup the sidebar navigation"""
    # App title at the top
    st.sidebar.markdown("# 🌐 Local Explorer")
    st.sidebar.markdown("---")
    
    # Navigation menu
    menu_options = {
        "🏠 Home": "Home",
        "🛍️ Products": "Products", 
        "📍 Places": "Places",
        "⚙️ Settings": "Settings"
    }
    
    # Create the selectbox for navigation
    selected = st.sidebar.selectbox(
        "Navigate to:",
        options=list(menu_options.keys()),
        index=0,  # Default to Home
        key="main_nav"
    )
    
    # Add some spacing and info
    st.sidebar.markdown("---")
    st.sidebar.markdown("*Your local marketplace & tourism guide*")
    
    return menu_options[selected]

def main():
    """Main application function"""
    # Load data
    data = load_data()
    
    # Setup sidebar and get selected page
    current_page = setup_sidebar()
    
    # Initialize session state for page navigation if not exists
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    
    # Update session state with current selection
    st.session_state.current_page = current_page
    
    # Route to the appropriate page
    if current_page == "Home":
        home.show_home(data)
    elif current_page == "Products":
        products.show_products(data)
    elif current_page == "Places":
        places.show_places(data)
    elif current_page == "Settings":
        settings.show_settings(data)

if __name__ == "__main__":
    main()