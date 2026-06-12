/* Pali (Devanagari (also Sinhala, Thai, Burmese, Khmer historically)) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define सचे if
#define याव while
#define अत्थाय for
#define पटिनिवत्त return
#define किच्च void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Pali Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
