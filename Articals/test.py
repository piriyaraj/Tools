import requests
import json
def getGoogleSuggestion(keyword):
    URL="http://suggestqueries.google.com/complete/search?client=firefox&hl="+str("en")+"&q="+keyword
    headers = {'User-agent':'Mozilla/5.0'}
    response = requests.get(URL, headers=headers) 
    result = json.loads(response.content.decode('utf-8'))
    return result[1]

if "__main__"==__name__:
    print(getGoogleSuggestion("Sri Lanka"))
    # ['sri lanka', 'sri lanka cricket', 'sri lankan airlines', 'sri lanka news', 'sri lanka vs afghanistan', 'sri lanka map', 'sri lanka railway', 'sri lanka insurance', 'sri lanka national cricket team', 'sri lanka power cuts']