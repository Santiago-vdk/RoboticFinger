obj-m += arduino_usb.o

all:
	make -k -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules 

clean:
	make -k -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
