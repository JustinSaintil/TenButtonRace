#! /usr/bin/env python

import wx

def OnClickMe(e): 
		wx.MessageBox("You Clikced it, which implies, you actually, are, a, fool", "Well Than", wx.CANCEL)

myApp = wx.App(False) #print normal error messages

frame = wx.Frame(None, wx.ID_ANY, "Do the JOHN WALL")

btnClickMe = wx.Button(frame, label= "Click Me Fool!")

btnClickMe.Bind(wx.EVT_BUTTON, OnClickMe)

frame.Show(True)

myApp.MainLoop()
