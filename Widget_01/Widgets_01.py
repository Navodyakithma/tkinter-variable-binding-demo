#In here im going to use some Widgets
#First We need Import Some Packages
import tkinter as tk
from tkinter import ttk,PhotoImage


from logger import logging

class Main:
    #In this Constructor im creating Window but not run in here
    def __init__(self):

        try:

            logging.info("Create the Window")
            self.root = tk.Tk()
            # add A size and make the Center

            logging.info("Make the Window Center")
            display_width, display_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            width, height = 400, 400

            left = int((display_width / 2) - (width / 2))
            top = int((display_height / 2) - (height / 2))

            self.root.geometry(f"{width}x{height}+{left}+{top}")


            #Add a title to the created Window
            logging.info("Add a title")
            self.root.title("Application 01")

            #Add the Icon Image with png Extention to the Created the Window
            logging.info("Add Icon Image")
            image = PhotoImage(file='check-mark.png')
            self.root.iconphoto(False,image)


        except:
            logging.error("Something Went Wrong when Creating Window Section")

        # In this Function do all thing happens when the User Click the Button

    def command_happen(self):
         try:
            logging.info("User Clicked the Button")
            #Get the text for the Text Field and pass to the Label
            self.label.configure(text=self.entry_field.get())
            logging.info("get that Text and pass to the label")

            #Make the Button Click only ones
            logging.info("Make the Button Clicked Ones")
            self.button.configure(state='disabled')

         except:
              logging.error("Something Went Wrong when User click this Button")


    #In this Method add Some Widgets
    def add_the_widgets(self):
        try:

            logging.info("First add Entry Field to the Created Window")
            #Add a Field to created Entry Field
            self.entry_field = tk.Entry(self.root)
            self.entry_field.pack()

            logging.info("Add Button using ttk module and give the Command As well")
            #In here im going create Button using ttk module
            self.button = ttk.Button(self.root,text="Click Me",command=self.command_happen)
            self.button.pack()

            logging.info("Add a label to the Created Window")
            #In here im going to create a label
            self.label = ttk.Label(self.root)
            self.label.pack()

        except:
            logging.error("Something Went Wrong when add Widget Section")


    #In this Method Run the Created Window
    def run_the_window(self):
        try:
            logging.info("Run the Window")
            self.root.mainloop()
        except:
            logging.error("Something Went Wrong When Run the Created Window")


class Main_01:
    logging.info("Start the Program")
    myObject = Main()
    myObject.add_the_widgets()
    myObject.run_the_window()



