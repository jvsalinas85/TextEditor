'''Create a text editor'''

import tkinter as tk
from tkinter import Menu
from tkinter import Text
from tkinter import filedialog as fd


#Declaring the overall path
path = ""

#Declare the class
class App(tk.Tk):
    def __init__(self):
        super().__init__()


        window_width = 1500
        window_height = 800

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(0,0)

        self.create_widgets()
    

    def create_widgets(self):
        '''This creates the whole widgets'''
        self.title("Text Editor")

        #create the superior menu
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        #create Files menu inside our menu bar
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        #Now we add elements to our Files menu
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save File", command=self.save_file)
        file_menu.add_command(label="Save File As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)

        #create the main editor screen
        self.text = Text(self)
        self.text.pack(fill=tk.BOTH, expand=True) #so it covers the whole screen
        self.text.config(padx=10, pady=10, bd=0, font=("Consolas", 12)) #setting a padding x and y and changing font to Consolas size 12
        self.text.focus()

        #create the lower tab
        self.message = tk.StringVar() #create a stringvar, this will display in the lower tab the command we are dealing with
        self.message.set("Editor by Jesus Valencia")
        lower_label = tk.Label(self, textvariable=self.message, justify="right") #creating the label justified to the right
        lower_label.pack(side="left") #sets the label at the left side of the widget




    def new_file(self):
        '''Logic for creating an empty document'''
        self.message.set("New document")
        self.text.delete(1.0,tk.END) #This delete method deletes character from text. The 1.0 means is one char, and the second is where to finish. END document.

        #we have to make sure each time a the New document button is pressed we erase the path and the title to its original state
        global path
        self.title("Text Editor")
        path = ''

        
        

    def open_file(self):
        '''Logic to open an existing file'''
        self.message.set("Open File...")
        global path
        path = fd.askopenfilename(initialdir=".",filetypes=(("Text Files","*.txt"), ("All files","*")),title="Open File...") #opens dialog to ask for file name
        # filetypes is a series of tuples where you specify the description of the filetype and on second place the available file extension

        #If path is correct we open it
        if path != '':
            file = open(path,'r') #open the path
            content = file.read() #assign the content to a variable
            self.text.delete(1.0,tk.END) #delete all information present in the editor
            self.text.insert('insert',content) #insert the content in the widget
            file.close() #close file
            self.title(path+" -  My Text Editor") #changing the title to display the file path and the original Title in a string


    def save_file(self):
        '''Logic to save the current document'''
        self.message.set("Save File...")

        #This is only when a file already exists
        global path
        if path != '':
            content = self.text.get(1.0,"end-1c") #we get the whole text that is present in the window minus 1 char. Because it always adds an extra char at the end
            file = open(path,'w+') #open the file or creat if it doesn't exist
            file.write(content) #write the content into the file located in "path"
            file.close() #close the file
            self.message.set("File saved correctly.") #display that we saved the file.

        #This is when the file is new and we have to save it with a new name
        else:
            self.save_file_as()
    
    def save_file_as(self):
        '''Logic to save the document as'''
        self.message.set("Save Document As...")

        global path
        file = fd.asksaveasfile(title="Save document As", mode='w', defaultextension='.txt')
        path = file.name
        
        if file is not None:
            content = self.text.get(1.0, 'end-1c') #get all the text minus 1 char
            file = open(path,'w+') #open the file or create a new one if it doesn't exist
            file.write(content) #write the content
            file.close() #Close file
            self.message.set("File saved correctly")
        else:
            self.message.set("Save Cancelled")

    def exit(self):
        '''Exit editor'''
        self.destroy()
        






if __name__ == "__main__":
    app = App()
    app.mainloop()
