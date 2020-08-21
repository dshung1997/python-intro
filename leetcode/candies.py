import math


def distributeCandies(candies, num_people):
    max_num_candy = math.floor(math.sqrt(2 * candies + 0.25) - 0.5)
    dist = [i for i in range(1, max_num_candy + 1)]
    dist.append(candies - max_num_candy * (max_num_candy + 1) // 2)
    dist.extend([0 for i in range(num_people - len(dist) % num_people)])

    print("dist", dist)

    return [sum(dist[x::num_people])
            for x in range(0, num_people)]


print(distributeCandies(10, 3))
