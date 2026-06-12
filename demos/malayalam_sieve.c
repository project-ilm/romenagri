/* Malayalam (Malayalam) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define എങ്കിൽ if
#define വരെ while
#define വേണ്ടി for
#define മടക്കുക return
#define പൂർണ്ണസംഖ്യ int
#define അക്ഷരം char
#define ശൂന്യം void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Malayalam primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
