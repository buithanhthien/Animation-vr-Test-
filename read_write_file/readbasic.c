#include<stdio.h>

int main(){
	FILE *fp;
	char str[100];
	fp = fopen("write_file.txt","r");
	
    while(fgets(str, 100, fp))
		printf("%s",str);

	fclose(fp);
	return 0;
}
