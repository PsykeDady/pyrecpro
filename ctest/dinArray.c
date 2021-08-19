#include <stdio.h>
#include <stdlib.h>

#define STANDARD_INIT_LENGTH 2

typedef struct {
	int length;
	int used;
	int *array;	
} darr;

darr createDArray(int l){
	darr array;
	array.length=l;
	array.used=0;
	array.array=(int*)(malloc(l*sizeof(int)));
	return array;
}


void addEl(darr* array, int el){
	if(array->length>array->used){
		array->array[array->used]=el;
		array->used=array->used+1;
	} else {
		int* narray=(int*)(malloc(sizeof(int)*array->length*2));
		for (int i=0; i<array->length; i++){
			narray[i]=array->array[i];
		}
		narray[array->length]=el;
		array->used=array->used+1;
		array->length=array->length*2;
		free(array->array);
		array->array=narray;
	}
}

void pprintDarray(darr array){
	printf("[");
	for (int i=0;i<array.used;i++) 
		if(i==array.used-1) printf("%d]\n",array.array[i]);
		else printf("%d,",array.array[i]);
}

void darrFree(darr* array){
	free(array->array);
}

int main (char**argv, int argc) {

	darr array=createDArray(STANDARD_INIT_LENGTH);
	addEl(&array,1);
	addEl(&array,2);
	addEl(&array,3);
	addEl(&array,4);
	addEl(&array,5);
	addEl(&array,6);
	addEl(&array,7);
	addEl(&array,123);
	addEl(&array,321);
	addEl(&array,100000);
	pprintDarray(array);

	darrFree(&array);
	return 0;
}
