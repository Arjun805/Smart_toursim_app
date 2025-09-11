import streamlit as st

def create_card(item, item_type):
    """Create a card component for a product or place"""
    with st.container():
        # Add some styling with custom CSS
        st.markdown("""
        <style>
        .card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background-color: #f9f9f9;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Card container
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Image placeholder (you can replace with actual images later)
        st.image(
            item.get('image', 'https://via.placeholder.com/300x200?text=' + item_type.title()),
            use_column_width=True
        )
        
        # Title
        st.subheader(item.get('name', 'Untitled'))
        
        # Location/Description
        if item_type == 'product':
            location_text = item.get('description', 'No description available')
            if 'price' in item:
                location_text += f" - ${item['price']}"
        else:  # place
            location_text = item.get('address', 'No address available')
        
        st.write(location_text)
        
        # View More button
        if st.button(f"View More", key=f"{item_type}_{item.get('id', 'unknown')}"):
            st.info("Details coming soon")
        
        st.markdown('</div>', unsafe_allow_html=True)

def display_grid(items, title, item_type, cols=3):
    """Display items in a responsive grid"""
    if not items:
        st.write(f"No {title.lower()} available.")
        return
    
    st.subheader(f"📍 {title}")
    
    # Calculate number of rows needed
    rows = len(items) // cols + (1 if len(items) % cols > 0 else 0)
    
    for row in range(rows):
        columns = st.columns(cols)
        for col_idx in range(cols):
            item_idx = row * cols + col_idx
            if item_idx < len(items):
                with columns[col_idx]:
                    create_card(items[item_idx], item_type)

def show_page(data):
    """Display the Home page with products and places in responsive grids"""
    
    # Page header
    st.title("🏠 Welcome Home")
    st.markdown("Discover amazing products and places!")
    
    # Check if data exists
    if not data:
        st.warning("No data loaded. Please add content to data.json.")
        st.markdown("""
        ### Expected data structure:
        ```json
        {
            "products": [
                {
                    "id": 1,
                    "name": "Product Name",
                    "description": "Product description",
                    "price": 99.99,
                    "image": "https://example.com/image.jpg"
                }
            ],
            "places": [
                {
                    "id": 1,
                    "name": "Place Name",
                    "address": "123 Main St, City, State",
                    "image": "https://example.com/place.jpg"
                }
            ]
        }
        ```
        """)
        return
    
    # Get products and places from data
    products = data.get('products', [])
    places = data.get('places', [])
    
    # Display statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Products", len(products))
    with col2:
        st.metric("Total Places", len(places))
    with col3:
        st.metric("Total Items", len(products) + len(places))
    
    st.markdown("---")
    
    # Display products in responsive grid
    if products:
        display_grid(products, "Featured Products", "product", cols=3)
        st.markdown("---")
    
    # Display places in responsive grid
    if places:
        display_grid(places, "Popular Places", "place", cols=3)
    
    # Footer message
    if not products and not places:
        st.info("Add some products and places to data.json to see them displayed here!")
    else:
        st.success(f"Showing {len(products)} products and {len(places)} places")

print(dir())