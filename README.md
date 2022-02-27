# PPL-Mini-Project
"Green Canopy" is a web application, which calculates percent vegetation cover of a particular area and keeps historic track of the calculations.

Application allows user to select the location using Google Map and then uses OpenCV image processing functions to find the green ( forest) cover.

Applicaiton is developed using python and uses Python-Flask web framework to make it an web application. SQLite3 database is used to store the location details and the history of calculations done to determine green cover.

When user selects a location using Google Map, the locations details ( lattitude, longitude and zoom factor) are used to download the satellite image using Google Map APIs. This image is then processed using OpenCV functions to determing the area covered in green color. 




Heroku Deployment
1. Create an app in Heroku and link it to the Git repository
2. In Heroku app dashboard , goto settings and add a heroku python buildpack. This tells heroku that its a python application
3. Create requirement.txt file in the root folder of repository. This file contains all the dependent components used by the python code, e.g Flask, Jinja, OpenCV etc
4. Create Procfile in the root folder of repository. This file specifies the command to run the application. 
5. Since web app is in subfolder ( greencanopy), Proc file is modified to change the directory and then run the applicaiton.
6. Heroku uses Gunicorn ( Green Unicorn) as HTTP server to run the application