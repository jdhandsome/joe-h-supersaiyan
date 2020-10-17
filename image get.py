from bs4 import BeautifulSoup
from PIL import Image
import urllib3
import io
import requests
import tkinter as tk
import tkinter.filedialog

# used by urllib2
http = urllib3.PoolManager()
#global list to hold downloaded pics
pics = []

#start of tkinter window
window = tk.Tk()
#sizes tkinter window
frame_a = tk.Frame(master=window, width=525, height=10)

#Creates the tkinter labels and buttons
label = tk.Label(
    text="Pull all images from a webpage"
)

label.pack()

label_b = tk.Label(
    text="Input URL Here:"
)

label_b.pack()
label_b.place(x=20, y=18)

entry = tk.Entry(
    width=50
    )
entry.pack()

#Creates the first button. Notice the attributes and how it is set up. You do not have to indent. makes it cleaner
button = tk.Button(
    text="Execute",
    background="green"
)
button.pack(fill=tk.X)

#second close button
close = tk.Button(
    text="End",
    background="red"
)
close.pack(fill=tk.X)

#begin functions to bind buttons
#gives a status of complete after get_url executes
def status(event):
    entry_c = tk.Entry()
    entry_c.pack()
    get_url()
    entry_c.insert(0, "complete")

#function to get images from website
def get_url():

    entry_text = entry.get()
    #builds the beautfulsoup object, if it fails throws a -1 exception
    try:
        html_doc = http.request('GET',entry_text).data
        soup = BeautifulSoup(html_doc, 'html.parser')
    except:
        -1
    #images list used to store images
    images = []
    #loops through all img tages in the website and stores them in images
    for image in soup.find_all("img"):
         images.append(image.get('src'))
    #loops throw the images list and gets the actual pic file and stores in pics
    for img in images:

        try:
            response = requests.get(img, stream=True)
            response.raw.decode_content = True
            image = Image.open(response.raw)
            pics.append(image)
        except:
            -1
    num = 1
    #Save as operation, asks where to save the files
    f = tkinter.filedialog.asksaveasfile(mode='w')
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    #loops through pic images, converts num to string to append file name
    for pic in pics:
        n = str(num)
        #pulls the name and location from the iowrapper f
        file_name = (f.name)
        #saves the image file with the filename, space, number, png file format
        pic.save(file_name + " " + n + '.png' )
        #increments num
        num = num + 1

#binds the search button to the handle_cick function
button.bind("<Button-1>", status)
#exits window
def exit(event):
    window.destroy()

#binds the exit button to the ext function
close.bind("<Button-1>",exit)
#end tkinter window
frame_a.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
window.mainloop()
