import tkinter as tk
from PIL import Image, ImageTk
import json

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

'''SETTING UP WINDOW AND EVERYTHING ELSE'''
window = tk.Tk()
window.wm_title("Election")
window.geometry("600x1000")
window.resizable(False, False)

message = tk.Label(text="Choose your president:")
message.pack()

# frame1 = tk.Frame()
# frame1.pack(fill='both', side='left', expand=True)

# frame2 = tk.Frame()
# frame2.pack(fill='both', side='right', expand=True)

# frame3 = tk.Frame()
# frame3.pack(side='bottom')
'''DONE SETTING UP'''

'''STARTING SETTING UP JSON'''
end_data = []

'''DONE SETTING UP JSON'''

def thank_the_user():
    popUpWindow = tk.Toplevel()
    popUpWindow.grab_set()
    popUpWindow.geometry("300x200")
    popUpWindow.resizable(False, False)
    popUpWindow.wm_title("Thanks")
    thank = tk.Label(popUpWindow, text="Thank You for voting!")
    thank.pack()
    def thanks_destroy():
        popUpWindow.grab_release()
        popUpWindow.destroy()

    ok_button = tk.Button(popUpWindow, text="ok", command=thanks_destroy)
    ok_button.pack()


def blue_pressed():
    print("Blue")
    data = {}
    data["object_id"] = get_random_string(16)
    data["ballot_style"] = "united-states-ballot-style"
    data["contests"] = [
        {
            "object_id": "presidency",
            "ballot_selections": [
                {
                    "object_id": "funny-valentine-selection",
                    "vote": "True"
                }
            ]
        }
    ]
    # vote = {}
    # vote["object_id"] = "presidency"
    # vote["ballot_selections"] = {}

    # data["contests"].append(

    # )
    end_data.append(data)
    thank_the_user()

def red_pressed():
    print("Red")
    data = {}
    data["object_id"] = get_random_string(16)
    data["ballot_style"] = "united-states-ballot-style"
    data["contests"] = [
        {
            "object_id": "presidency",
            "ballot_selections": [
                {
                    "object_id": "senator-armstrong-selection",
                    "vote": "True"
                }
            ]
        }
    ]
    # vote = {}
    # vote["object_id"] = "presidency"
    # vote["ballot_selections"] = {}

    # data["contests"].append(

    # )
    end_data.append(data)
    thank_the_user()

def close_window():
    popUpWindow = tk.Toplevel()
    popUpWindow.grab_set()
    
    popUpWindow.resizable(False, False)
    greeting = tk.Label(popUpWindow, text="Please enter password to make sure you are authorized to end it.")
    greeting.pack()
    password = tk.Entry(popUpWindow, show="*", fg="black", bg="white", width=50)
    password.pack()
    popUpWindow.wm_title("Close?")
    def finish_vote():
        if password.get() == "12345":
            # plaintext_ballots_simple.json
            f = open("data/plaintext_ballots_simple.json", "w")
            f.write(json.dumps(end_data))
            f.close()
            window.destroy()
        else:
            popUpWindow.grab_release()
            popUpWindow.destroy()
    ok_button = tk.Button(popUpWindow, text="ok", command=finish_vote)
    ok_button.pack()

'''adding the presidents here'''
# Adding the images
load1 = Image.open("valentine.png")
load1 = load1.resize((100,100), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(load1)
img1 = tk.Label(image=render1)
img1.pack()

pres1 = tk.Label(text="Funny Valentine")
pres1.pack()

# Button for Funny Valentine
button1 = tk.Button(
    text="Blue",
    width=25,
    height=5,
    bg="blue",
    fg="white",
    command=blue_pressed,
    
)
button1.pack()

# Adding the images
load2 = Image.open("armstrong.png")
load2 = load2.resize((100,100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)
img2 = tk.Label(image=render2,)
img2.pack()

pres2 = tk.Label(text="Senator Armstrong", )
pres2.pack()

# Adding button for Armstrong
button2 = tk.Button(
    text="Red",
    width=25,
    height=5,
    bg="red",
    fg="white",
    command=red_pressed,
    
)
button2.pack()

button3 = tk.Button(
    text="Done",
    width=5,
    height=5,
    command=close_window,
    
)

button3.pack()

window.mainloop()