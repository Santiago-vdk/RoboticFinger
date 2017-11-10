
all:
	$(MAKE) -C driver
	$(MAKE) -C library

install:
	@echo "Instalando..."
	@echo "Recuerde que debe haber llamado antes 'make'"
	chmod 777 install.sh
	./install.sh

uninstall:
		@echo "Desinstalando..."
		chmod 777 uninstall.sh
		./uninstall.sh
