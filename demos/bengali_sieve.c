/* Bengali (Bengali) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যতক্ষণ while
#define জন্য for
#define ফেরত return
#define পূর্ণসংখ্যা int
#define অক্ষর char
#define শূন্য void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Bengali primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
