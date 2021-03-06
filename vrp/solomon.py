import numpy as np

from vrp import Solution

from operator import itemgetter #to get max in a tuple, stackoverflow says its faster than lambda and pure python, see bellow and check someday 
# https://stackoverflow.com/questions/13145368/find-the-maximum-value-in-a-list-of-tuples-in-python


# mudar para vetor ordenado
def create_route_farthest_clienter(vrptw_instance, ordered_tuple):
    client = ordered_tuple.pop(0)
    route = [0] * 3
    route[1] = client[0]
    return route


'''    EXAMPLE:
    distances = [0, -1, 3, 2]xz
    ordered_indexers = np.argsort(distances) = ([1, 0, 3, 2])
    ordered_clients_distance = []
'''
def create_tuple_ordered_clients_by_distance(vrptw_instance):
    tuple_clients = [[0,0]] * (vrptw_instance.number_of_clients -1) #depot
    for i in range(1, vrptw_instance.number_of_clients):
        tuple_clients[i -1] = i, vrptw_instance.distances[0][i]

    
    ordered_tuple = sorted(tuple_clients, key=lambda tup: tup[1], reverse = True)
    return tuple_clients, ordered_tuple


def calculate_c11(vrptw_instance, i, u, j, mu):
    return vrptw_instance.distances[i][u] + vrptw_instance.distances[u][j] - mu * vrptw_instance.distances[i][j]


def insertion_heuristic(vrptw_instance, alpha1=0.5, alpha2=0.5, mu=1, lambdaa=1, debug=False, debug_level2=False):
    if debug: 
        print("=========== SOLOMON INSERTION HEURISTIC ==============\n\n",
              "Entry Parameters: alpha1 = {}, alpha2 = {}\n".format(alpha1, alpha2),
              "                  mu = {}, lambda = {}\n\n".format(mu, lambdaa))

    solution = Solution(vrptw_instance.number_of_clients)

    route_index = 0
    #tuple_clients, ordered_tuple = create_tuple_ordered_clients_by_distance(vrptw_instance)
    _, ordered_tuple = create_tuple_ordered_clients_by_distance(vrptw_instance)
    
    #Do while, I miss you </3
    route = create_route_farthest_clienter(vrptw_instance, ordered_tuple) #it will remove the first element from ordered tuple
    solution.insert_route(route, vrptw_instance)
    if debug: 
        route_string = solution.get_route_bland_string(route_index)
        print("[SEED]: New Route ", route_string, "\n")

    while len(ordered_tuple) > 0:
        route = solution.routes[route_index] #not necessary, actually
        route_starting_times = solution.get_route_starting_time(vrptw_instance, route_index)
        if debug_level2: print("STARTING TIMES: ", route_starting_times)


        c1_list = []
        #Ordered tuple of clients corrected by demand
        corrected_tuple = solution.tuple_clients_allowed_demand(vrptw_instance, ordered_tuple, route_index)
        for u_index in range(len(corrected_tuple)):
            u = corrected_tuple[u_index][0]

            if debug_level2: print("  * Checking Client {} on route {}.".format(u, route_index))

            lowest_c1 = (10000, -1, -1) #(c1, route_index, u)
            #testing arc (i,u,j)
            for current_route_index in range(1, len(route)):
                i = route[current_route_index -1]
                j = route[current_route_index]
                if debug_level2: print("     - insertion (i,u,j) = ({},{},{})".format(i,u,j))

                bi = route_starting_times[i]
                bu = solution.calculate_starting_time(vrptw_instance, i, bi, u, route_index)

                if debug_level2: print("       bu lu", bu, vrptw_instance.time_windows[u][1])
                if bu > vrptw_instance.time_windows[u][1]:
                    if debug_level2: print("       infeasible: bu > lu.\n")
                    continue

                #Calculating Push Foward. Look for Lemma 1.1 on Solomon articles.
                bju = solution.calculate_starting_time(vrptw_instance, u, bu, j, route_index)
                #bj = solution.calculate_starting_time(vrptw_instance, i, bi, j, route_index)
                bj = route_starting_times[j]

                PF = bju - bj

                if debug_level2: print("       bju, bj, PF", bju, bj, PF)

                viable = True
                for temp_index in range(current_route_index, len(route)): #not doing for depot
                    j_temp = route[temp_index]

                    if debug_level2: print("         PF: (bj, bj + PF, lj)", route_starting_times[j_temp], route_starting_times[j_temp] + PF, vrptw_instance.time_windows[j_temp][1])
                    if route_starting_times[j_temp] + PF > vrptw_instance.time_windows[j_temp][1]:
                        viable=False
                        if debug_level2: print("         infeasible: bju > lju.\n")
                        break

                if not viable: #goto feelings.
                    continue

                #print("Calculating ({},{},{})\n". format(i,u,j))
                #If it goes here, then the insertion is viable
                c11 = calculate_c11(vrptw_instance, i, u, j, mu)
                c12 = bju - bj #PF, really?

                c1 = alpha1*c11 + alpha2*c12

                if c1 < lowest_c1[0]:
                    lowest_c1 = (c1, current_route_index, u)

            #Here we have already calculated all c1 for u client
            if lowest_c1[1] != -1: #then we have a viable insertion, which has the minimum c1 for the current u client.
                c1_list.append(lowest_c1)

        #Here we have a lisbvv= max{5,2} = 5, viavel [5,8]t of minimum c1 for all viable clients
        if len(c1_list) > 0:
            c2_list = []
            for c1_triple in c1_list:
                u = c1_triple[2]
                c1 = c1_triple[0]

                c2 = lambdaa * vrptw_instance.distances[0][u] - c1
                triple = (c2, c1_triple[1], u)
                c2_list.append(triple)

            #highest_triple = max(c2_list,key=itemgetter(0))
            highest_triple = max(c2_list)

            if debug_level2:
                print("  Route:", solution.routes[route_index])
                print("  C1 List:", c1_list)
                print("  C2 List:", c2_list)
                print("  Selected triple:", highest_triple, "\n")

            optimum_u = highest_triple[2]
            optimum_index = highest_triple[1]

            solution.routes[route_index].insert(optimum_index, optimum_u)

            #linkar indices ordered x corrected tuple pra nao percorrer
            for temp in range(len(ordered_tuple)):
                if ordered_tuple[temp][0] == optimum_u:
                    ordered_tuple.pop(temp)
                    break

            if debug: print("[INSERTION]: {}  (client: {})\n".format(solution.routes[route_index], optimum_u))
        else:

            if debug: print("[INFEASIBLE CLIENT]: Could not find any viable insertion for the current route.\n                     Starting a new route...\n\n")
            route_index += 1

            route = create_route_farthest_clienter(vrptw_instance, ordered_tuple) #it will remove the first element from ordered tuple
            solution.insert_route(route, vrptw_instance)
            if debug: 
                route_string = solution.get_route_bland_string(route_index)
                print("[SEED]: New Route ", route_string, "\n")


    solution.print_solution(vrptw_instance)