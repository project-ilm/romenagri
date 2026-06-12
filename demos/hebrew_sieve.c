/* Hebrew (Hebrew) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define אם if
#define כלעוד while
#define עבור for
#define החזר return
#define פונקציה void
int main(void) {
  int n=50, i, j, p[51];
  עבור(i=2; i<=n; i++) p[i]=1;
  עבור(i=2; i*i<=n; i++) אם(p[i]) עבור(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Hebrew primes to %d: ", n);
  עבור(i=2; i<=n; i++) אם(p[i]) printf("%d ", i);
  printf("\n"); החזר 0;
}
