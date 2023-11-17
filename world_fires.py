from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract lat, lon, brightness
lats, lons, brights = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])


    lats.append(lat)
    lons.append(lon)
    brights.append(bright)

# Plot brightnesses on a world map.
title = "Global wildfire activity"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights,
                     color_continuous_scale='YlOrRd',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     )

fig.show()