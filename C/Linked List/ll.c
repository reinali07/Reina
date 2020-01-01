#include <stdio.h>
#include <stdlib.h>
#include "ll.h"

/* One of the lessons here is to see that if we want to use a function to malloc something that
 * is a POINTER in the CALLER of the function, then we must send in the ADDRESS of the POINTER
 * to that function.
 * 
 * Recap: if we want to use a function to modify a VARIABLE in the caller
 *        then the CALLER needs to send in the ADDRESS of the VARIABLE
 *
 * Similarly: if we want to use a function to modify a POINTER in the caller
 *            then the CALLER needs to send in the ADDRESS of the POINTER
 *
 * In the code below, ll_add_to_head and ll_add_to_tail are dynamically creating new
 * nodes to be added to the linked list. Any dynamic creation of a node must be via
 * malloc.
 */

int ll_add_to_head( llnode **head, int val) {
    llnode *old_head;
   if (head == NULL) {
      return -1;
   }
	old_head = *head;

   *head = ( llnode *) malloc(sizeof( llnode));
   (**head).val = val;
	(**head).next = old_head;
	return 0;
}

int ll_add_to_tail( llnode **head, int val) {
   if (head == NULL) {
      return -1;
   }
   if (*head == NULL) {
      *head = ( llnode *) malloc(sizeof( llnode));
      (**head).val = val; 
      (**head).next = NULL;
      return 0;
   } else { /* recursively call ll_add_to_tail until we get to the tail
					which is the point where the pointer is NULL */
      return ll_add_to_tail(&((**head).next), val); /*#&((**head).next) is the address of the next llnode ("head" is the current one)*/
   }
}

int ll_print( llnode *p) {
   if (p==NULL) {
      return 0;
   } else {
      printf("val = %d\n",p->val);
      return ll_print(p->next);
   }
}

int ll_free( llnode *p) {
   if (p==NULL) {
      return -1;
   } else {
       llnode *f=p->next;
      free(p);
      return ll_free(f);
   }
}

int ll_find_by_value(llnode *pList, int val){
	if(pList == NULL){
		return -1;
	}
	if((*pList).val == val){
		return 0;
	}
	else if((*pList).next == NULL) {
		return -1;
	}
	else{
		return ll_find_by_value((*pList).next,val);
	}
}

int ll_del_from_tail(llnode **ppList) {
	int r = 0;
	llnode nextNode = *((**ppList).next);

	if(ppList == NULL){return -1;}
	
	if(nextNode.next == NULL) {
		(**ppList).next = NULL;
		r = ll_free((**ppList).next); /*free nextNode, which is the last node*/
		return 0;
	}
	else{
		return ll_del_from_tail(&((**ppList).next));
	}
}

int ll_del_from_head(llnode **ppList) {
	int r = 0;
	llnode *nextNode = &(*((**ppList).next));
	**ppList = *nextNode;
	(*nextNode).next = NULL;
	r = ll_free(nextNode);
	return 0;
}

int ll_del_by_value(llnode **ppList,int val) {
	int r = 0;
	llnode *nextNode = &(*((**ppList).next));
	llnode *newNext = (*nextNode).next;
	if(ppList == NULL){return -1;} /*obligatory check*/
	if(ll_find_by_value(*ppList,val) == -1) {
		return -1;
	}
	if((*nextNode).val == val) {
		(**ppList).next = newNext;
		(*nextNode).next = NULL;
		r = ll_free(nextNode); /*free this one */
		return 0;
	}
	else{
		return ll_del_by_value(&((**ppList).next),val);
	}
}

int ll_insert_in_order(llnode **ppList,int val) {
	int r = 0;
	if(ppList == NULL) {return -1;}
	if(*ppList == NULL) {
		r = ll_add_to_head(ppList,val);
		return 0;
	}
	else if(val <= (**ppList).val) {
		r = ll_add_to_head(ppList,val);
		return 0;
	}
	else if((**ppList).next != NULL){
		return ll_insert_in_order(&((**ppList).next),val);
	}
	else{
		(**ppList).next = (llnode *)malloc(sizeof(llnode));
		(*((**ppList).next)).val = val;
		(*((**ppList).next)).next = NULL;
		return 0;
	}
}

int ll_concat(llnode **pSrcA,llnode **pSrcB) {
	int r = 0;
	llnode *broot = *pSrcB;

	if(pSrcA==NULL || pSrcB == NULL) {return -1;}

	if((**pSrcA).next == NULL){
		(**pSrcA).next = broot;
		return 0;
	}
	else{
		return ll_concat(&((**pSrcA).next),pSrcB);
	}
}

int ll_sort(llnode **ppList){
	int r = 0;
	int i = 0;
	int swapped = 1;
	llnode *prev = *ppList;
	llnode *curr = *ppList;
	llnode *forw = (*curr).next;
	llnode oldprev = *prev;
	llnode oldcurr = *curr;
	llnode oldforw = *forw;
	if(ppList == NULL){return -1;}

	r = ll_add_to_head(ppList,0);
	while(swapped == 1){
		printf("\n\nswapped was true so we go again\n");
		swapped = 0;
		prev = *ppList;
		curr = (*prev).next;
		forw = (*curr).next;
		oldprev = *prev;
		oldcurr = *curr;
		oldforw = *forw;
		while((*curr).next != NULL){
			if((*curr).val > (*forw).val){
				(*prev).next = forw;
				(*forw).next = curr;
				(*curr).next = oldforw.next;
				swapped = 1;
				/*r = ll_print(*ppList);*/
				printf("one iteration switched %d and %d\n",(*forw).val,(*curr).val);
			}
			prev = (*prev).next;
			forw = (oldforw).next;
			curr = (*prev).next;
			oldprev = *prev;
			oldcurr = *curr;
			if(forw != NULL){
				oldforw = *forw;
			}
			else{
				oldforw = *curr;
			}
			printf("p is %d, c is %d, f is %d\n",oldprev.val,oldcurr.val);
			printf("swapped is %d\n",swapped);
		}
	}
	r = ll_del_from_head(ppList);
	return 0;
}
