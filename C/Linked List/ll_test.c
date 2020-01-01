#include <stdio.h>
#include "ll.h"

int main(void) {
   llnode *root = NULL;
   llnode *rootb = NULL;
   int r=0;
   int i=0;

   r=ll_add_to_tail(&rootb,100);
   r=ll_add_to_tail(&rootb,200);
   r=ll_add_to_tail(&rootb,300);
   r=ll_print(rootb);
   printf("List A\n");
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&root,i*100);
   }
   r=ll_print(root);
   r=ll_free(root);

   printf("List B\n");
	root=NULL;
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_head(&root,i*100);
   }
   r=ll_find_by_value(root,500);
   printf("%d\n",r);
   r=ll_del_by_value(&root,500);
   r=ll_del_from_tail(&root);
   r=ll_del_from_head(&root);
   r=ll_insert_in_order(&root,1000);
   r=ll_insert_in_order(&root,500);
   r=ll_insert_in_order(&root,900);
   r=ll_concat(&root,&rootb);
   r=ll_print(root);
   r=ll_sort(&root);
   r=ll_print(root);
   r=ll_free(root);

   return 0;
}
