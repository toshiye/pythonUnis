# _*_ coding: latin1 _*_

# importa wxPython
import wx

# Identificadores para as opções do menu
ID_FILE_OPEN = wx.NewId()
ID_FILE_SAVE = wx.NewId()
ID_FILE_EXIT = wx.NewId()
ID_HELP_ABOUT = wx.NewId()


class Main(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        # Cria o menu arquivo
        filemenu = wx.Menu()

        # Cria as opções
        filemenu.Append(ID_FILE_OPEN, 'Abrir arquivo...')
        filemenu.Append(ID_FILE_SAVE, 'Salvar')
        filemenu.AppendSeparator()
        filemenu.Append(ID_FILE_EXIT, 'Sair')

        # Cria o menu ajuda
        helpmenu = wx.Menu()
        helpmenu.Append(ID_HELP_ABOUT, 'Sobre...')

        # Cria o menu
        menubar = wx.MenuBar()
        menubar.Append(filemenu, 'Arquivo')
        menubar.Append(helpmenu, 'Ajuda')
        self.SetMenuBar(menubar)

        # Associa  métodos aos eventos de menu
        wx.EVT_MENU(self, ID_FILE_OPEN, self.on_open)
        wx.EVT_MENU(self, ID_FILE_SAVE, self.on_save)
        wx.EVT_MENU(self, ID_FILE_EXIT, self.on_exit)
        wx.EVT_MENU(self, ID_HELP_ABOUT, self.about)

        # Cria uma caixa de texto
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.fn = ''

    def on_open(self, evt):
        # Abre uma caixa de diálogo escolher arquivo
        dialog = wx.FileDialog(None, style=wx.OPEN)
        d = dialog.ShowModal()
        if d == wx.ID_OK:
            # Pega arquivo escolhido
            self.fn = dialog.GetPath()

            # Muda o título da janela
            self.SetTitle(self.fn)

            # Carrega o texto na caixa de texto
            self.control.SetLabel(file(self.fn, 'rb').read())
            dialog.Destroy()

    def on_save(self, evt):
        # Salva o texto na caixa de texto
        if self.fn:
            file(self.fn, 'wb').write(self.control.GetLabel())

    def on_exit(self, evt):
        # Fecha a janela principal
        self.Close(True)

    def about(self, evt):
        dlg = wx.MessageDialog(self, 'Exemplo wxPython', 'Sobre...', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


app = wx.App()
frame = Main(None, wx.ID_ANY, 'Isto é quase um editor...')
frame.Show(True)
app.MainLoop()
