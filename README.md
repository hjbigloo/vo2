Virtual Orchard Frontend
===
This repo holds the frontend code for Virtual Orchard. This file introduces the code files as a reference for future developers.

## Architecture

The frontend code is mainly written in Javascript. We use RESTful API to communicate with the backend. Following libraries are used to build the frontend:
* Vue.js - For almost all panels in the frontend.
* Leaflet - The library for wrapping the map services.
* Axios - Frontend-backend communication.
* Bootstrap - CSS for user interfaces. 
* jQuery - Depended by Bootstrap and for the UI parts outside Vue.js
* d3.js - Visualization.

### Code Structure
Following files are most important to the user interfaces:
* index.html - The HTML template of the user interface. It should be directly rendered.
* static/main.js - The entry point of the project. All UI components are initialized and installed to the UI by this script.
* static/vo_core.js - The core abstractions of the Virtual Orchard data structures. The global variable, **VO**, is declared in this file.
* static/vue_components.js - Specific Vue.js components for Virtual Orchard. Reading the tutorials of Vue.js is highly recommended before modifying this file.
* static/dialog_callback.js - On-click handlers for dialogs.

A small backend is also implemented in order to support the basic functions for starting the demo. Flask and sqlite3 are used to build this simple backend.
* main.py: The entry of backend program.
* dataconn.py: Data abstaction for the backend. 
* manage.py: Backend manage program.

## Usage
Before actually run the server, we need to initialize the database. By simply run this command:
<pre>
$ python dataconn.py
</pre>

Then execute the main.py to run server:
<pre>
$ python main.py
</pre>

The server will run a HTTP service at port 9802. Then you can use a browser to open http://127.0.0.1:9802/ 

The only user created by dataconn.py has a username of "admin". The password is also "admin". You can use following manage.py to add new users.

For example, following command will add a new user whose username is "foo" and password is "bar".
<pre>
$ python manage.py add-user foo bar
</pre>

