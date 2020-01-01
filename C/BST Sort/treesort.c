#include <stdio.h>
#include <stdlib.h>
struct bstNode{
	int val;
	struct bstNode *l;
	struct bstNode *r;
};
typedef struct bstNode bstNode;
struct llnode {
	bstNode val;
	struct llnode *next;
};
typedef struct llnode llnode;

int dequeue(llnode **root,bstNode *return_value){
	llnode *save = (**root).next;

	if(root==NULL){return -1;}
	if(*root==NULL){return -1;}
	*return_value = (**root).val;
	free(*root);
	*root = save;
	return 0;
}
int enqueue(llnode **root,bstNode val){
	if(root == NULL){return -1;}
	if(*root == NULL) {
		*root = (llnode *)malloc(sizeof(llnode));
		(**root).val = val;
		(**root).next = NULL;
		return 0;
	}
	else{
		return enqueue(&((**root).next),val);
	}
}
int printLevelOrder(bstNode *root){
	llnode *x = NULL;
	int ret = 0;
	bstNode hold;
	enqueue(&x,*root);

	while(x != NULL){
		ret = dequeue(&x,&hold);
		if(ret != -1){
			printf("%d\n",hold.val);
		}
		if(hold.l != NULL){
			enqueue(&x,*(hold.l));
		}
		if(hold.r != NULL){
			enqueue(&x,*(hold.r));
		}
	}
	return 0;
}
int add_bst(bstNode **root, int val) {	
	if(root == NULL) {return -1;}
	if(*root == NULL) {
		*root = (bstNode *)malloc(sizeof(bstNode));
		if(*root == NULL){return -1;}
		(**root).val = val;
		(**root).l = NULL;
		(**root).r = NULL;
		return 0;
	}
	else {
		if(val>(**root).val){
			return add_bst(&((**root).r),val);
		}
		else if(val<(**root).val){
			return add_bst(&((**root).l),val);
		}
		else{
			return -1;
		}	
	}
}
int printTreeInOrder(bstNode *root){
	if(root == NULL){return -1;}
	if((*root).l != NULL){
		printTreeInOrder((*root).l);
	}
	printf("%d\n",(*root).val);
	if((*root).r != NULL){
		printTreeInOrder((*root).r);
	}
	return 0;
}
int getNumberOfElements(bstNode *root,int *accum){
	if(root == NULL){
		return -1;
	}
	*accum = *accum + 1;
	if((*root).l != NULL){
		getNumberOfElements((*root).l,accum);
	}
	if((*root).r != NULL){
		getNumberOfElements((*root).r,accum);
	}
	return 0;
}
int getHeight(bstNode *root){
	int lheight = 0;
	int rheight = 0;
	if(root == NULL){return 0;}
	lheight = getHeight((*root).l);
	rheight = getHeight((*root).r);
	if(lheight>rheight)
		return lheight+1;
	else{
		return rheight+1;
	}
}
int main(void){
	int n = 0;
	int value = 0;
	int rvalue = 0;
	bstNode *input_list=NULL;

	while (scanf("%d",&value) != EOF) {
		n=n+1;
		add_bst(&input_list,value);
	}
	printTreeInOrder(input_list);
	/*printLevelOrder(input_list);
	printLevelOrder(input_list);*/

	return 0;	
}
