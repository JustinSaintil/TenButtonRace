#!/usr/bin/env python

#You will experiment with this file by changing it and adding to it.
#But first just run it and see what it does.

#Now that you have run the file, read through it and look at the exercises below.

#We always have to import wx before we can use it.
import wx


#In wx we always sart by creating a wx.App. I like to call it "app".
app = wx.App(False) #False means error messages will print in the normal way

#Create a new frame (A frame is often casually called a window).
frame = wx.Frame(None, wx.ID_ANY, "J.S.", size=(400,100), pos=(1000,300)) # None means it is top level. It has no parent frame.

# Show the frame.
frame.Show(True)

#MainLoop makes the app listen for clicks, and other events.
#This is always the last line of a wxPython app.
app.MainLoop()

# ----------- Exercises Below -----------------

#1. Change the title of your Frame to something new.

#2. Add the argument size = (400,100) to the frome constructor on line 16.
#What does it do?
#It changes the dimensions (width and height) of my frame.

#3. Add the argument pos=(1000,300) to the frome constructor on line 16.
#What does it do?

#It changes the allignment of the frame on my screen.