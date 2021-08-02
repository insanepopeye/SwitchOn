# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:02:46 2021

@author: Gourav 
"""
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class CustomTableModel(QtCore.QAbstractTableModel):
    """
    Custom Table Model to handle MongoDB Data
    """
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = list(self.user_data[0].keys())

    def flags(self, index):
        """
        Make each table column with specific properties
        :param index:
        :return:
        """
        if index.column() < 3:
            return QtCore.Qt.ItemIsSelectable |QtCore.Qt.ItemIsEnabled
        if index.column() == 3:
            return QtCore.Qt.BackgroundRole | QtCore.Qt.ItemIsEnabled
        if index.column() == 4:
            return QtCore.Qt.DecorationRole | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

    def rowCount(self, *args, **kwargs):
        """
        set row counts
        :param args:
        :param kwargs:
        :return:
        """
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        """
        set column counts
        :param args:
        :param kwargs:
        :return:
        """
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """
        set column header data
        :param section:
        :param orientation:
        :param role:
        :return:
        """
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[section].title()

    def data(self, index, role):
        """
        Display Data in table cells
        :param index:
        :param role:
        :return:
        """
        row = self.user_data[index.row()]
        column = self.columns[index.column()]
        if index.column() == 3:
            selected_row = self.user_data[index.row()]
            Status = selected_row['Status']
            if Status == 'Bad':
                return QtGui.QColor('Red')
            elif Status == 'Good':
                return QtGui.QColor('Green')
        
        try:
            if index.column() == 4:
                selected_row = self.user_data[index.row()]
                image_data = selected_row['Photo']
                image = QtGui.QImage()
                image.loadFromData(image_data)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap.fromImage(image))
                return icon
            elif role == QtCore.Qt.DisplayRole:
                return str(row[column])
        except KeyError:
            return None


class InLineEditDelegate(QtWidgets.QItemDelegate):
    """
    Delegate is important for inline editing of cells
    """

    def createEditor(self, parent, option, index):
        return super(InLineEditDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        text = index.data(QtCore.Qt.EditRole) or index.data(QtCore.Qt.DisplayRole)
        editor.setText(str(text))