from PySide2.QtCore import (QAbstractTableModel, QDateTime, QModelIndex,
                            QRect, Qt, QTimeZone, Slot)


from PySide2.QtWidgets import (QAction, QApplication, QHBoxLayout, QHeaderView,
                               QMainWindow, QSizePolicy, QTableView, QWidget)

import sys

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("LaTeX Generator")
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        ## Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)
        ## Open QAction
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        self.file_menu.addAction(open_action)
        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Ready")
        # Window dimensions
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

    @Slot()
    def exit_app(self, checked):
        sys.exit()

    @Slot()
    def open_file(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())