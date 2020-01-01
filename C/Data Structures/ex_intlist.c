#include <stdio.h>
#include <stdlib.h>
struct intlist{
	int *x;
	int end;
	int len;
};
typedef struct intlist intlist;

int init(intlist *l, int len){
	if(l==NULL){return -1;}
	(*l).x = (int *)malloc(len * sizeof(int));
	if((*l).x == NULL){return -1;}
	(*l).end = -1;
	(*l).len = len;
	return 0;
}

int add_to_end(intlist *l,int val){
	if(l == NULL){return -1;}
	if((*l).x == NULL){return -1;}
	((*l).x)[(*l).end+1] = val;
	(*l).end = (*l).end + 1;
	return 0;
}
int add_to_start(intlist *l, int val){
	int *temp = NULL;
	int i = 0;

	if(l == NULL){return -1;}
	if((*l).x==NULL){return -1;}
	temp = (int *)malloc((*l).len * sizeof(int));
	if(temp == NULL){return -1;}
	for(i=0;i<=(*l).end;i++){
		temp[i] = ((*l).x)[i];
	}
	((*l).x)[0] = val;
	(*l).end = (*l).end + 1;
	for(i=0;i<=(*l).end;i++){
		((*l).x)[i+1] = temp[i];
	}
	return 0;
}
int insert_after(intlist *l, int insert_val,int val){
	int *temp = NULL;
	int i = 0;
	int found = 0;
	int x = 0;

	if(l == NULL){return -1;}
	if((*l).x == NULL){return -1;}
	temp = (int *)malloc((*l).len * sizeof(int));
	if(temp==NULL){return -1;}
	if(insert_val > (*l).len){return -1;}

	for(i=insert_val+1;i<=(*l).end;i++){
		temp[i-insert_val-1] = ((*l).x)[i];
	}
		
	((*l).x)[insert_val+1] = val;
	(*l).end = (*l).end + 1;
	for(i=insert_val+2;i<=(*l).end;i++){
		((*l).x)[i] = temp[i-insert_val-2];
	}
	return 0;	
}
int printarray(intlist l){
	int i = 0;
	printf("printing: \n");
	for(i=0;i<=l.end;i++){
		printf("%d\n",(l.x)[i]);
	}
	return 0;
}
/*
int main(void){
	intlist a;
	
	init(&a,20);
	add_to_end(&a,1);
        printarray(a);
        add_to_end(&a,2);
        printarray(a);
        add_to_start(&a,3);
        printarray(a);
        add_to_start(&a,4);
        printarray(a);
        insert_after(&a,1,5);
	printarray(a);
	return 0;
}*/
