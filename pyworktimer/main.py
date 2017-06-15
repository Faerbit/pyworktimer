import sys
from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtCore import Slot
from qtpy.QtCore import QLocale

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        changeAction = menu.addAction(self.tr("Change"))
        changeAction.triggered.connect(self.change)
        exitAction = menu.addAction(self.tr("Exit"))
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        self.setContextMenu(menu)
        self.setToolTip("pyworktimer")
        
    @Slot()
    def change(self):
        self.setIcon(QtGui.QIcon("icons/icon2.png"))


def main():
    translator = QtCore.QTranslator()
    system_language = QLocale.languageToString(QLocale.system().language())
    print("System Locale: {}".format(system_language))
    print("Localization loaded: {}".format(
        translator.load("{}.qm".format(system_language.lower()), "translations")))
    if translator.isEmpty():
        print("Fallback Localization loaded: {}".format(
                translator.load("english.qm", "translations")))
    app = QtWidgets.QApplication(sys.argv)
    app.installTranslator(translator)

    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("icons/icon.png"), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
