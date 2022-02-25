import requests

api_key = "AIzaSyAs7QFlJwNS97PQy_ZILj9yfbaM7OX6RmU"

url = "https://maps.googleapis.com/maps/api/staticmap?"

center = "18.444665,73.672504"

zoom = 8

maptype = "satellite"

url2 = url + "center=" + center + "&zoom=" +str(zoom) + "&size=400x400&maptype=satellite&style=feature:poi|element:labels|visibility:off&key=" + api_key + "&sensor=false"

print(url2)
r = requests.get(url2)

# r = requests.get("https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap\
#     &markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318\
# &markers=color:red%7Clabel:C%7C40.718217,-73.998284\
# &key=AIzaSyAs7QFlJwNS97PQy_ZILj9yfbaM7OX6RmU")

# url3 = 

print(r.status_code)
# print(r.text)

file = open("google_img.jpg", "wb")

file.write(r.content)

file.close()

