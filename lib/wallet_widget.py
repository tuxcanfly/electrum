from PyQt4.QtGui import *
from i18n import _
from util import user_dir
from wallet import *
import glob, os, re

class WalletWidget(QTreeWidget):

    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)
        self.setColumnCount(2)
        self.setHeaderLabels([_("Wallet"), _("Balance")])
        self.setIndentation(0)

        wallet_dir = user_dir()
        # Make wallet directory if it does not yet exist.
        if not os.path.exists(wallet_dir):
            os.mkdir(wallet_dir)
        else:
          for wallet_file in glob.glob( os.path.join(wallet_dir, '*.dat') ):
            sanitized_name = wallet_file.replace(wallet_dir + "/", "")
            full_name = sanitized_name
            sanitized_name = sanitized_name.replace(".dat","")
            sanitized_name = sanitized_name.title()
            self.append(sanitized_name , "Not available", full_name)

    def append(self, file_name, label, full_name):
        wallet_file = user_dir() + "/" + full_name
        item = QTreeWidgetItem([file_name, label, full_name])
        self.insertTopLevelItem(0, item)

