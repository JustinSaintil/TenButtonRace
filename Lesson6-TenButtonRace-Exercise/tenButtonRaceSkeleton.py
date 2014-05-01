#! /usr/bin/evn python

import wx
import time
#import the graphical library
#import the time module

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race")
		
		self.panel = wx.Panel(self)
		
		self.btnStartButton = wx.Button(self.panel, label="Start", pos=(5, 20))
		self.btnButton1   = wx.Button(self.panel, label="Can't touch this", pos=(10, 60))
		self.btnButton2 = wx.Button(self.panel, label="DA", pos=(30, 20))
		self.btnButton3   = wx.Button(self.panel, label="DA", pos=(40, 40))
		self.btnButton4   = wx.Button(self.panel, label="DA", pos=(50, 70))
		self.btnButton5   = wx.Button(self.panel, label="DA", pos=(60, 90))
		self.btnButton6   = wx.Button(self.panel, label="DA", pos=(70, 10))
		self.btnButton7   = wx.Button(self.panel, label="DA", pos=(80, 30))
		self.btnButton8   = wx.Button(self.panel, label="DA", pos=(90, 100))
		self.btnButton9   = wx.Button(self.panel, label="DA", pos=(100, 5))
		self.btnButton10   = wx.Button(self.panel, label="Can't Touch This", pos=(110, 400))
		
		self.btnStartButton.Show(True)
		self.btnButton1.Show(False)
		self.btnButton2.Show(False)
		self.btnButton3.Show(False)
		self.btnButton4.Show(False)
		self.btnButton5.Show(False)
		self.btnButton6.Show(False)
		self.btnButton7.Show(False)
		self.btnButton8.Show(False)
		self.btnButton9.Show(False)
		self.btnButton10.Show(False)
		
		self.btnStartButton.Bind(wx.EVT_BUTTON, self.OnStartButton)
		self.btnButton1.Bind(wx.EVT_BUTTON, self.OnButton1)
		self.btnButton2.Bind(wx.EVT_BUTTON, self.OnButton2)
		self.btnButton3.Bind(wx.EVT_BUTTON, self.OnButton3)
		self.btnButton4.Bind(wx.EVT_BUTTON, self.OnButton4)
		self.btnButton5.Bind(wx.EVT_BUTTON, self.OnButton5)
		self.btnButton6.Bind(wx.EVT_BUTTON, self.OnButton6)
		self.btnButton7.Bind(wx.EVT_BUTTON, self.OnButton7)
		self.btnButton8.Bind(wx.EVT_BUTTON, self.OnButton8)
		self.btnButton9.Bind(wx.EVT_BUTTON, self.OnButton9)
		self.btnButton10.Bind(wx.EVT_BUTTON, self.OnButton10)
		#Bind all the buttons to their event handlers
		
	# Event handler for the start button
	def OnStartButton(self, e):
		#Make the start button disappear
		self.time = time.time()
		self.btnButton1.Show(True)
		self.btnStartButton.Show(False)
	
	def OnButton1(self, e):
		self.btnButton2.Show(True)
		self.btnButton1.Show(False)

	def OnButton2(self, e):
		self.btnButton3.Show(True)
		self.btnButton2.Show(False)
	
	def OnButton3(self, e):
		self.btnButton4.Show(True)
		self.btnButton3.Show(False)
	
	def OnButton4(self, e):
		self.btnButton5.Show(True)
		self.btnButton4.Show(False)
	
	def OnButton5(self, e):
		self.btnButton6.Show(True)
		self.btnButton5.Show(False)
		
	def OnButton6(self, e):
		self.btnButton7.Show(True)
		self.btnButton6.Show(False)
		
	def OnButton7(self, e):
		self.btnButton8.Show(True)
		self.btnButton7.Show(False)
	
	def OnButton8(self, e):
		self.btnButton9.Show(True)
		self.btnButton8.Show(False)
	
	def OnButton9(self, e):
		self.btnButton10.Show(True)
		self.btnButton9.Show(False)
	
	def OnButton10(self, e):
		self.btnButton10.Show(True)
		self.btnButton10.Show(False)
		self.time = time.time()-self.time
		wx.MessageBox("Your time was: " + str(self.time), "Great Job, Now Try to Go Even Faster", wx.CANCEL)


	#Other event handlers here
	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()