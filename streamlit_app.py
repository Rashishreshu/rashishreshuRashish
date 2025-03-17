import streamlit as st

# --- LOGIN SECTION ---

# Initialize login state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Function to handle login
def login(username, password):
    if username == "admin" and password == "password":
        st.session_state.logged_in = True
    else:
        st.error("Invalid username or password")

# Display login form if not logged in
if not st.session_state.logged_in:
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)
    st.stop()  # Stop the app here if not logged in

# --- MAIN CONTENT (AFTER LOGIN) ---

# Custom CSS and Header
st.markdown("""
    <style>
        .custom-header {
            background-color: transparent;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 30px;
            border-radius: 10px;
            margin-top: 0px;
            padding-top: 0px;
        }
    </style>
    <div class="custom-header">
        Customer Review Classifier 🚀
    </div>
""", unsafe_allow_html=True)

# Predefined list of places
places = [
    "Jaipur", "Delhi", "Mumbai", "Chennai", "Kolkata",
    "Hyderabad", "Bangalore", "Ahmedabad", "Pune", "Lucknow"
]

contact_methods = ["Email", "Home phone", "Mobile phone"]

# Initialize session state with default values if not already set
if 'contact_method' not in st.session_state:
    st.session_state.contact_method = contact_methods[0]

if 'current_place' not in st.session_state:
    st.session_state.current_place = places[0]

# Sidebar: Select contact method with session state
contact_method = st.sidebar.selectbox(
    "How would you like to be contacted?",
    contact_methods,
    index=contact_methods.index(st.session_state.contact_method)
)

# Sidebar: Select current place with session state
current_place = st.sidebar.selectbox(
    "Current Place",
    places,
    index=places.index(st.session_state.current_place)
)

# Update session state on selection
st.session_state.contact_method = contact_method
st.session_state.current_place = current_place

# Display selections in the sidebar
st.sidebar.write("### Your Selection:")
st.sidebar.write(f"- **Contact Method:** {st.session_state.contact_method}")
st.sidebar.write(f"- **Current Place:** {st.session_state.current_place}")

# Logout button logic
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.success("You have been logged out!")
    st.stop()  # Stop the script to redirect to the login form
