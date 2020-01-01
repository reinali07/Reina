/* This is an example of how to use a linked list as a
 * dynamic container to store data that is input with an
 * unknown number of items.
 *
 * Note how we get the data:
 * -while loop (because the number of iterations is unknown)
 * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 * -for each iteration, we stuff the input data into a linked list
 *
 * Usage:
 * gcc getData.c
 * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 * should report 10 items read and dump it out
 * -> white space is ignored (space, tab, return)
 *
 * Assignment:
 * -modify this code so that it handles input "char" data
 *  rather than ints (trivial modification)
 * echo "abcdef" | ./a.out
 * should report 7 items read
 * (white space is representable by the char hence the
 * final return you enter is stored as a char)
 */

#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

char llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

char llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
    return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
    return 0;
      }
   }
}
int push(llnode **x,char value) {
   return llnode_add_to_tail(x,value);
}

int pop(llnode **x, char *return_value) {
   llnode *p=NULL;
   llnode **pp=NULL;
   if (x==NULL) { return -1; }
   if (*x==NULL) { return -1; }
   pp=x;
   while (1) {
      if ((*pp)->next == NULL) { break; }
      else { pp=&((*pp)->next); }
   }
   *return_value = (*pp)->value;
   free(*pp);
   *pp=NULL;
   return 0;
}

int main(void) {
   int n=0;
   char  value=0;
   char ovalue=0;
   int  rvalue=0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      if ((value=='(') || (value=='[') || (value=='{')) {
         push(&input_list,value);
         //llnode_print_from_head(input_list);
      } else if (value==')') {
        pop(&input_list,&ovalue);
        //printf("DEBUGA: %c\n",ovalue);
        if (ovalue != '(') { printf("FAIL,%d\n",n); return -1; }
      } else if (value==']') {
        pop(&input_list,&ovalue);
        //printf("DEBUGB: %c\n",ovalue);
        if (ovalue != '[') { printf("FAIL,%d\n",n); return -1; }
      } else if (value=='}') {
        pop(&input_list,&ovalue);
        //printf("DEBUGC: %c\n",ovalue);
        if (ovalue != '{') { printf("FAIL,%d\n",n); return -1; }
      }
      n=n+1;
   }
   if (pop(&input_list,&ovalue) == -1) { printf("PASS\n"); } else { printf("FAIL,%d\n",n); }
   return 0;
}
