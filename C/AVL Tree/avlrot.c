#include <stdio.h>
#include <stdlib.h>
struct avlNode{
	int balance;
	int val;
	struct avlNode *l;
	struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode{
	avlNode *pval;
	struct qNode *nxt;
};
typedef struct qNode qNode;

struct llnode{
	avlNode val;
	struct llnode *next;
};typedef struct llnode llnode;

int getDepth(avlNode *root){
	int leftdepth = 0;
	int rightdepth = 0;
	
	if(root == NULL){return -1;}

	leftdepth = getDepth((*root).l);
	rightdepth = getDepth((*root).r);
	if(leftdepth > rightdepth){
		return leftdepth + 1;
	}
	else{
		return rightdepth + 1;
	}
}

int isAVL(avlNode **root){
	int leftdepth = 0;
	int rightdepth = 0;
	int imbalance = 0;

	leftdepth = getDepth((**root).l);
	rightdepth = getDepth((**root).r);
	imbalance = rightdepth - leftdepth;
	if(imbalance == 1 || imbalance == 0 || imbalance == -1){
		(**root).balance = imbalance;
		return 0;
	}
	else{
		return -1;
	}
}
int add_avl(avlNode **root, int val) {	
	if(root == NULL) {return -1;}
	if(*root == NULL) {
		*root = (avlNode *)malloc(sizeof(avlNode));
		if(*root == NULL){return -1;}
		(**root).val = val;
		(**root).balance = 0;
		(**root).l = NULL;
		(**root).r = NULL;
		return 0;
	}
	else {
		if(val>(**root).val){
			return add_avl(&((**root).r),val);
		}
		else if(val<(**root).val){
			return add_avl(&((**root).l),val);
		}
		else{
			return -1;
		}	
	}
}
int printTreeInOrder(avlNode *root){
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
int printLevelOrder(avlNode *root){
	llnode *x = NULL;
	int ret = 0;
	avlNode hold;
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
int llprint(llnode *root){
	llnode *point = root;

	while(point != NULL){
		printf("%d\n",(point->val).val);
		point = (point->next);
	}
	return 0;
}
int dequeue(llnode **root,avlNode *return_value){
	llnode *save = (**root).next;

	if(root==NULL){return -1;}
	if(*root==NULL){return -1;}
	*return_value = (**root).val;
	free(*root);
	*root = save;
	return 0;
}
int enqueue(llnode **root,avlNode val){
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
int getTreeInOrder(avlNode *root,llnode **ret){
	if(root == NULL){return -1;}
	if((*root).l != NULL){
		getTreeInOrder((*root).l,ret);
	}
	enqueue(ret,*root);
	if((*root).r != NULL){
		getTreeInOrder((*root).r,ret);
	}
	return 0;
}
int getLevelOrder(avlNode *root,llnode **return_val){
	llnode *x = NULL;
	int ret = 0;
	avlNode hold;
	enqueue(&x,*root);

	while(x != NULL){
		ret = dequeue(&x,&hold);
		if(ret != -1){
			enqueue(return_val,hold);
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
int rotate(avlNode **root,unsigned int Left0_Right1){
	avlNode *newroot = NULL;
	avlNode *oldroot = *root;
	if(root == NULL){return -1;}
	if(*root == NULL){return -1;}
	if(Left0_Right1 == 0){
		newroot = (**root).r;
		if(newroot == NULL){return -1;}
		(**root).r = (*newroot).l;
		(*newroot).l = *root;
		*root = newroot;		
	}
	else if(Left0_Right1 == 1){
		newroot = (**root).l;
		if(newroot == NULL){return -1;}
		(**root).l = (*newroot).r;
		(*newroot).r = *root;
		*root = newroot;
	}
	else{return -1;}
	return 0;
}
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
	int rootHeavy = 0;
	int childHeavy = 0;
	if(root == NULL){return -1;}
	if(*root == NULL){return -1;}
	if(MajLMinR0_MajRMinL1 == 0){
		isAVL(root);
		isAVL(&(**root).r);
		rootHeavy = (**root).balance;
		childHeavy = (*(**root).r).balance;
		if(childHeavy == rootHeavy){return -1;}
		rotate(&(**root).r,1);
		rotate(root,0);
	}
	else if(MajLMinR0_MajRMinL1 == 1){
                isAVL(root);
		isAVL(&(**root).l);
		rootHeavy = (**root).balance;
		childHeavy = (*(**root).l).balance;
		if(childHeavy == rootHeavy){return -1;}	
		rotate(&(**root).l,0);
		rotate(root,1);
	}
	return 0;
}
