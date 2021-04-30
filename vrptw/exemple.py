from vrptw import VRPTW

def create_renatos_example():
	vrptw_example = VRPTW(number_of_clients=5 +1)#depot


	vrptw_example.distances = [ [ 0,28,31,20,25,34],
								[28, 0,21,29,26,20],
								[31,21, 0,38,20,32],
								[20,29,38, 0,30,27],
								[25,26,20,30, 0,25],
								[34,20,32,27,25, 0]
							  ]

	vrptw_example.time_windows = [ [0,0],
								   [2,5],
								   [4,6],
								   [2,3],
								   [5,8],
								   [0,3]
								 ]

	vrptw_example.travel_times = [ [ 0, 2, 3, 1, 2, 3],
								   [ 2, 0, 1, 2, 2, 1],
								   [ 3, 2, 0, 4, 1, 3],
								   [ 1, 2, 4, 0, 3, 2],
								   [ 2, 2, 1, 3, 0, 2],
								   [ 3, 1, 3, 2, 2, 0]
								 ]

	vrptw_example.services = [0, 3, 2, 4, 1, 4]
	vrptw_example.demands =  [ 0,37,35,30,25,32]

	vrptw_example.number_of_vehicles = 25
	vrptw_example.vehicle_capacity = 100

	return vrptw_example