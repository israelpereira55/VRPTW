from vrp import VRPTW

def create_renatos_example():
	vrptw = VRPTW(number_of_clients=6)

	vrptw.distances = [ [ 0,28,31,20,25,34],
	                                   [28, 0,21,29,26,20],
	                                   [31,21, 0,38,20,32],
	                                   [20,29,38, 0,30,27],
	                                   [25,26,20,30, 0,25],
	                                   [34,20,32,27,25, 0]
	                                 ]

	vrptw.time_windows = [ [0,1000],
	                                    [2,5],
	                                    [4,6],
	                                    [2,3],
	                                    [5,8],
	                                    [0,3]
	                                  ]

	vrptw.travel_times = [ [ 0, 2, 3, 1, 2, 3],
	                                  [ 2, 0, 1, 2, 2, 1],
	                                  [ 3, 2, 0, 4, 1, 3],
	                                  [ 1, 2, 4, 0, 3, 2],
	                                  [ 2, 2, 1, 3, 0, 2],
	                                  [ 3, 1, 3, 2, 2, 0]
	                                ]

	vrptw.services = [0, 3, 2, 4, 1, 4]
	vrptw.demands =  [ 0,37,35,30,25,32]

	vrptw.number_of_vehicles = 25
	vrptw.vehicle_capacity = 100
	return vrptw