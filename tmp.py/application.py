import wx
import os


class Application(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="VP-5 KKM", size=(800, 600))
        panel=MainPanel(self)
        self.Center()
        self.create_menu_bar()



    def create_menu_bar(self):
        self.CreateStatusBar()

        filemenu = wx.Menu()
        new_file = filemenu.Append(wx.ID_NEW, "&Новое замечание",
                                   "Create new file")
        self.Bind(wx.EVT_MENU, self.create_new_file, new_file)

        open_file_menu = filemenu.Append(wx.ID_OPEN, "&Открыть",
                                        "Open file in editor")
        self.Bind(wx.EVT_MENU, self.open_file, open_file_menu)

        filemenu.Append(wx.ID_SAVEAS, "Сохранить как")

        print_file = filemenu.Append(wx.ID_PRINT, "Печать")
        self.Bind(wx.EVT_MENU, self.printer, print_file)

        filemenu.AppendSeparator()

        exit_program = filemenu.Append(wx.ID_EXIT, "Выход",
                                       "Terminate the program")
        self.Bind(wx.EVT_MENU, self.exit_prog, exit_program)

        filemenu.AppendSeparator()

        helpmenu = wx.Menu()
        helpmenu.Append(wx.ID_HELP, "Help", "Show help content")
        hlp_about = helpmenu.Append(wx.ID_ABOUT, "О программе",
                                    "Information about this program")
        helpmenu.AppendSeparator()
        self.Bind(wx.EVT_MENU, self.on_about, hlp_about)

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Файл")
        menuBar.Append(helpmenu, "&Help")

        self.SetMenuBar(menuBar)
        self.Show(True)

    def printer(self, event):
        """Распечатать файл
        !!!Необходимо найти информацию для реализации!!!
        """
        pass

    def open_file(self, event):
        """Открыть файл, для просмотра, редактирования.
            !!! Необходимо определиться в каком
            формате будет хранится файл "замечаний"!!!
        """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Выберите файл", self.dirname, "", "*.*",
                            wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


    def exit_prog(self, event):
        """Выход из программы, закрытие приложения"""
        self.Close(True)


    def create_new_file(self, event):
        """Создание нового замечания
            !!Необходимо доделать!!
        """

        create_comment = CreateComment(None, "Новое замечание")
        create_comment.Show()


    def on_about(self, event):
        """Информация о программе, кто разработал,
        версию программы, реквизиты для обратной
        связи.
        """
        dlg_about = wx.MessageDialog(self, "Текст который необходимо "
                                           "добавить в описание программы",
                                            "О программе")
        dlg_about.ShowModal()

class MainPanel(wx.Panel):
    """Добавить фоновое изображение"""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame=parent
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_add_jpg)

    def on_add_jpg(self, event):
        dc=event.GetDC()
        if not dc:
            dc=wx.ClientDC(self)
            rect=self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp=wx.Bitmap("tmp.jpg")
        dc.DrawBitmap(bmp, 0, 0)


class CreateComment(wx.Frame):
    def __init__(self, parent, text):
        wx.Frame.__init__(self, parent, title=text, size=(400, 300))
        self.panel=wx.Panel(self, wx.ID_ANY)

        lbl_number = wx.StaticText(self.panel, wx.ID_ANY,
                                   "Заводской номер")
        input_number=wx.TextCtrl(self.panel, wx.ID_ANY, '')
        ok_btn=wx.Button(self.panel, wx.ID_ANY, "Добавить")
        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)
        self.murkup(lbl_number, input_number, ok_btn)

    def murkup(self, lbl_number, input_number, ok_btn):
        top_sizer=wx.BoxSizer(wx.VERTICAL)
        input_one_sizer=wx.BoxSizer(wx.HORIZONTAL)
        input_num=wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer=wx.BoxSizer(wx.HORIZONTAL)

        input_one_sizer.Add(lbl_number, 0, wx.ALL, 5)
        input_one_sizer.Add(input_number, 1, wx.ALL | wx.EXPAND, 5)


        btn_sizer.Add(ok_btn, 0, wx.ALL, 5)

        top_sizer.Add(input_one_sizer, 0, wx.ALL | wx.EXPAND, 5)
        #top_sizer.Add(input_num, 0, wx.ALL | wx.EXPAND, 5)
        top_sizer.Add(wx.StaticLine(self.panel, ), 0, wx.ALL | wx.EXPAND, 5)
        top_sizer.Add(btn_sizer, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(top_sizer)
        top_sizer.Fit(self)

    def on_ok(self, event):
        pass

if __name__ == "__main__":
    app = wx.App(False)
    frame = Application(None)
    app.MainLoop()