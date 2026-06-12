/* Syriac (Syriac (Estrangela)) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ܐܢ if
#define ܟܡܐ while
#define ܦܢܐ return
int fact(int n) { ܐܢ(n<=1) ܦܢܐ 1; ܦܢܐ n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Syriac %d! = %d\n", i, fact(i));
  ܦܢܐ 0;
}
