from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, rainfall_data = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[3])
    except ValueError:
        rainfall = 0.0
    dates.append(current_date)
    rainfall_data.append(rainfall)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall_data, color='blue')

# Format plot.
ax.set_title("Daily Rainfall Amount, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall Amount (inches)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()