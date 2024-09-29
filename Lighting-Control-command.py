# Lighting condition app

lobby = {
    "up right": False,
    "down right": False,
    "up left": False,
    "down left": False
}

wc = {
    "door": False,
    "men": False,
    "women": False
}

secretary = {
    "desk": False,
    "back": False
}

locations_str = ["lobby", "wc", "secretary"]
locations = [lobby, wc, secretary]

# red zone

input_message = "\033[0m" + '''
App Commands:
lc -> Show the condition of all lamps
elc -> Change the lighting condition
tun -> Turn the all lights on
tuf -> Turn the all lights off
rev -> Reverse the all lights condition
mnu -> Back to the main menu
end -> Close app

enter the command:
'''

def dic_key_index(dic, num):
    list = []
    for i in dic:
        list.append(i)
    return list[num]

def loc_code(code):
    n = code.index("/")
    x = code[:n]
    x1 = locations[int(x)-1]
    # returns dic
    return x1

def lum_code(code):
    n = code.index("/")
    x = code[:n]
    y = code[n+1:]
    x1 = locations[int(x)-1]
    y1 = dic_key_index(x1, int(y)-1)
    # returns key
    return y1

def code(location, lamp):
    y = 1
    x = locations.index(location) + 1
    for i in location:
        if i == lamp:
            break
        y += 1
    return str(x)+"/"+str(y)

def reverse(condition):
    if condition == False:
        condition = True
    elif condition == True:
        condition = False
    return condition

def complex_color(location):
    z = 0
    for i in location:
        if location[i] == False:
            print("\033[1;31;48m"+code(location, dic_key_index(location, z))+".",i ,"lamp"+ ":", "OFF")
        else:
            print("\033[1;32;48m"+code(location, dic_key_index(location, z))+".",i,"lamp"+ ":", "ON")
        z += 1

def true_false(condition):
    if condition == True:
        return "\033[1;32;48m"+"ON"
    else:
        return "\033[1;31;48m"+"OFF"

while True:
    cm = input(input_message)
    if cm == "lc":
        for i in locations_str:
            print("\033[0m" + i,"lamps: ")
            complex_color(locations[locations_str.index(i)])
    elif cm == "elc":
        for i in locations_str:
            print("\033[0m" + i,"lamps: ")
            complex_color(locations[locations_str.index(i)])
        change_list = []
        while True:
            cm2 = input("\033[0m" +'''enter the code of lamp that you want to change and than press \'enter\' button.
at the end, enter \'done\' :  ''')
            if cm2 == "done":
                break
            elif cm2 == "mnu":
                change_list = []
                break
            elif cm2 == "end":
                print("app closed! ")
                quit()
            else:
                change_list.append(cm2)
        for i in change_list:
            try:
                location = loc_code(i)
                lamp = lum_code(i)
                location[lamp] = reverse(location[lamp])
                print("\033[0m"+"the condition of", locations_str[locations.index(location)], lamp, "lamp is turned", true_false(location[lamp]))
            except:
                print("\033[0m"+"the", i, "command you entered is wrong! ")

    elif cm == "tun":
        for location in locations:
            for lamp in location:
                location[lamp] = True
        print("all lamps turned on. ")
    elif cm == "tuf":
        for location in locations:
            for lamp in location:
                location[lamp] = False
        print("all lamps turned off. ")
    elif cm == "rev":
        for location in locations:
            for lamp in location:
                location[lamp] = reverse(location[lamp])
        print("all lamps reversed. ")
    elif cm == "end":
        print("app closed! ")
        break
    else:
        print("wrong command! ")

# end