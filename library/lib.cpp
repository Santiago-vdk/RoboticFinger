/*H**********************************************************************
* FILENAME :        lib.cpp             
*
* DESCRIPTION :
*       Biblioteca encargada de comunicarse con el driver del Arduino UNO
*
* PUBLIC FUNCTIONS :
*       int	mov	(int motor, int direccion, int steps)
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
int mov(int motor, int direccion, int steps){
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
		printf("File no found\n");
		return -1;
	}
}


/*
	Metodo encargado de hacer la llamada para bajar el dedo en la posicion actual.
*/
int drop(int tiempo){
	return 0;	
}

int main(){
	int i = mov(1,0,3200);
	mov(1,1,3000);
	mov(1,1,5000);
	mov(1,0,200);
	mov(1,1,1000);

	return i;
}

}






