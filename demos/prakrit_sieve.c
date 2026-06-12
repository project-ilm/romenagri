/* Prakrit (Devanagari (historically Brahmi)) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जइ if
#define जाव while
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) जइ(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Prakrit primes to %d: ", n);
  for(i=2; i<=n; i++) जइ(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
