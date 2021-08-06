import csv
import collections

class Robo():
    def sayHello(self):
        print('Hello! What youre name')
        name = input()

        return name

    def whichDoYouLike(self, name):
        print(f'{name}. Which restaurant do you like?')
        restaurant = input()

        return restaurant

    def getRecommendsRestaurants(self):
        recomends = collections.defaultdict(int)
        with open('views/text.csv') as f:
            reader = csv.DictReader(f)
            for i in reader:
                recomends[i['NAME']] = int(i['COUNT'])
        return recomends

    def recommend(self, recommendRestaurantsDict):
        for k in recommendRestaurantsDict:
            print(f'I suggest {k}.')
            print('Do you like this?[Y/n]')
            answer = input()
            while True:
                if answer == 'Y' or answer == 'n':
                    break
                answer = input()

            if answer == 'Y':
                recommendRestaurantsDict[k] += 1

        return recommendRestaurantsDict

    def noteRestaurant(self, restaurantName):
        with open('views/text.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['NAME','COUNT'])
            for k in dict(restaurantName):
                writer.writerow([k, restaurantName[k]])
