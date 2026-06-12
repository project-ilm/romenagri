/* Arabic (Arabic) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define إذا if
#define طالما while
#define لكل for
#define أرجع return
#define اكتب printf
#define صحيح int
#define حرف char
#define فراغ void
صحيح main(void) {
  صحيح n=50, i, j, p[51];
  لكل(i=2; i<=n; i++) p[i]=1;
  لكل(i=2; i*i<=n; i++) إذا(p[i]) لكل(j=i*i;j<=n;j+=i) p[j]=0;
  اكتب("Arabic primes to %d: ", n);
  لكل(i=2; i<=n; i++) إذا(p[i]) اكتب("%d ", i);
  اكتب("\n"); أرجع 0;
}
