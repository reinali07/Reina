#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int *store;
	unsigned int size;
	unsigned int end;
	int (*compare)(int x,int y);
} intHeap_T;

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
int hs(int *x,int size,int (*compare)(int x,int y)){
	int i = 0;
	int j = 0;
	int save = 0;
	intHeap_T heap;
	
	if(x==NULL){return -1;}
	if(compare==NULL){return -1;}
	if(size<0){return -1;}

	heap.size = size;
	heap.store = (int*)malloc(size*sizeof(int));
	heap.end = 0;
	heap.compare = (*compare);
	
	for(i=0;i<size;i++){
		store(&heap,x[i]);
	}
	for(i=0;i<size;i++){
		retrieve(&heap,&save);
		x[heap.end] = save;
	}
	return 0;
}
/*int main(void){
	int x[7] = {3,6,2,7,1,0,4};
	int i = 0;
	hs(x,7,gt);
	for (i=0;i<7;i++){
		printf("out[%d]=%d  ",i,x[i]);
	}
	printf("\n");
	return 0;
}*/
