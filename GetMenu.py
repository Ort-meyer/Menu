import urllib.request
from datetime import datetime
import json 











'''
TODO:
- Send mail
- Run as service in Raspberry Pi
'''

def jprint(jsonText):
    print(json.dumps(jsonText, indent=4, sort_keys=True))

def main():
    desiredFood = []
    desiredFood.append('Caesarsallad')
    desiredFood.append('Köttbullar')
    desiredFood.append('Aids')
    desiredFood.append('citron')




    send_url = 'http://carboncloudrestaurantapi.azurewebsites.net/api/menuscreen/getdataweek?restaurantid=9'

    with urllib.request.urlopen(send_url) as url:
        data = json.loads(url.read().decode())

    # One menu per day
    menus = data['menus']
    for menu in menus:
        date = menu['menuDate']
        date = datetime.strptime( date[:10], '%Y-%M-%d').strftime('%A')
        for meal in menu['recipeCategories']:
            # If no food in the recipe category exists, we continue
            if not meal['recipes']:
                continue
            for name in meal['recipes']:
                displayName = name['displayNames'][0]['displayName']
                for food in desiredFood:
                    if food in displayName:
                        print(date + ":  " + displayName)


        #print('------------------------')


if __name__ == "__main__":
    main()