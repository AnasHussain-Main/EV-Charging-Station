"""
Load Data into the program using Python's Dictionary Structure, 
We load the data in where each key is a node, and each value is a list of tuples relative to the node
"""

graph = {
    'A': [('B', 6), ('F', 5)],
    'B': [('A', 6), ('C', 5), ('F', 8), ('G', 6)],
    'C': [('B', 5), ('D', 7)],
    'D': [('C', 7), ('E', 7), ('I', 12)],
    'E': [('D', 7), ('N', 6)],
    'F': [('A', 5), ('B', 8), ('J', 7)],
    'G': [('B', 6), ('H', 9), ('K', 5)],
    'H': [('G', 9), ('I', 12), ('K', 8), ('L', 7)],
    'I': [('D', 12), ('H', 12), ('M', 10), ('N', 15)],
    'J': [('F', 7), ('O', 7), ('K', 13)],
    'K': [('G', 5), ('H', 8), ('J', 13), ('Q', 11)],
    'L': [('H', 7), ('M', 7), ('P', 7)],
    'M': [('I', 10), ('L', 7), ('N', 9), ('R', 7)],
    'N': [('E', 6), ('I', 15), ('M', 9)],
    'O': [('J', 7), ('S', 9), ('P', 13)],
    'P': [('L', 7), ('O', 13), ('U', 8)],
    'Q': [('K', 11), ('U', 8), ('T', 9)],
    'R': [('M', 7), ('V', 5), ('W', 10)],
    'S': [('O', 9), ('T', 9)],
    'T': [('S', 9), ('Q', 9), ('U', 8)],
    'U': [('P', 8), ('Q', 8), ('T', 8), ('V', 8)],
    'V': [('U', 8), ('R', 5), ('W', 5)],
    'W': [('R', 10), ('V', 5)]
}

#Charging stations are assigned to an array called charging_stations
charging_stations = ['H', 'K', 'Q', 'T']

#import Heapq module 
import heapq

"""
The initial function that Finds the shortest paths from a 
starting node to all other nodes in a weighted graph using Dijkstra's algorithm
"""

def dijkstra(graph, start):

    # Initialize distances from start node to all others as infinity, except the start node itself which is 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue (min heap) to store nodes and their distances from the start node. Initialized with the start node
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the node with the smallest distance from the start node.
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the popped distance is greater than the current recorded distance, skip processing.
        if current_distance > distances[current_node]:
            continue

        # Explore each neighbor of the current node.        
        for neighbor, weight in graph[current_node]:
            # Calculate the distance to the neighbor through the current node.
            distance = current_distance + weight
            
             # If the calculated distance is less than the recorded distance, update the distance and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Return the computed shortest distances from the start node to all other nodes           
    return distances


#Finds the nearest charging station from a starting node in the graph
def nearest_charging_station(graph, start, charging_stations):

    # Calculate the shortest distances from the start node to all other nodes using Dijkstra's algorithm
    distances = dijkstra(graph, start)

    # Initialize variables to keep track of the nearest charging station and its distance from the start node
    nearest_station = None
    min_distance = float('infinity')

    # Initialize variables to keep track of the nearest charging station and its distance from the start node
    for station in charging_stations:
        if distances[station] < min_distance:
            nearest_station = station
            min_distance = distances[station]
    
    # Return the nearest charging station and its distance from the start node
    return nearest_station, min_distance


#Recommends the nearest charging station for each node in the graph
def route_recommendation(graph, charging_stations):

    # Initialize an empty dictionary to store the recommendation for each node
    recommendations = {}

    # Iterate through each node in the graph
    for node in graph.keys():

        # Find the nearest charging station and its distance from the current node
        nearest_station, distance = nearest_charging_station(graph, node, charging_stations)

        # Add the nearest charging station and its distance to the recommendations dictionary
        recommendations[node] = (nearest_station, distance)

    # Return the complete set of recommendations
    return recommendations

# Calls the function and prints out the results
recommendations = route_recommendation(graph, charging_stations)
for node in graph:
    nearest_station, distance = recommendations[node]
    print(f"Node {node}: Shortest charging station is at {nearest_station} with a distance of {distance}")
