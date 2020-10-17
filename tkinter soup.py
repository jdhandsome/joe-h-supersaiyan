import tkinter as tk
import urllib3
from bs4 import BeautifulSoup as bs

#Required for URLLIB3. Creates a pool manager
http = urllib3.PoolManager()

#creates a GUI window for tkinter
window = tk.Tk()

#Puts everything after the Frame command into a frame
frame_a = tk.Frame()

#Creates the first label
label = tk.Label(
    text="Pull all url's from a webpage"
)
label.pack()

#Creates the first button. Notice the attributes and how it is set up. You do not have to indent. makes it cleaner
button = tk.Button(
    text="Execute Search",
    background="green"
)
button.pack(fill=tk.X)

#second close button
close = tk.Button(
    text="End Search",
    background="red"
)
close.pack(fill=tk.X)

#label for search field and search field. positioned via coordinates

label_b = tk.Label(
    text="Input URL Here:"
)

label_b.pack()
label_b.place(x=10, y=73)

entry = tk.Entry(
    width=70
    )
entry.place(x=0, y=90)
entry.pack()

frame_a.pack()

#Search box code
text_box = tk.Text()
text_box.pack()

#Code for what happenes when you press the GUI buttons

#defines what happens when you click the execute search button
def handle_click(event):
    #pulls info from the entry field
    info = entry.get()
    #deletes whats in the text_box
    text_box.delete('1.0', tk.END)

    try:
        #BeautifulSoup entry. gets the URL from info, passes it to soup
        html_doc = http.request('GET',info).data
        soup = bs(html_doc, 'html.parser')

        #creates a urls list
        urls = []

        #loops through each anchor in the web page
        for i in soup.find_all("a"):
                #gets the links with an href, then finds http.
                link = i.get('href')
                result = link.find('http')
                #if the link has http it adds to the URL list. If not, the error is -1
                if result != -1:
                    urls.append(link)
        for url in urls:
            #loops through the url list and formats the output to contain two white spaces
            space = (url + "\n" + "\n")
            #inserts the results into the text_box
            text_box.insert('1.0', space)
    except:
        #throws a -1 exception on all errors
        -1
#binds the search button to the handle_cick function
button.bind("<Button-1>", handle_click)

def exit(event):
    window.destroy()
#binds the exit button to the ext function
close.bind("<Button-1>",exit)

#closes the tk program
window.mainloop()
