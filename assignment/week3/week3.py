# import urllib.request as requestor
# import json
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
# with requestor.urlopen (src) as response:
#     taipeiTravel = json.load (response)
# travelImage=taipeiTravel["result"]["results"]
# print (travelImage)
# # for i in travelImage:
# #     print (i["stitle"]+","+i["longitude"]+","+i["file"]+"\n")


# for i in travelImage:
#     print (i["stitle"]+","+i["longitude"]+","+i["file"]+"\n")
        


# with open ("data.txt","w",encoding="UTF-8") as file:
#     for i in travelImage:
#         file.write(i["stitle"]+","+i["longitude"]+","+i["file"]+"\n")

# -----------------------------------------------------------------------------------------

# ["result"]["results"][0]只有第一筆的資料
# import urllib.request as requestor
# import json
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
# with requestor.urlopen (src) as response:
#     taipeiTravel = json.load (response)
#     title=taipeiTravel["result"]["results"][0]["stitle"]
#     longitude=taipeiTravel["result"]["results"][0]["longitude"]
#     imageFile=taipeiTravel["result"]["results"][0]["file"]
#     splitFile = imageFile.split("http",50)
# print (title,",",longitude,",","http",splitFile[1])

# splitFile = imageFile.split("http",50)
# print (splitFile)
# print ("http",splitFile[1])

# -----------------------------------------------------------------------------------------
# import urllib.request as requestor
# import json
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
# with requestor.urlopen (src) as response:
#     taipeiTravel = json.load (response)
#     travelSpot=taipeiTravel["result"]["results"]
#     length=len(travelSpot)
#     # print(len(travelSpot)) #319
#     i=0
#     for i in range (i, length):
#         title=taipeiTravel["result"]["results"][i]["stitle"]
#         longitude=taipeiTravel["result"]["results"][i]["longitude"]
#         imageFile=taipeiTravel["result"]["results"][i]["file"]
#         splitFile = imageFile.split("http",50)
#         print (title,",",longitude,",","http",splitFile[1])

# -----------------------------------------------------------------------------------------

import urllib.request as requestor
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with requestor.urlopen (src) as response:
    taipeiTravel = json.load (response)
travelSpot=taipeiTravel["result"]["results"]
length=len(travelSpot)
i=0
with open ("data.txt","w",encoding="UTF-8") as file:
     for i in range (i, length):
        title=taipeiTravel["result"]["results"][i]["stitle"]
        longitude=taipeiTravel["result"]["results"][i]["longitude"]
        imageFile=taipeiTravel["result"]["results"][i]["file"]
        splitFile = imageFile.split("http",50)
        file.write(title+","+longitude+","+"http"+splitFile[1]+"\n")




