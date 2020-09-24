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
skyroute()
test = set_start_and_end(None, None)
print(test)
