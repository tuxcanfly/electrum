#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from distutils.core import setup
import os, sys, platform

# We redefine the method here so we can skip importing electrum itself and make it so we can do a pip install
def appdata_dir():
    """Find the path to the application data directory; add an electrum folder and return path."""
    if platform.system() == "Windows":
        return os.path.join(os.environ["APPDATA"], "Electrum")
    elif platform.system() == "Linux":
        return os.path.join(sys.prefix, "share", "electrum")
    elif (platform.system() == "Darwin" or
          platform.system() == "DragonFly"):
        return "/Library/Application Support/Electrum"
    else:
        raise Exception("Unknown system")

if sys.version_info[:3] < (2,6,0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

data_files = []

if platform.system() != 'Windows' and platform.system() != 'Darwin':
    data_files += [
        ('/usr/share/applications/',['electrum.desktop']),
        ('/usr/share/app-install/icons/',['electrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo'%lang):
            data_files.append(  ('/usr/share/locale/%s/LC_MESSAGES'%lang, ['locale/%s/LC_MESSAGES/electrum.mo'%lang]) )

data_files += [
    (appdata_dir(), ["data/noface.svg", "data/README"]),
    (os.path.join(appdata_dir(), "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir(), "dark"), [
        "data/dark/background.png",
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]

setup(name = "Electrum",
    version = "1.1.0",
    install_requires = ['slowaes','ecdsa'],
    package_dir = {'electrum': 'lib'},
    scripts= ['electrum'],
    data_files = data_files,
    py_modules = ['electrum.version',
                  'electrum.wallet',
                  'electrum.interface',
                  'electrum.gui',
                  'electrum.gui_qt',
                  'electrum.gui_lite',
                  'electrum.exchange_rate',
                  'electrum.icons_rc',
                  'electrum.mnemonic',
                  'electrum.pyqrnative',
                  'electrum.qrscanner',
                  'electrum.history_widget',
                  'electrum.bmp',
                  'electrum.msqr',
                  'electrum.util',
                  'electrum.i18n'],
    description = "Lightweight Bitcoin Wallet",
    author = "thomasv",
    author_email = "thomasv@gitorious",
    license = "GNU GPLv3",
    url = "http://electrum-desktop.com",
    long_description = """Lightweight Bitcoin Wallet""" 
)


