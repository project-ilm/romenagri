/* Marathi (Devanagari) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जर if
#define पर्यंत while
#define साठी for
#define परत return
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) जर(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Marathi primes to %d: ", n);
  for(i=2; i<=n; i++) जर(p[i]) printf("%d ", i);
  printf("\n"); परत 0;
}
