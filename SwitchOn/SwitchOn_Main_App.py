# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:00:59 2021

@author: Gourav
"""
from UI import SwitchOn_UI
from Ops import Db_Ops
from Ops import Data_Model
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class PythonMongoDB(SwitchOn_UI.Ui_MainWindow, QtWidgets.QMainWindow): 
    
    " Main class to put everything together"
    
    def __init__(self):
        super(PythonMongoDB, self).__init__()
        self.setupUi(self)
        self.table = QtWidgets.QTableView()
        self.user_data = Db_Ops.get_multiple_data()
        self.model = Data_Model.CustomTableModel(self.user_data)
        self.delegate = Data_Model.InLineEditDelegate()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.verticalHeader().setDefaultSectionSize(50)
        self.tableView.hideColumn(0)
        self.tableView.resizeColumnToContents(True)
        self.tableView.resizeRowToContents(True)
        self.show()
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()
    
