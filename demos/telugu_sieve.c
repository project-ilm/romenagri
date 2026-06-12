/* Telugu (Telugu) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ఒకవేళ if
#define వరకు while
#define కొరకు for
#define తిరిగి return
#define పూర్ణాంకం int
#define అక్షరం char
#define శూన్య void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Telugu primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
