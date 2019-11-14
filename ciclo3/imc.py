# _*_ coding: latin1 _*_

import wx

"""
app = wx.App()

frame = wx.Frame(None, -1, 'IMC', style= wx.MAXIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX)

frame.Show()

app.MainLoop()
"""

class WindowsClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WindowsClass, self).__init__(*args, **kwargs)

        self.basic_gui()
        #self.Move((800, 450))
        #self.Centre()
        #self.Show()
    def basic_gui(self):
        panel = wx.Panel(self)

        self.CreateStatusBar()
        self.SetStatusText('Eu hein')

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        editMenu = wx.Menu()

        exitItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        menuBar.Append(fileMenu, '&File')
        menuBar.Append(editMenu, 'Edit')

        nameDialog = wx.TextEntryDialog(None, 'Qual o seu nome?', 'Seja Bem vindo.', 'Beltrano')

        if nameDialog.ShowModal() == wx.ID_OK:
            username = nameDialog.GetValue()

        nameDialog.Destroy()

        yesNoDialog = wx.MessageDialog(None, 'Isso está funcionando %s?' %username, 'Pergunta', wx.YES_NO)
        yesNoAnswer = yesNoDialog.ShowModal()
        yesNoDialog.Destroy()

        if yesNoAnswer == wx.ID_NO:
            username = 'Perdedor!'

        chooseOneBox = wx.SingleChoiceDialog(None, 'Qual a sua cor favorita?', 'Questao de cor', ['yellow', 'blue', 'black', 'green'])

        favColor = None

        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()

        chooseOneBox.Destroy()

        textArea = wx.TextCtrl(panel, pos=(3, 100), size=(200, 50))

        if favColor:
            textArea.AppendText('Sua cor favorita é o ' + favColor)

        text = wx.StaticText(panel, -1, 'Cor legal', (3, 3))

        text.SetForegroundColour('yellow')
        text.SetBackgroundColour('black')

        wx.Button(panel, 1, 'Close', (205, 130))
        """
        bmp = wx.Bitmap('closeButton.png')
        button = wx.BitmapButton(
            panel, id=1, bitmap=bmp, size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10), pos=(210, 110)
        )
        """

        aweText = wx.StaticText(panel, -1, 'Super customizado!', (3, 30))
        aweText.SetForegroundColour(favColor)
        aweText.SetBackgroundColour('black')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)

        self.SetSize((800, 600))
        #self.SetTitle('Calculo do IMC - Índice de Massa Corporal')
        self.SetTitle('Seja bem vindo ' + username)

        self.Bind(wx.EVT_BUTTON, self.onQuit, id=1)


        self.Centre()
        self.Show(True)

    def onQuit(self, e):
        self.Close()

def Main():
    app = wx.App()
    WindowsClass(None)
    app.MainLoop()

Main()
