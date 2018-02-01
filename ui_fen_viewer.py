# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fen_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FenViewer(object):
    def setupUi(self, FenViewer):
        FenViewer.setObjectName("FenViewer")
        FenViewer.resize(612, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FenViewer.sizePolicy().hasHeightForWidth())
        FenViewer.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(FenViewer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.f_board = QtWidgets.QFrame(FenViewer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_board.sizePolicy().hasHeightForWidth())
        self.f_board.setSizePolicy(sizePolicy)
        self.f_board.setMinimumSize(QtCore.QSize(600, 600))
        self.f_board.setMaximumSize(QtCore.QSize(600, 600))
        self.f_board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_board.setObjectName("f_board")
        self.verticalLayout.addWidget(self.f_board)
        self.le_fen_string = QtWidgets.QLineEdit(FenViewer)
        self.le_fen_string.setObjectName("le_fen_string")
        self.verticalLayout.addWidget(self.le_fen_string)
        self.le_move_string = QtWidgets.QLineEdit(FenViewer)
        self.le_move_string.setObjectName("le_move_string")
        self.verticalLayout.addWidget(self.le_move_string)
        self.widget = QtWidgets.QWidget(FenViewer)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_show_all_moves = QtWidgets.QCheckBox(self.widget)
        self.cb_show_all_moves.setObjectName("cb_show_all_moves")
        self.horizontalLayout.addWidget(self.cb_show_all_moves)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_insert_default_board = QtWidgets.QPushButton(self.widget)
        self.pb_insert_default_board.setObjectName("pb_insert_default_board")
        self.horizontalLayout.addWidget(self.pb_insert_default_board)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(FenViewer)
        QtCore.QMetaObject.connectSlotsByName(FenViewer)

    def retranslateUi(self, FenViewer):
        _translate = QtCore.QCoreApplication.translate
        FenViewer.setWindowTitle(_translate("FenViewer", "FEN Viewer"))
        self.le_fen_string.setPlaceholderText(_translate("FenViewer", "FEN String"))
        self.le_move_string.setPlaceholderText(_translate("FenViewer", "Move String"))
        self.cb_show_all_moves.setText(_translate("FenViewer", "show moves"))
        self.pb_insert_default_board.setText(_translate("FenViewer", "insert initial board"))

