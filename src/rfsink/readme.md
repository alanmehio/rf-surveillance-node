# This is an overview on how rfsink is working

## Folders

The work is separated into folder:
1-database folder:
This folder is responsible for the modules that query the database. It contains the files:
    1- database_query.py: This file contains the databasemanager class which queries the database using the method search_power_frequency() and returns the result.

2-widgets folder:
This folder contains all the different widgets that will be added into the main window later. It contains the files:
    1- search_layout.py: This module creates the widget for the search box at the top of the main window.

we create different widgets now here and easily add them to the main window later.

3-windows folder:
This folder contains the different windows of our application. It contains the files:
    1- main_window.py: which is the main app gui, it contains the search box currently at the top.
    2- query_result_window.py: which is the window that pops up when you press search. It will contain your result in a clean table view.

I separated them, and made the result pop up in a different window. This way our main gui is much cleaner and not crammed with results.
And the user gets a beautiful clean window for the result.

## main

In the main.py, I added an arg parser for the "--version" . This way rfsink --version will give the user the current version of our application.
And called the main_window class to create our main gui.


