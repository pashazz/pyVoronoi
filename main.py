from PyQt5 import QtGui, QtCore, uic, QtWidgets
#from qtpy import QtGui, QtCore, QtWidgets
import xml.etree.ElementTree as xml
import pyside2uic
from io import StringIO





from layout import Canvas
import sys
uifile = 'layout.ui'
form, base = uic.loadUiType(uifile)


class CreateLayout(base,form):
    def __init__(self):
        super(base,self).__init__()
        self.setupUi(self)
        self.PaintPanel = Canvas(self)
        self.canvas.insertWidget(0,self.PaintPanel)
        self.canvas.setCurrentWidget(self.PaintPanel)
        self.data_info= QtWidgets.QLabel()
        self.scrollArea.setWidget(self.data_info)

        self.output_info = QtWidgets.QLabel()
        self.output_area.setWidget(self.output_info)

        self.Establish_Connections()

    def Establish_Connections(self):
        self.Run_button.clicked.connect(self.PaintPanel.Run)
        self.clear_button.clicked.connect(self.PaintPanel.drawDisplay.ClearCanvas)
        self.open_button.clicked.connect(self.PaintPanel.IOData.ReadFile)
        self.next_data.clicked.connect(self.PaintPanel.IOData.next_data)
        self.step_button.clicked.connect(self.PaintPanel.step_by_step)
        self.output_button.clicked.connect(self.PaintPanel.IOData.output_data)
        self.reload_output.clicked.connect(self.PaintPanel.IOData.read_output)
        self.next_data.setEnabled(False)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CreateLayout()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
