#include <stdio.h>
#include <stdlib.h>
#include <string.h>


FILE * device;   //pointer for a file handled to driver

void main(){
	device = fopen("/dev/arduino","r+");
	if(device != NULL){
		
		fprintf(device, "%c", 'p');
		sleep(2);
fprintf(device, "%c", 'a');

		fclose(device);
	}
	else{
		printf("File no found\n");
	}

}

