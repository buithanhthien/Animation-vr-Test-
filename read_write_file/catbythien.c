#include<stdio.h>

int main(){
	FILE *fp;
	char cat[1000];
	char file_name[100];
	printf("Nhap file muon doc: ");
	gets(file_name);

	fp = fopen(file_name,"r");
	while(fgets(cat, 1000, fp))
		printf("%s",cat);
	fclose(fp);
	return 0;
}
