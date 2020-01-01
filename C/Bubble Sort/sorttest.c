#include <stdio.h>
#include "sort.c"

int main(void) {
	int m[4] = {2,5,3,1};
	int a[1] = {0};
	int b[10] = {3,5,2,7,5,24,64,2,6,3};
	int c[7] = {1,2,3,4,5,6,7};
	int d[2] = {5,2};
	int x = 0;
	
	x = bubbleSort(m,4);
	for(x=0;x<4;x++) {
		printf("%3d",m[x]);
	}
	printf("\n");
	x= bubbleSort(a,1);
	for(x=0;x<1;x++) {
                printf("%3d",a[x]);
        }
        printf("\n");
	x=bubbleSort(b,10);
	for(x=0;x<10;x++) {
                printf("%3d",b[x]);
        }
        printf("\n");
	x = bubbleSort(c,7);
	for(x=0;x<7;x++) {
                printf("%3d",c[x]);
        }
        printf("\n");
	x = bubbleSort(d,2);
	for(x=0;x<2;x++) {
                printf("%3d",d[x]);
        }
        printf("\n");
}
