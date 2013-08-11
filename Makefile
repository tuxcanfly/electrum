PYTHON=`which python`
DESTDIR=/
BUILDIR=$(CURDIR)/debian/electrum
PROJECT=electrum
VERSION=1.8.1

all:
	@echo "make source - Create source package"
	@echo "make install - Install on local system"
	@echo "make buildrpm - Generate a rpm package"
	@echo "make builddeb - Generate a deb package"
	@echo "make clean - Get rid of scratch and byte files"

gui/icons_rc.py:
	pyrcc4 icons.qrc -o gui/icons_rc.py

source: gui/icons_rc.py
	$(PYTHON) setup.py sdist $(COMPILE)

install: gui/icons_rc.py
	$(PYTHON) setup.py install --root $(DESTDIR) $(COMPILE)

buildrpm: gui/icons_rc.py
	$(PYTHON) setup.py bdist_rpm --post-install=rpm/postinstall --pre-uninstall=rpm/preuninstall

builddeb: gui/icons_rc.py
	# build the source package in the parent directory
	# then rename it to project_version.orig.tar.gz
	$(PYTHON) setup.py sdist $(COMPILE) --dist-dir=../ --prune
	rename -f 's/$(PROJECT)-(.*)\.tar\.gz/$(PROJECT)_$$1\.orig\.tar\.gz/' ../*
	# build the package
	dpkg-buildpackage -i -I -rfakeroot -S

clean:
	$(PYTHON) setup.py clean
	fakeroot $(MAKE) -f $(CURDIR)/debian/rules clean
	rm -rf build/ MANIFEST
	rm -f gui/icons_rc.py
	find . -name '*.pyc' -delete
