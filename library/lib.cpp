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

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"

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
		if(motor==0){
			if(direccion == 0) {
				fprintf(device,  "000_%d\n", steps);
				fclose(device);
				return 0;
			}

			fprintf(device,  "001_%d\n", steps);
			fclose(device);
			return 0;
		} else {

			if(direccion == 1) {
				fprintf(device,  "010_%d\n", steps);
				fclose(device);
				return 0;
			}

			fprintf(device,  "011_%d\n", steps);
			fclose(device);
			return 0;
		}
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
  	drag(0,0,1000);	// Servo flotante izquierda
  	drag(0,1,1000);// Servo flotante derecha
		drag(1,0,1000);	// Servo principal hacia atras
		drag(1,1,1000);	// Servo principal hacia adelante
  	return 0;
  }

}
