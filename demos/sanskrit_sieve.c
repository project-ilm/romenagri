/* Sanskrit (Devanagari) — Sieve of Eratosthenes (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define यावत् while
#define प्रति for
#define प्रत्यागम return
#define लिख printf
#define पूर्णाङ्क int
#define वर्ण char
#define शून्य void
int main(void) {
  int n=50, i, j, p[51];
  for(i=2; i<=n; i++) p[i]=1;
  for(i=2; i*i<=n; i++) if(p[i]) for(j=i*i;j<=n;j+=i) p[j]=0;
  printf("Sanskrit primes to %d: ", n);
  for(i=2; i<=n; i++) if(p[i]) printf("%d ", i);
  printf("\n"); return 0;
}
