def search(query, ranking = lambda r: r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key = ranking)

class Restaurant:
    all = []
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        Restaurant.all.append(self)

    def similar(self, k, similarity):
        others = Restaurant.all.remove(self)
        return sorted(others, key=lambda r: -similarity(r, self))[:k]

    def __repr__(self):
        return '<' + self.name + '>'

Restaurant('Thai Delight', 2)
Restaurant('Thai Basil', 3)
Restaurant('Top Dog', 5)

results = search('Thai')
for r in results:
    print(r, 'is similar to', r.similar(2))

