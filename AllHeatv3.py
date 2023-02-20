# This is a python script that I've been working on that will accept both LAT/LONG and MGRS Format
# coordinates and then turn out a simple heatmap.


import os
import datetime
import pandas as pd
import folium
from folium.plugins import HeatMap
from mgrs import MGRS
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select either Lat/Long or MGRS format
while True:
    latlong_or_mgrs = input("Enter 'L' for Lat/Long format or 'M' for MGRS format: ")
    if latlong_or_mgrs.lower() == 'l':
        latlong_format = True
        break
    elif latlong_or_mgrs.lower() == 'm':
        latlong_format = False
        break
    else:
        print("Invalid selection. Please enter 'L' or 'M'.")

# A window will appear that will let the user pick a CSV file
root = Tk()
root.withdraw()
csv_path = askopenfilename(filetypes=[("CSV Files", "*.csv")])

# Load the CSV file to pandas DataFrame
df = pd.read_csv(csv_path)

# Convert MGRS coordinates to Lat/Long coordinates, if MGRS is selected
if not latlong_format:
    m = MGRS()
    df[['lat', 'lon']] = pd.DataFrame(df.apply(lambda row: m.toLatLon(row['MGRS']), axis=1).tolist())
    df = df.drop(columns=['MGRS'])

# Generate a heatmap based on the coordinates in the DataFrame
heatmap_map = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=5)
HeatMap(data=df[['lat', 'lon']], radius=10).add_to(heatmap_map)

# Generate a custom filename for the output HTML file
now = datetime.datetime.now()
output_filename = "Heatmap_{}_{}_{}_{}_{}_{}.html".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

# Save the output HTML file to the user's desktop
desktop_path = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
output_path = os.path.join(desktop_path, output_filename)
heatmap_map.save(output_path)

# Display final text prompt in green bold text
print("\033[1m\033[1;32mHeatmap saved to {}\033[0m".format(output_path))

