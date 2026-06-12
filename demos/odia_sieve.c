/* Odia (Odia) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ଯଦି if
#define ଯେପର୍ଯ୍ୟନ୍ତ while
#define ପାଇଁ for
#define ଫେରାଅ return
#define ପୂର୍ଣ୍ଣସଂଖ୍ୟା int
#define ଅକ୍ଷର char
#define ଶୂନ୍ୟ void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Odia primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
