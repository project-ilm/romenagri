/* Kannada (Kannada) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ಆದರೆ if
#define ತನಕ while
#define ಗಾಗಿ for
#define ಹಿಂತಿರುಗಿಸು return
#define ಪೂರ್ಣಾಂಕ int
#define ಅಕ್ಷರ char
#define ಶೂನ್ಯ void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Kannada Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
