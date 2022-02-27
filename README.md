# PPL-Mini-Project
Umgrage is a web application, which calculates percent vegetation cover of a particular area and keeps historic track of the calculations.

Umbrage word stands for shade or shadow cast by trees. This name is chosen as the application keeps track of green cover at a particular geographic location. 
Application allows user to select the location using Google Map and then uses OpenCV image processing functions to find the green ( forest) cover.

Applicaiton is developed using python and uses Python-Flask web framework to make it an web application. SQLite3 database is used to store the location details and the history of calculations done to determine green cover.

When user selects a location using Google Map, the locations details ( lattitude, longitude and zoom factor) are used to download the satellite image using Google Map APIs. This image is then processed using OpenCV functions to determing the area covered in green color. 



