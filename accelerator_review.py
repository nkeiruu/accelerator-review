import requests
import json

#parameters to pass into Google Custom Search JSON API
parameters = {
    "cx" : "c6e3001bf986f4943",
    "exactTerms" : "particle accelerators"

}

#API request
search_results = requests.get("https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyCyiQ9vR0zdfOOfvKh7NPenIq47CrO45FI", params=parameters)

formatted = json.dumps(search_results.json(), indent=4, sort_keys=True)

search_dict = search_results.json()



# create new dictionary with selcted keys
selected_results = {}

print ("Error code", search_results.status_code)
#print(formatted)

#testing out the loop logic for writing selected info to dictionary

lay1 = search_dict["items"]






#accessing the required info in the search Response object
#i.e. title and link
for i in range(len(lay1)):
    print(lay1[i]["title"])  
    

  











#print(results_dict)