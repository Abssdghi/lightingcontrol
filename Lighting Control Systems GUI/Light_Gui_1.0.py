from tkinter import *

# Lighting condition app

lobby = {
    "upright": False,
    "downright": False,
    "upleft": False,
    "downleft": False
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


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

def show():
    for i in locations:
        print(i)


def connection():
    for location in locations:
        for lamp in location:
            if location[lamp] == True:
                var_name = f'{locations_str[locations.index(location)]}_{lamp}'
                globals()[var_name].select()
            elif location[lamp] == False:
                var_name = f'{locations_str[locations.index(location)]}_{lamp}'
                globals()[var_name].deselect()
    show()


def rev_def():
    for location in locations:
        for lamp in location:
            location[lamp] = reverse(location[lamp])
    connection()
    print("all lamps reversed. ")

def tun_def():
    for location in locations:
        for lamp in location:
            location[lamp] = True
    connection()
    print("all lamps turned on. ")

def tuf_def():
    for location in locations:
        for lamp in location:
            location[lamp] = False
    connection()
    print("all lamps turned off. ")

def change(location, lamp):
    location[lamp] = reverse(location[lamp])

def chan_def():
    for location in locations:
        for lamp,condition in location.items():
            var_name = f'{locations_str[locations.index(location)]}_{lamp}_var'
            if globals()[var_name].get() == 1:
                location[lamp] = True
            else:
                location[lamp] = False
    show()

def ex_def():
    quit()

root = Tk()
root.geometry('750x430')
root.title('Lighting App')
root.resizable(width=False, height=False)
root.config(background='#202020')

main_ph = PhotoImage(file='main.png')
tuf_ph = PhotoImage(file='icons8-switch-off-55.png')
tun_ph = PhotoImage(file='icons8-switch-on-55.png')
rev_ph = PhotoImage(file='icons8-reverse-55.png')
ex_ph = PhotoImage(file='icons8-close-55.png')

main = Label(root, image=main_ph, bg='#202020')
main.place(x=22, y=78)

tuf_butt = Button(master=root, image=tuf_ph, bg='#202020', command=tuf_def)
tun_butt = Button(master=root, image=tun_ph, bg='#202020', command=tun_def)
rev_butt = Button(master=root, image=rev_ph, bg='#202020', command=rev_def)
ex_butt = Button(master=root, image=ex_ph, bg='#202020', command=ex_def)

tuf_butt.place(x=311,y=10)
tun_butt.place(x=241,y=10)
rev_butt.place(x=381,y=10)
ex_butt.place(x=451,y=10)

for location in locations:
    for lamp,condition in location.items():
        var_name = f'{locations_str[locations.index(location)]}_{lamp}_var'
        globals()[var_name] = IntVar()


for location in locations:
    for lamp,condition in location.items():
        var_name = f'{locations_str[locations.index(location)]}_{lamp}'
        globals()[var_name] = Checkbutton(master=root,
                     disabledforeground='red',
                     indicatoron=0,
                     background='red',
                     activebackground='white',
                     selectcolor='green',
                     width=2,
                     height=1,
                     variable=globals()[var_name+'_var'],
                     onvalue=1,
                     offvalue=0,
                     command=chan_def)



lobby_upright.place(x=497, y=143)
lobby_upleft.place(x=241, y=143)
lobby_downright.place(x=497, y=269)
lobby_downleft.place(x=242, y=269)

wc_door.place(x=98, y=201)
wc_men.place(x=98, y=132)
wc_women.place(x=98, y=269)

secretary_desk.place(x=626, y=258)
secretary_back.place(x=626, y=143)


root.mainloop()