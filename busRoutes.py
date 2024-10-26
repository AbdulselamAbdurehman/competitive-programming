class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Build a graph of bus stops to bus routes
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for bus_stop in route:
                graph[bus_stop].append(i)

        queue = deque([(source, 0)]) 
        visited_stops = set([source]) 
        visited_routes = [False] * len(routes)  

        while queue:
            curr_stop, buses = queue.popleft()

            if curr_stop == target:
                return buses

            for route_index in graph[curr_stop]:
                if visited_routes[route_index]:
                    continue
                visited_routes[route_index] = True 

                for stop in routes[route_index]:
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses + 1))

        return -1
