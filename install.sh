echo "Conecte su dispositivo ARDUINO UNO antes de continuar!"
echo -n "Presione [ENTER] para continuar...: "
read var_name
echo "Desmontando modulo CDC_ACM"
sudo rmmod cdc_acm
echo "Insertando modulo ARDUINO_USB"
sudo insmod driver/arduino_usb.ko
echo "Cambiando permisos en /dev/arduino"
sudo chmod 666 /dev/arduino
echo "Listo!"
