/* Urdu (Perso-Arabic (Nastaliq)) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define برائے for
#define واپس return
#define صحیح int
#define حرف char
#define خالی void
صحیح main(void) {
  صحیح n=50, i, j, p[51];
  برائے(i=2; i<=n; i++) p[i]=1;
  برائے(i=2; i*i<=n; i++) اگر(p[i]) برائے(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Urdu primes to %d: ", n);
  برائے(i=2; i<=n; i++) اگر(p[i]) printf("%d ", i);
  printf("\n"); واپس 0;
}
