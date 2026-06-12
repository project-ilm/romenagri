/* Pali (Devanagari (also Sinhala, Thai, Burmese, Khmer historically)) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define सचे if
#define याव while
#define अत्थाय for
#define पटिनिवत्त return
#define किच्च void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Pali %d! = %d\n", i, fact(i));
  return 0;
}
