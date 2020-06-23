from model import *
from widok import *
from kontroler import Controler
import sys



"""
            Wywołują się 2 maszyny. Check why.
"""

if __name__ == '__main__':
    app = QApplication([])
    view = MainWindow()
    maszyna = Machine()
    app.setStyleSheet(StyleSheet)
    view.show()
    Controler(w=view, m=maszyna)
    sys.exit(app.exec_())