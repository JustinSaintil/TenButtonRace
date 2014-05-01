#! /usr/bin/env python

import wx

def OnJustinsButton(e):
    btnJustinsButton.SetLabel("Ooh Killem")





#-----------Main Program Below --------------

app = wx.App(False)#Display errors normally

frame = wx.Frame(None, wx.ID_ANY, "Justin Saintil is A BOSS")
#ID_ANY means -1

btnJustinsButton = wx.Button(frame, label= "SELF DESTRUCT!")

btnJustinsButton.Bind(wx.EVT_BUTTON, OnJustinsButton)

frame.Show(True)

app.MainLoop()