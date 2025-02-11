<!-- Overview
This project integrates Blender with a Flask server to control and manage 3D object transformations (position, rotation, scale) through a custom Blender plugin. The plugin communicates with the server to send object data, enabling real-time updates and control.



📦 DDC_Project
 ┣ 📂 blender_plugin  (Blender Plugin)
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 dcc_plugin.py
 ┃ ┣ 📜 operator.py
 ┃ ┣ 📜 panel.py
 ┃ ┣ 📜 utils.py
 ┣ 📂 server  (Flask Server + Database)
 ┃ ┣ 📜 server.py
 ┃ ┣ 📜 database.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 utils.py
 ┃ ┣ 📜 inventory.db
 ┃ ┣ 📜 ui.py



blender_plugin
The blender_plugin folder contains the Blender plugin files that allow interaction with Blender's 3D objects. This includes:

operator.py: Contains the functions for transforming objects and sending data to the Flask server.
panel.py: Creates a custom panel in Blender's UI for controlling the object transformations.
dcc_plugin.py: Core plugin functionality for managing the Blender operations.
utils.py: Helper functions to facilitate operations in Blender.
server
The server folder houses the Flask server files and database management:

server.py: Flask app that handles communication between the Blender plugin and the database.
database.py: Interacts with the SQLite database to store and retrieve data.
models.py: Defines the database models for storing object transformations and inventory information.
inventory.db: The SQLite database used for tracking transformations and inventory.
ui.py: User interface components for managing inventory data on the server side.
Features
Blender Plugin: Allows users to select and transform objects (position, rotation, scale) within Blender.
Server Communication: Sends object transformation data to the Flask server for processing and storage.
Database Integration: Stores object transformation data in an SQLite database.
Inventory Management: Manage and update the inventory of objects through the server.
Real-time Updates: Updates from Blender are reflected in the server in real time, ensuring accurate data management.
Installation
Prerequisites
Blender (version 4.3 or later)
Python (for running the Flask server)
Flask (for the server)
SQLite (for database management)
Blender Plugin Installation
Download the plugin: Download the blender_plugin folder.
Install the plugin:
Open Blender and go to Edit → Preferences → Add-ons.
Click Install and select the blender_plugin.zip file (or just the folder).
Enable the addon by checking the checkbox next to Flask Connector.
Press Save Preferences to save the addon.
Flask Server Installation
Install required Python dependencies:
bash
Copy
Edit
pip install flask
Run the Flask server:
bash
Copy
Edit
python server/server.py
Usage
In Blender:

Open the Blender scene and press N to open the N-panel.
You should see the Flask Connector panel with options for selecting and transforming objects.
Choose an object and modify its transform properties (Location, Rotation, Scale).
Click the Submit button to send the transformation data to the Flask server.
On the Server:

The Flask server will receive the object transformation data from Blender and store it in the inventory.db SQLite database.
You can query or manage the inventory from the server side.
Troubleshooting
If the Flask Connector panel does not show up in Blender, ensure the plugin is enabled in the Preferences tab.
If the server does not respond, ensure it is running properly and check the console for errors.
License
This project is open-source and distributed under the MIT License.

Feel free to modify this based on the specific details of your project! -->