# Import
from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource

from bokeh.models.tools import HoverTool

from bokeh.palettes import Blues8
from bokeh.transform import factor_cmap

import pandas as pd

# Data
df = pd.read_csv('cars.csv')

# Create a ColumnDataSource from DataFrame
source = ColumnDataSource(df)

# Output File
output_file('index.html')

# Car List
car_list = source.data['Car'].tolist()

# Add Plot
p = figure(
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    title="Cars with Top Horsepower",
    x_axis_label="Horsepower",
    tools="pan, box_select, zoom_in, zoom_out, reset, save"
)

# Render Glyph
p.hbar(
    source=source,
    legend='Car',
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car',
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9 
)

# Add Legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'


# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>Horsepower: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200" /</div>
    </div>
"""

p.add_tools(hover)

# Show
show(p)