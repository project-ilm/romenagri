/* Tamil (Tamil) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define எனில் if
#define வரை while
#define க்கு for
#define திரும்பு return
#define முழு int
#define எழுத்து char
#define வெறுமை void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Tamil primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
