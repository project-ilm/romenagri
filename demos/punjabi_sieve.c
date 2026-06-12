/* Punjabi (Gurmukhi) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਲਈ for
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int
#define ਅੱਖਰ char
#define ਖਾਲੀ void
int main(void) {
  int n=50, i, j, p[51];
  ਲਈ(i=2; i<=n; i++) p[i]=1;
  ਲਈ(i=2; i*i<=n; i++) if(p[i]) ਲਈ(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Punjabi primes to %d: ", n);
  ਲਈ(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
