import plotly.express as px

# Load built-in Gapminder dataset
df = px.data.gapminder()

# Create an interactive scatter plot with a slider for years
fig = px.scatter(
    df, 
    x="gdpPercap", 
    y="lifeExp", 
    animation_frame="year", 
    animation_group="country",
    size="pop", 
    color="continent", 
    hover_name="country",
    log_x=True, 
    size_max=55, 
    range_y=[25, 90],
    title="<b>Economic Growth vs. Life Expectancy (Interactive Demo)</b>"
)

# Show the interactive figure in your browser or notebook
fig.show()