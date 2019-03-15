#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<unistd.h>

void print_out(char *str, FILE *find){	
	
    while(fgets(find, 20, str))
	printf("%s", str);
}

int main(void){
	FILE *find;
	char Name[12];
	char str[];

	find = fopen("Contact.txt","a+");	

	print_out(str, find);	

	fclose(find);
}

