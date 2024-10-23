from dash import html, dcc
import plotly.express as px

def render(app, data):
    # Create a pie chart using Plotly Express
    fig = px.pie(
        data,
        values="order_price",
        names="item_name",
        title="Top 5 Bestsellers",
        color_discrete_sequence=px.colors.sequential.RdBu,  
        hole=0.4,
    )
    
    fig.update_layout(
        title_font_size=20,
        title_x=0.5,  # Center the title
        margin=dict(t=40, b=20, l=0, r=0),  # Adjust margins
        legend_title_text="Best Sellers in order",  
        legend=dict(
            orientation="h",  # Horizontal legend
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
    )
    
    # Inline CSS styling for the component
    return html.Div(
        [
            html.H2("Pie Chart of Foods ", style={"textAlign": "center", "color": "#333", "marginBottom": "18px"}),
            dcc.Graph(figure=fig),  # Insert the pie chart graph here
        ],
        style={
            "padding": "30px",
            "backgroundColor": "#f9f9f9",  
            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",  
            "borderRadius": "10px",  
            "maxWidth": "1000px",
            "margin": "auto"  
        },
        id="pie-chart"
    )