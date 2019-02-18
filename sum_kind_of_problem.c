#include <stdio.h>

int main(){
  int p, k, n, s1, s2, s3;
  scanf("%d", &p);

  for (int i = 0; i < p; i++){
    scanf("%d %d", &k, &n);
    s1 = s2 = s3 = 0;
    for (int j = 1; j <= (2*n); j++){
      if (j <= n)
        s1 += j;
      if (j % 2 == 1)
        s2 += j;
      if (j % 2 == 0)
        s3 += j;
    }
    printf("%d %d %d %d\n", k, s1, s2, s3);
  }
}
