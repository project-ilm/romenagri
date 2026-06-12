/* Prakrit (Devanagari (historically Brahmi)) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जइ if
#define जाव while
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Prakrit Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
