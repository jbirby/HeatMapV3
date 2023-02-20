READ ME, HEATMAPV3.PY

Heatmap Generator
This Python script generates a heatmap visualization of coordinate data in either lat/long or MGRS format using the folium library.
It was written and intended for use on Debian Linux based platforms. I've tested this on UBUNTU and RASPBERIAN.  
I've included some CSV files that have the proper header format and for users to play around with. 

Installation
To use this script, you will need to have Python 3 installed on your computer, as well as the following Python libraries:

pandas
folium
folium.plugins
mgrs
You can install these libraries using pip, the Python package manager, by running the following command:

pip install pandas folium mgrs

Usage
To use this script, follow these steps:

Download the script and save it to your computer.

Open a terminal or command prompt and navigate to the directory where the script is saved.

Run the script by typing the following command and pressing enter:

python3 AllHeatv3.py

The script will prompt you to select either lat/long or MGRS format for your coordinate data. Enter 'L' for lat/long format or 'M' for MGRS format and press enter.

The script will then prompt you to enter the file path and name of the CSV file containing your coordinate data. Enter the file path and name and press enter.

The script will then generate a heatmap visualization of the coordinate data and save it as an HTML file on your desktop. The name of the HTML file will be in the format "Heatmap_yyyy_mm_dd_hh_mm_ss.html".

Once the heatmap has been generated, the script will display a message indicating the path where the HTML file has been saved.

Contributing
If you have suggestions for improving this script, please submit a pull request or open an issue on GitHub.

License
This script is licensed under the MIT License.