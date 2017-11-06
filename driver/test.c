#include <stdio.h>
#include <stdlib.h>
#include <string.h>


FILE * device;   //pointer for a file handled to driver

void main(){
	mov(1,0,"3200");
}

int mov(int motor, int direccion, char * steps){

	device = fopen("/dev/arduino","r+");
	if(device != NULL){
		if(direccion == 0) {
			fprintf(device, "%s", "mov_m1_izq_" + steps + "\n");
			fclose(device);
			return 0;
		}

		fprintf(device, "%s", "mov_m1_izq_" + steps + "\n");
		fclose(device);
		return 0;	
		
	}
	else{
		printf("File no found\n");
		return -1;
	}

}




