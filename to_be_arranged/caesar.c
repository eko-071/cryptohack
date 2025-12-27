#include <stdio.h>
#include <ctype.h>

int main(){
    char string[1000];
    fgets(string, 1000, stdin);
    
    for(int i=0; i<26; i++){
        for(int j=0; string[j] != '\0'; j++){
	    if(string[j] == '\n') continue;
            if(string[j] != ' '){
                int cipher = ((toupper(string[j]) - 'A') + i) % 26;
                printf("%c", cipher + 'A');
            }
            else printf(" ");
        }
        printf("\n");
    }
}
