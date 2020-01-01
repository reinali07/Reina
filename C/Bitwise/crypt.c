#include <stdio.h>
#include <stdlib.h>

unsigned char FSR(unsigned char x){
	unsigned char oldbit0 = x & 0x1; /*extract bit 0*/
	unsigned char r = x >> 1; /*shift right*/
	unsigned char newbit7 = oldbit0 << 7; /*move bit0 to the bit7 pos*/
	r = r | newbit7; /*rotate old value of bit0 into bit7 pos*/
	return r;
}
unsigned char prng(unsigned char x, unsigned char pattern){
	unsigned char r = FSR(x);
	r = r^pattern;
	return r;
}
int crypt(char *data,unsigned int size,unsigned char password){
	unsigned char prngVal;
	int i = 0;
	if(password == 0){
		return -1;
	}
	prngVal = password;
	for(i=0;i<size;i++){
		prngVal = prng(prngVal,0xb8);
		data[i] = data[i]^prngVal;
	}
	return 0;
}
/*
int main(void){
	unsigned char z = 'a';
	char data[4] = "lol\0";
	unsigned char password = 'c';
	
	int i =0;
	for(i=0;i<20;i++){
		z = prng(z,0xb8);
		printf("%c\n",z);
	}
	for(i=0;i<4;i++){
		printf("%c\n",data[i]);
	}
	crypt(data,3,password);
	printf("lol\n");
	for(i=0;i<4;i++){
		printf("%c\n",data[i]);
	}
	return 0;
}*/
