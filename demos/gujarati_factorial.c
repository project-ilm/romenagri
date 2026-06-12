/* Gujarati (Gujarati) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define જો if
#define જ્યાંસુધી while
#define માટે for
#define પાછા return
#define પૂર્ણાંક int
#define અક્ષર char
#define શૂન્ય void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Gujarati %d! = %d\n", i, fact(i));
  return 0;
}
