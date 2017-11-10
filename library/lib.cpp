/*H**********************************************************************
* FILENAME :        lib.cpp
*
* DESCRIPTION :
*       Biblioteca encargada de comunicarse con el driver del Arduino UNO
*
* PUBLIC FUNCTIONS :
*       int	drag	(int motor, int direccion, int steps)
*	int	drop	(int tiempo)
*
* NOTES :
*
*
* AUTHOR :    Santiago Vargas de Kruijf
*
* CHANGES :
*
* DATE: 5 Nov 2017
*
*H*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

FILE * device;   //Puntero al archivo que controla Arduino
using namespace std;

extern "C"
{

/*
	Metodo encargado de hacer la llamada para el movimiento de los servos en X o Y.
*/
int drag(int motor, int direccion, int steps){
	device = fopen("/dev/arduino","r+");
	if(device != NULL){
		if(direccion == 0) {
			fprintf(device,  "000_%d\n", steps);
			fclose(device);
			return 0;
		}

		fprintf(device,  "001_%d\n", steps);
		fclose(device);
		return 0;

	}
	else{
		printf("Lib: Error al comunicarse con driver\n");
		return -1;
	}
}


  /*
  	Metodo encargado de hacer la llamada para tocar la pantalla durante un determinado tiempo.
  */
  int push(int tiempo){
    device = fopen("/dev/arduino","r+");
  	if(device != NULL){
  		fprintf(device,  "100_%d\n", tiempo);
  		fclose(device);
  		return 0;
  	}
  	else{
  		printf("Lib: Error al comunicarse con driver\n");
  		return -1;
  	}
  }

  /*
  	Metodo encargado de hacer la llamada para tocar la pantalla e inmediatamente subir el dedo.
  */
  int touch(){
    device = fopen("/dev/arduino","r+");
  	if(device != NULL){
  		fprintf(device,  "200_%d\n",0);
  		fclose(device);
  		return 0;
  	}
  	else{
  		printf("Lib: Error al comunicarse con driver\n");
  		return -1;
  	}
  }

  int main(){
  	int i = drag(1,0,3200);
  	drag(1,1,3000);
  	drag(1,1,5000);
  	drag(1,0,200);
  	drag(1,1,1000);

  	return i;
  }

}
