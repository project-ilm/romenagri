/* Gujarati (Gujarati) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define જો if
#define જ્યાંસુધી while
#define માટે for
#define પાછા return
#define પૂર્ણાંક int
#define અક્ષર char
#define શૂન્ય void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Gujarati Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
