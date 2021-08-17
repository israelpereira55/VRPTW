import numpy as np
import math


class Solution:   
    #routes 
    #demands
    #routed_clients


    def __init__(self, number_of_clients):
        self.routes = []
        #self.demands = []
        self.free_capacities = []
        self.routed_clients = [0] * number_of_clients
        self.number_of_clients = number_of_clients


    def insert_route(self, route, vrptw_instance):
        self.routes.append(route)

        demand = 0
        for i in range(len(route)):
            demand += vrptw_instance.demands[route[i]]

        #self.demands.append(demand)
        self.free_capacities.append(vrptw_instance.vehicle_capacity - demand)

    def get_route_bland_string(self, route_index):
        route = self.routes[route_index]

        string = str(route[0])
        for client in range(1, len(route)):
            string += " - " + str(route[client])

        return string


    def print_solution(self, vrptw_instance):
        route_distance = 0
        sum_route_distances = 0
        for i in range(len(self.routes)):
            route = self.routes[i]

            print("ROUTE #{}:".format(i))
            string = str(route[0])
            for j in range(1, len(route)):
                string += " - " + str(route[j])
                route_distance += vrptw_instance.distances[j-1][j]

            sum_route_distances += route_distance
            print(string, "  Travelled distance: {}, Demand: {}, Free: {}".format(round(route_distance,2), vrptw_instance.vehicle_capacity - self.free_capacities[i], self.free_capacities[i]))
        print("\nTotal travelled distance:", round(sum_route_distances,2))


    def tuple_clients_allowed_demand(self, vrptw_instance, tuple_clients, route_index):
        #check demands

        route = self.routes[route_index] 
        free_capacity = self.free_capacities[route_index] 

        for i in range(len(tuple_clients)):
            client = tuple_clients[i][0]

            if vrptw_instance.demands[client] > free_capacity: #Demand restriction
                tuple_clients.pop(i)

        return tuple_clients

    #ej : TW earliest earliest time of service of client j
    #bi : initiation time service of client i
    #si : service time of client i
    #tij: travel time from i to j
    def calculate_starting_time(self,vrptw_instance, i, bi, j, route_index): #bj-*********************
        route = self.routes[route_index]
        ej = vrptw_instance.time_windows[j][0]
        #bi = route_starting_times[i]
        si = vrptw_instance.services[i]
        tij = vrptw_instance.travel_times[i][j]
        return max(ej, bi+si+tij)


    def get_route_starting_time(self, vrptw_instance, route_index):
        route = self.routes[route_index]
        route_size = len(route)

        route_starting_times = np.zeros((self.number_of_clients))

        for index in range(1, route_size -1): #depot removed
            i = route[index -1]
            j = route[index]

            bi = route_starting_times[i]
            route_starting_times[j] = self.calculate_starting_time(vrptw_instance, i, bi, j, route_index) #bj

        return route_starting_times