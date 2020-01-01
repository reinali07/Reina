#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int *store;
	unsigned int size;
	unsigned int end;
	int (*compare)(int x,int y);
} intHeap_T;

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
int store(intHeap_T* heap, int value) {
	int node = (*heap).end;
	int parent = (node-1)/2;
	int old = 0;
	int i = 0;
	if(heap == NULL){return -1;}
	(*heap).store[(*heap).end] = value;
	(*heap).end += 1;
	while((*heap).compare(value,(*heap).store[parent]) == 1 && parent >= 0){
		(*heap).store[node] = (*heap).store[parent];
		(*heap).store[parent] = value;
		node = parent;
		parent = (parent-1)/2;
	}
	return 0;
}
int retrieve(intHeap_T* heap, int *rvalue) {
	int lc = 1;
	int rc = 2;
	int node = 0;
	int i = 0;
	int priorchild = lc;
	int key = (*heap).store[(*heap).end-1];
	
	if(heap == NULL){return -1;}
	if(rvalue == NULL){return -1;}
	
	*rvalue = (*heap).store[0];
	(*heap).store[0] = (*heap).store[(*heap).end-1];
	(*heap).end -= 1;
	while(1){
		priorchild = lc;
		if(priorchild >= (*heap).end){break;}
		if((*heap).compare((*heap).store[rc],(*heap).store[lc])==1){
			priorchild = rc;
		}
		if((*heap).compare((*heap).store[priorchild],key)==1){
			(*heap).store[node] = (*heap).store[priorchild];
			(*heap).store[priorchild] = key;
			node = priorchild;
			lc = priorchild*2+1;
			rc = priorchild*2+2;
		}
		else{break;}
	}
	return 0;
}
/*int main(void){
	intHeap_T heap;
	int i = 0;
	int x = 0;
	heap.store=(int*)malloc(1000*sizeof(int));
	heap.size=1000;
	heap.end=0;
	heap.compare = gt;
	store(&heap,3);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	store(&heap,6);
	store(&heap,2);
	store(&heap,7);
	store(&heap,1);
	store(&heap,0);
	store(&heap,4);
	for (i=0;i<heap.end;i++){
		printf("out[%d]=%d  ",i,heap.store[i]);
	}
	printf("\n");
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	retrieve(&heap,&x);
	printf("x=%d\n",x);
	for (i=0;i<heap.end;i++){
		printf("out[%d]=%d  ",i,heap.store[i]);
	}
	printf("\n");
	return 0;
}*/
