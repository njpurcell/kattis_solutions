#include <stdio.h>

int main(){
  char jon_ahh[1000];
  char doc_ahh[1000];

  scanf("%s", jon_ahh);
  scanf("%s", doc_ahh);

  int i = 0;
  int j = 0;
  while (jon_ahh[i] != '\0'){
    i += 1;
  }
  while (doc_ahh[j] != '\0'){
    j += 1;
  }

  if (i < j)
    printf("no\n");
  else
    printf("go\n");

}
