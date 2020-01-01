#include <stdio.h>
#include <stdlib.h>
#include "avlrot.c"
int main(void){
	avlNode *root = NULL;
	avlNode *root1 = NULL;
	avlNode *root2 = NULL;

	add_avl(&root,6);
	add_avl(&root,2);
	add_avl(&root,7);
	add_avl(&root,1);
	add_avl(&root,4);
	add_avl(&root,3);
	add_avl(&root,5);
	printf("root\n");
	printLevelOrder(root);
	printf("rotate\n");	
	dblrotate(&root,1);
	printLevelOrder(root);
	printf("in order\n");
	printTreeInOrder(root);

	add_avl(&root1,5);
	add_avl(&root1,2);
	add_avl(&root1,10);
	add_avl(&root1,8);
	add_avl(&root1,12);
	add_avl(&root1,7);
	add_avl(&root1,9);
	printf("root1\n");
	printLevelOrder(root1);
	printf("rotate\n");
	dblrotate(&root1,0);
	printLevelOrder(root1);
	printf("in order\n");
	printTreeInOrder(root1);
	
	add_avl(&root2,5);
	add_avl(&root2,2);
	add_avl(&root2,6);
	add_avl(&root2,3);
	add_avl(&root2,12);
	add_avl(&root2,14);
	printf("root1\n");
	printLevelOrder(root2);
	printf("rotate\n");
	dblrotate(&root2,0);
	printLevelOrder(root2);
	printf("in order\n");
	printTreeInOrder(root2);
	return 0;
}
