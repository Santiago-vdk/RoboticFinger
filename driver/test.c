#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

FILE * device;   //pointer for a file handled to driver
using namespace std;
int mov(int motor, int direccion, int steps){

	device = fopen("/dev/arduino","r+");
	if(device != NULL){
		if(direccion == 0) {
			

			fprintf(device,  "mov_m1_izq_%d\n", steps);
			fclose(device);
			return 0;
		}

		fprintf(device,  "mov_m1_der_%d\n", steps);
		fclose(device);
		return 0;	
		
	}
	else{
		printf("File no found\n");
		return -1;
	}

}

int main(){
	int i = mov(1,0,3200);
	return i;
}








