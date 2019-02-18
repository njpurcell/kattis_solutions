#include <stdio.h>
#include <math.h>

int main()
{
	int n, w, h, matchlength;
	scanf("%d %d %d", &n, &w, &h);
	float hyp = sqrt(pow(w,2) + pow(h,2));

	for (int i = 0; i < n; i++){
		scanf("%d", &matchlength);
		if (matchlength <= hyp)
			printf("DA\n");
		else
			printf("NE\n");
	}
}
