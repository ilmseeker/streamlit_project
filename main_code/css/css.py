# Define custom CSS for button styling
button_style = """
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50; /* Green */
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stButton.red-button>button {
        background-color: #f44336; /* Red */
    }
    .stButton.red-button>button:hover {
        background-color: #da190b; /* Darker red on hover */
    }
    </style>
    """