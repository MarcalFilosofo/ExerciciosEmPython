#include <stdio.h>
#include <string.h>
#include <ctype.h>

char isVogal(char letra){
	letra = tolower(letra);
	if((letra=='a')||(letra=='i')||(letra=='e')||(letra=='o')||(letra=='u')){
		return 1;
	}else{
		return 0;
	}
}
int main(int argc, char** argv){
	char nome[300];
	char nomeAlterado[300];
	int i;
	int vogais = 0;
	printf("Digite um nome: ");
	fgets(nome,300, stdin);
	for(i = 0; i < strlen(nome); i++){
		if(isVogal(nome[i]) == 1){
			vogais++;
		}
	}
	printf("Existem %i no seu nome", vogais);
	
	
	for(i = 0; i < strlen(nome); i++){
		if(isVogal(nome[i]) == 1){
			printf("Altere o caracter %s: ", nome[i]);
			scanf("%s", &nomeAlterado[i]);
		}else{
			nomeAlterado[i] = nome[i];
			
		}
	}
	printf("%s", nomeAlterado);
}