#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int *store;
	unsigned int size;
	unsigned int end;
} HeapType;

int initHeap(HeapType *pHeap,int size){
	int i = 0;
	if(pHeap == NULL){return -1;}
	(*pHeap).store = (int *)malloc(size*sizeof(int));
	if((*pHeap).store == NULL){return -1;}
	(*pHeap).size = size;
	(*pHeap).end = 0;
	return 0;
}
int inorder(HeapType *pHeap, int **output, int *o_size){
	int leftmost = 0;
	int i = 0;
	int increment = 2;
	int j = 0;
	int start = 0;
	int k = 1;
	if(pHeap == NULL){return 01;}
	leftmost = ((*pHeap).size-1)/2;
	*output = (int *)malloc((*pHeap).size*sizeof(int));
	if(*output == NULL){return -1;}
	while(leftmost != 0){
		j = 0;
		for(i=start;i<(*pHeap).size;i = i+increment){
			(*output)[i] = ((*pHeap).store)[leftmost+j];
			j = j+1;
		}
		start = start + k;
		k = k*2;
		increment = increment*2;
		leftmost = (leftmost-1)/2;
	}
	(*output)[((*pHeap).size)/2] = ((*pHeap).store)[0];
	*o_size = (*pHeap).size;
	return 0;
}

int preorder(HeapType *pHeap, int **output, int *o_size){
	int oIndex = 0;
	if(pHeap == NULL){return -1;}
	if(output == NULL){return -1;}
	*output = (int *)malloc((*pHeap).size*sizeof(int));
	if(*output == NULL){return -1;}
	prehelper(pHeap,*output,0,&oIndex);
	*o_size = (*pHeap).end;
	return 0;
}
int prehelper(HeapType *pHeap,int *output, int hIndex, int *oIndex){
	if(pHeap == NULL){return -1;}
	if(hIndex > (*pHeap).end - 1){return -1;}
	
	output[*oIndex] = (*pHeap).store[hIndex];
	/*printf("output @ oIndex %d\n oindex is %d\n hIndex is %d\n value at hIndex is %d\n",output[*oIndex],*oIndex,hIndex,(*pHeap).store[hIndex]);
	*/
	*oIndex = *oIndex + 1;
	prehelper(pHeap,output,hIndex*2+1,oIndex);
	prehelper(pHeap,output,hIndex*2+2,oIndex);
	return 0;
}
int postorder(HeapType *pHeap, int **output, int *o_size){
	int oIndex = 0;
	int i = 0;
	if(pHeap == NULL){return -1;}
	if(output == NULL){return -1;}
	*output = (int *)malloc((*pHeap).size*sizeof(int));
	if(*output == NULL){return -1;}
	
	posthelper(pHeap,*output,0,&oIndex);
	*o_size = (*pHeap).end;
	return 0;
}
int posthelper(HeapType *pHeap,int *output, int hIndex, int *oIndex){
	if(pHeap == NULL){return -1;}
	if(hIndex > (*pHeap).end - 1){return -1;}
	
	
	posthelper(pHeap,output,hIndex*2+1,oIndex);
	posthelper(pHeap,output,hIndex*2+2,oIndex);
	
	output[*oIndex] = (*pHeap).store[hIndex];	
	/*printf("output @ oIndex %d\n oindex is %d\n",output[*oIndex],*oIndex);*/
	*oIndex = *oIndex + 1;
	return 0;
}
int addHeap(HeapType *pHeap, int key){
	int cindex = (*pHeap).end;	
	int pindex = (cindex - 1)/2;
	int i = 0;	
	if(pHeap==NULL){return -1;}
	if((*pHeap).end == (*pHeap).size){return -1;}
	(*pHeap).end = (*pHeap).end + 1;
	((*pHeap).store)[cindex] = key;
	while(key >= ((*pHeap).store)[pindex] && pindex != cindex){
		((*pHeap).store)[cindex] = ((*pHeap).store)[pindex];
		((*pHeap).store)[pindex] = key;
		cindex = pindex;
		pindex = (cindex - 1)/2;
	}
	return 0;
}
int findHeap(HeapType *pHeap, int key){
	int i = 0;
	if(pHeap==NULL){return -1;}
	for(i=0;i<(*pHeap).end;i++){
		if(((*pHeap).store)[i] == key){
			return 1;
		}
	}
	return 0;
}
int getGreater(HeapType *pHeap, int index, int *gindex){
	if(pHeap==NULL){*gindex = -1;return -1;}
	if(index*2+1 < (*pHeap).end && ((*pHeap).store)[index] < ((*pHeap).store)[index*2+1]){
		*gindex = index*2+1;
	}
	else if(index*2+2 < (*pHeap).end && ((*pHeap).store)[index] < ((*pHeap).store)[index*2+2]){
		*gindex = index*2+2;
	}
	else{
		*gindex = -1;
	}
	return 0;
}
int delHeap(HeapType *pHeap,int *key){
	int end = (*pHeap).end;
	int node = 0;
	int this = 0;
	int greater = 0;
	if(pHeap == NULL){return -1;}
	if((*pHeap).end == 0){return -1;}
	(*pHeap).end = (*pHeap).end - 1;
	if((*pHeap).end > 1){
		*key = ((*pHeap).store)[0];
		((*pHeap).store)[0] = ((*pHeap).store)[end-1];
		node = ((*pHeap).store)[0];
		while(1){
			getGreater(pHeap,this,&greater);
			if(greater == -1){break;}
			((*pHeap).store)[this] = ((*pHeap).store)[greater];
			((*pHeap).store)[greater] = node;
			this = greater;
		}
	}
	return 0;
}
/*int main(void){
	HeapType *x;
	int i = 0;
	int size=0;
	int key = 0;
	int* output;
	initHeap(x,15);	
	for(i=0;i<17;i++){
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
}*/
