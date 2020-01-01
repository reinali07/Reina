#include "heap.c"
#include <stdio.h>
#include <stdlib.h>


int main(void){
	HeapType *x;
	int i = 0;
	int size=0;
	int key = 0;
	int* output;
	initHeap(x,15);	
	for(i=0;i<17;i++){
		/*((*x).store)[i] = i;*/
		addHeap(x,i);
	}
	for(i=0;i<(*x).end;i++){
		printf("%d\n",((*x).store)[i]);
	}
	printf("traverse in order: \n");
	inorder(x,&output,&size);
	for(i=0;i<(*x).end;i++){
		printf("%d\n",output[i]);
	}
	printf("traverse preorder: \n");
	preorder(x,&output,&size);
	for(i=0;i<(*x).end;i++){
		printf("%d\n",output[i]);
	}
	printf("traverse postorder: \n");
	postorder(x,&output,&size);
	for(i=0;i<(*x).end;i++){
		printf("%d\n",output[i]);
	}
	i = findHeap(x,15);
	printf("i is %d\n",i);
	delHeap(x,&key);
	for(i=0;i<(*x).end;i++){
		printf("%d\n",((*x).store)[i]);
	}
	printf("i is %d\n",i);
	return 0;
}
