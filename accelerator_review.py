import requests

parameters = {
    "cx" : "c6e3001bf986f4943",
    "exactTerms" : "particle accelerators"

}

response = requests.get("https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyCyiQ9vR0zdfOOfvKh7NPenIq47CrO45FI", params=parameters)
print (response.status_code)
print(response.json())