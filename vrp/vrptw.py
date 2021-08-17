import numpy as np
import math

import geometry

class VRPTW:
    #coordinates   [x,y]   
    #distances      dij     distance matrix
    #time_windows  [ei, li] earliest time of service, latest time of service 
    #services      [si]     service time 
    #demands       [?] 

    vehicle_capacity : int
    number_of_vehicles : int
    number_of_clients : int

    is_initiated = False

    def __init__(self, number_of_clients):
        self.coordinates = np.zeros((number_of_clients,2))
        self.distances = np.zeros((number_of_clients, number_of_clients))
        self.time_windows = np.zeros((number_of_clients,2))
        self.services = np.zeros((number_of_clients))
        self.demands = np.zeros((number_of_clients))

        self.number_of_clients = number_of_clients
        self.number_of_vehicles = 0
        self.vehicle_capacity = 0


    def read_instance(self, instance_file):
        try:
            file = open(instance_file)
            lines =  file.readlines()[4:]
            file.close()
        except IOError:
            print("[ERROR]: Could not open the {} file.".format(instance_file))
            exit(1)


        self.number_of_vehicles, self.vehicle_capacity = (int(x) for x in lines[0].split())

        for i in range(self.number_of_clients):
            line = lines[5 + i]

            #print(line[:len(line) -1])
            client_id, x, y, demand, ready_time, due_date, service = [int(x) for x in line.split()]

            self.coordinates[i] = x,y
            self.time_windows[i] = ready_time, due_date
            self.services[i] = service
            self.demands[i] = demand

        self.travel_times = self.distances = geometry.distances.calculate_distance_matrix(self.coordinates)

    def print_instance(self):
        print("=================================== VRPTW INSTANCE ========================================")

        print("ID\tX\tY\tDEMAND\t\tREADY TIME\tDUE DATE\tSERVICE\tTRAVEL TIME")
        for i in range(self.number_of_clients):
            client_id, x, y, demand, ready_time, due_date, service = i, self.coordinates[i][0], self.coordinates[i][1], self.demands[i], self.time_windows[i][0], self.time_windows[i][1], self.services[i]
            print("{}\t{}\t{}\t{}\t\t{}\t\t{}\t\t{}".format(client_id, x, y, demand, ready_time, due_date, service))
        print("===========================================================================================")



        print("\n  DISTANCE MATRIX ({}x{})". format(len(self.distances), len(self.distances[0])) )
        for i in range(self.number_of_clients):
            print(self.distances[i])

        print("\n  TRAVEL TIMES ({}x{})". format(len(self.distances), len(self.distances[0])) )
        for i in range(self.number_of_clients):
            print(self.travel_times[i])

        print("\n  TIME WINDOWS")
        print(self.time_windows)

        print("\n  SERVICE")
        print(self.services, "\n")
