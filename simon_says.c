#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int n = 0;
  int j;
  scanf("%d\n", &n);
  char *simoninput = NULL;
  size_t maxsize = 101;
  char simonsays[11] = "Simon says ";

  for (int i = 0; i < n; i++){
    getline(&simoninput, &maxsize, stdin);
    //printf("%s\n", simoninput);
    if (strncmp(simoninput, simonsays, 11) == 0){
      j = 11;
      while (simoninput[j] != '\n'){
        printf("%c", simoninput[j]);
        j += 1;
      }
      printf("\n");
    }
  }

  return 0;
}
