/* Persian (Perso-Arabic) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define برای for
#define بازگرد return
#define صحیح int
#define نویسه char
#define تهی void
صحیح main(void) {
  صحیح n=50, i, j, p[51];
  برای(i=2; i<=n; i++) p[i]=1;
  برای(i=2; i*i<=n; i++) اگر(p[i]) برای(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Persian primes to %d: ", n);
  برای(i=2; i<=n; i++) اگر(p[i]) printf("%d ", i);
  printf("\n"); بازگرد 0;
}
