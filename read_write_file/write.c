#include<stdio.h>

int main(){
	FILE *fp;
	char str[100];
	fp = fopen("write_file.txt","w+");
	printf("Nhap cai gi di: ");
	gets(str);
	fprintf(fp,"%s",str);
	fclose(fp);

	return 0;
}
