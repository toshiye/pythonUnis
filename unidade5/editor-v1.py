# _*_ coding: latin1 _*_

# importa wxPython
import wx


class Main(wx.Frame):
    """
    Classe que define a janela principal do programa.
    """

    def __init__(self, parent, id, title):
        """
        Inicializa a classe
        """
        # Define a janela usando o __init__ da classe mãe
        wx.Frame.__init__(self, parent, id, title, size=(600, 400))

        # Cria uma caixa de texto
        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # Pega a fonte do programa (decodificado para latin1)
        font = file(__file__, 'rb').read().decode('latin1')

        # Carrega a fonte do programa na caixa de texto
        self.text.SetLabel(font)

        # Mostra a janela
        self.Show(True)

if __name__ == '__main__':
    # Cria um objeto "aplicação" do wxPython
    app = wx.App()

    # Cria um objeto "janela" a partir da classe
    frame = Main(None, wx.ID_ANY, 'Fonte')

    # Inicia o loop de tratamento de eventos
    app.MainLoop()
