from collections import defaultdict

class TravelRoute:
    def _init_(self, tickets, visited_cities):
        self.graph = defaultdict(list)
        self.visited_cities = set(visited_cities)  # Convert to a set for fast lookup
        self.route = []
        
        # Build graph
        for src, dst in tickets:
            self.graph[src].append(dst)
    
    def find_route(self, start_city):
        city = start_city
        while city in self.visited_cities:
            self.route.append(city)
            self.visited_cities.remove(city)
            if city in self.graph:
                for next_city in self.graph[city]:
                    if next_city in self.visited_cities:
                        city = next_city
                        break
        return self.route

# Given train tickets (edges)
tickets = [
    ("Paris", "Skopje"), ("Zurich", "Amsterdam"), ("Prague", "Zurich"),
    ("Barcelona", "Berlin"), ("Kiev", "Prague"), ("Skopje", "Paris"),
    ("Amsterdam", "Barcelona"), ("Berlin", "Kiev"), ("Berlin", "Amsterdam")
]

# Cities visited by the kid
visited_cities = {"Amsterdam", "Kiev", "Zurich", "Prague", "Berlin", "Barcelona"}

# Create the route finder
route_finder = TravelRoute(tickets, visited_cities)

# Find the route starting from Kiev
route = route_finder.find_route("Kiev")

print("Route taken by the kid:", route)