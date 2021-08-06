import hello
import collections

if __name__ == '__main__':
    result = collections.defaultdict(int)

    s = hello.Robo()
    name = s.sayHello()

    recomends = s.getRecommendsRestaurants()

    if len(recomends) >= 1:
        result = s.recommend(recomends)

    restaurant = s.whichDoYouLike(name)
    result[restaurant] += 1

    s.noteRestaurant(result)
