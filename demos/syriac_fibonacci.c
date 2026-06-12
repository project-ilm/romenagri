/* Syriac (Syriac (Estrangela)) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ܐܢ if
#define ܟܡܐ while
#define ܦܢܐ return
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Syriac Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  ܦܢܐ 0;
}
