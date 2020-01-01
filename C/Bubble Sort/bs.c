#include <stdio.h>
#include <stdlib.h>
int bs(int *x,int size,int (*compare)(int x,int y)){
	int swapped = 1;
	int i = 0;
	int temp = 0;
	while(swapped == 1){
		swapped = 0;
		for(i=0;i<size-1;i++){
			if((*compare)(x[i],x[i+1]) == 1){
				temp = x[i];
				x[i] = x[i+1];
				x[i+1] = temp;
				swapped = 1;
			}
		}
	}
	return 0;
}
int lt(int x,int y){
	if(x<y){
		return 1;
	}
	else{
		return 0;
	}
}
int gt(int x,int y){
	if(x>y){
		return 1;
	}
	else{
		return 0;
	}	
}
/*int main(void){
	int i=0;
	int vals[10];
	for (i=0;i<10;i=i+1){
		vals[i] = 100-i;
	}
	for (i=0;i<10;i=i+1){
		printf("in[%d]=%d\n",i,vals[i]);
	}
	bs(vals,10,lt);
	for (i=0;i<10;i++){
		printf("out[%d] = %d\n",i,vals[i]);
	}	
	return 0;
}*/
