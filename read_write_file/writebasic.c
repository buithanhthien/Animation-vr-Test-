#include<stdio.h>

int main(){
	FILE *fp;

	fp = fopen("file1.txt","w");
	fprintf(fp,"This is write test in file\n");
	fclose(fp);

	return 0;
}
