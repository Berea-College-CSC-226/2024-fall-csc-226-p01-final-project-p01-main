######################################################################
# Author: Arohasina, Dindin
# Username: dindin_aro
#
# T12: Events and GUIs
#
# Purpose: To explore the Tkinter module for making a GUI
#
# A GUI widget is a graphical component such as a button, text label as shown below.
# GUI widgets also exist to make drop-down menus and scroll bars, display images, etc...
# Tkinter gives you the ability to create GUI Windows containing widgets.
# This program is a simple exploration.
#######################################################################
# Acknowledgements:
#
# Original code written by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk       # Python's most commonly used GUI package.


class MyTkinterApp:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """
        self.root = tk.Tk()                         # Create the root window where all widgets go
        self.root.minsize(width=500, height=300)    # Sets the window's minimum size
        self.root.maxsize(width=500, height=300)    # Sets the window's maximum size
        self.root.title(windowtext)                 # Sets root window title

        self.count = 0                              # Click counter for myButton1
        self.myButton1 = None
        self.myButton2 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()      # Makes a Tkinter string variable
        self.myTextLabel1 = None
        self.myScale1=None
        self.myTextLabel2Text = tk.StringVar()
        self.myTextLabel2=None
        self.myTextLabel3Text = tk.StringVar()
        self.myTextLabel3=None


    def create_button1(self, buttontext="Push"):
        """
        Creates a button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.myButton1 = tk.Button(self.root, text=buttontext, command=self.button1_handler)
        # Note that when myButton1 button is pushed, self.button1handler is called
        self.myButton1.grid(row=0, column=0,padx=10, pady= 10)
        #self.myButton1.pack()                    # pack means add to window

    def create_button2(self, buttontext="Show Age"):
        """
        Creates a second button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.myButton2 = tk.Button(self.root, text=buttontext, command=self.scale_handler)
        self.myButton2.grid(row=3, column=1,padx=10, pady= 10)
        #self.myButton2.pack()                       # pack means add to window

    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """
        self.myTextBox1.grid(row=1, column=0,padx=10, pady= 10)
        #self.myTextBox1.pack()                      # pack means add to window

    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.grid(row=2, column=0,padx=10, pady= 10)
        #self.myTextLabel1.pack()                    # pack means add to window

    def create_label2(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel2Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel2 = tk.Label(self.root, textvariable=self.myTextLabel2Text)
        self.myTextLabel2.grid(row=2, column=1,padx=10, pady= 10)
        #self.myTextLabel2.pack()                    # pack means add to window

    def create_label3(self, labeltext="How old are you?"):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel3Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel3 = tk.Label(self.root, textvariable=self.myTextLabel3Text)
        self.myTextLabel3.grid(row=0, column=1,padx=10, pady= 10)
        #self.myTextLabel3.pack()


    def button1_handler(self):
        """
        Event handler for myButton1 above.
        Gets the text from the textbox and writes in myTextLabel1

        :return: None
        """
        txt = self.myTextBox1.get()                 # Retrieves the text entered by the user
        self.count += 1                             # increments each time the handler is called (button is pressed)
        if self.count % 10 == 0:
            message = "Wow, {1} clicks! Keep it up, {0}!".format(txt, self.count)
        else:
            message = "Hey {0}, click it again!\nYou have clicked the button {1} times.".format(txt, self.count)
        self.myTextLabel1Text.set(message)


    def create_scale(self):
        self.myScale1=tk.Scale(self.root, from_=0, to=100, orient="horizontal")
        self.myScale1.grid(row=1, column=1,padx=10, pady= 10)
        #self.myScale1.pack()

    def scale_handler(self):
        """
        Event handler for scale.
        Shows a simple message of the age

        :return: None
        """
        age = self.myScale1.get()
        self.myTextLabel2Text.set("you are "+ str(age) + " years old" )


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = MyTkinterApp("CSC226 Hello GUI")           # Create a new myTkinter object

    myGUI.create_button1("What is your name?")     # Calls the create button method to create a button

    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_label1()                           # Create a label to writing text into (empty for now)

    myGUI.create_label3("How old are you?")
    myGUI.create_scale()
    myGUI.create_button2("Show Age")
    myGUI.create_label2()


    myGUI.root.mainloop()                           # Needed to start the event loop


if __name__ == "__main__":
    main()
