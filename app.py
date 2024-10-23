from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd
import component
from util import get_data # Import the get_data function from util.py

# Load the data from a fixture
PATH = "./fixtures/chipotle.csv"
data = get_data(PATH)

# Print the head to verify the data was loaded correctly
print("-" * 90)
print(data)

# Initialize the main Dash app and apply Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = component.render(app, data)

if __name__ == "__main__":
    app.run_server(debug=True)
