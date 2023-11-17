from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather_data(path, date_index, high_index, low_index):
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates, and high and low temperatures.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


# Get weather data for Sitka.
sitka_path = Path('weather_data/sitka_weather_2021_simple.csv')
sitka_dates, sitka_highs, sitka_lows = get_weather_data(sitka_path, date_index=2, high_index=4, low_index=5)

# Get weather data for Death Valley.
death_valley_path = Path('weather_data/death_valley_2021_simple.csv')
death_valley_dates, death_valley_highs, death_valley_lows = get_weather_data(death_valley_path, date_index=2,
                                                                             high_index=3, low_index=4)

# Get weather data for San Francisco.
san_francisco_path = Path('weather_data/san_francisco.csv')
sf_dates, sf_highs, sf_lows = get_weather_data(san_francisco_path, date_index=5, high_index=9, low_index=10)

# Plot the high and low temperatures for all three locations.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, color='red', alpha=0.6, label='Sitka, AK - High')
ax.plot(sitka_dates, sitka_lows, color='blue', alpha=0.6, label='Sitka, AK - Low')
ax.plot(death_valley_dates, death_valley_highs, color='orange', alpha=0.6, label='Death Valley, CA - High')
ax.plot(death_valley_dates, death_valley_lows, color='purple', alpha=0.6, label='Death Valley, CA - Low')
ax.plot(sf_dates, sf_highs, color='green', alpha=0.6, label='San Francisco, CA - High')
ax.plot(sf_dates, sf_lows, color='yellow', alpha=0.6, label='San Francisco, CA - Low')

# Format plot.
title = "Daily High and Low Temperatures, 2021\nSitka, AK, Death Valley, CA, and San Francisco, CA"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(10, 140)
ax.legend(loc='upper left')

plt.show()
