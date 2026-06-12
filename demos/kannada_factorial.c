/* Kannada (Kannada) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ಆದರೆ if
#define ತನಕ while
#define ಗಾಗಿ for
#define ಹಿಂತಿರುಗಿಸು return
#define ಪೂರ್ಣಾಂಕ int
#define ಅಕ್ಷರ char
#define ಶೂನ್ಯ void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Kannada %d! = %d\n", i, fact(i));
  return 0;
}
