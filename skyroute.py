from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

#concatenate landmark_choices into a string
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{} - {}\n".format(letter, landmark)

def greet():
    print("Hi there, and welcome to SkyRoute!\n We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

#main program
def skyroute():
    greet()
    new_route()
    goodbye()

#Getting and setting functions
def set_start_and_end(start_point, end_point):
    if start_point:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == "b":
            start_point = get_start()
            end_point = get_end()
        elif change_point == "o":
            start_point = get_start()
        elif change_point == "d":
            end_point = get_end
        else:
            print('Oops! Please enter a lowercase "o", "d", or "b"')
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point
def get_start():
    start_point_key = input('Where are you coming from? Type in the corresponding letter: ')
    if start_point_key in landmark_choices.keys():
        start_point = landmark_choices[start_point_key]
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()
    return start_point
def get_end():
    end_point_key = input('Ok, where are you headed? Type in the corresponding letter:')
    if end_point_key in landmark_choices.keys():
        end_point = landmark_choices[end_point_key]
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()
    return end_point

def new_route(start_point = None, end_point = None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    again = input('Would you like to see another route? Enter y/n: ')
    if again == 'y':
        show_landmarks()
        new_route(start_point, end_point)

def show_landmarks():
    see_landmarks = input('Would you like to see the list of landmarks again? Enter y/n')
    if see_landmarks == "y":
        print (landmark_string)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start in start_stations:
        for end in end_stations:
            route = bfs(vc_metro, start, end)
            if route:
                routes.append(route)
    shortest_route = min(routes, key=len)
    return shortest_route
def goodbye():
    print("Thanks for using Skyroute!")

#Function calls
skyroute()
#test = get_route('Cathedral of Our Lady of the Holy Rosary', 'B.C. Place Stadium')
#print(test)
