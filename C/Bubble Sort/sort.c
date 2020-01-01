int bubbleSort(int *array, int size);
int swap(int *a,int *b);

int swap(int *a,int *b) {
	int old = *a;
	*a = *b;
	*b = old;
	return 0;
}
int bubbleSort(int *array, int size) {
	int swapped = 1;
	int i = 0;
	int r = 0;
	while(swapped == 1) {
		swapped = 0;
		for(i=1;i<size;i++) {
			if(array[i-1] > array[i]) {
				r = swap(&array[i-1],&array[i]);
				swapped = 1;
			}
		}
	}
	return 0;
}
