import wx
import os

class MainWindow(wx.Frame):
    """New class Frame"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu=wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)
    def OnAbout (self, e):
        dlg = wx.MessageDialog(self, "A small text editor",
                               "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def OnExit(self, e):
        self.Close(True)

app = wx.App(False)
frame = MainWindow(None, 'Small editor')
app.MainLoop()