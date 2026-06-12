/* Kannada (Kannada) — HPS/ILM localized C
   ಆದರೆ = if | ತನಕ = while | ಹಿಂತಿರುಗಿಸು = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ಆದರೆ if
#define ತನಕ while
#define ಹಿಂತಿರುಗಿಸು return
#define ಪೂರ್ಣಾಂಕ int

int main(void) {
  int n = 0;
  ತನಕ (n < 5) {
    ಆದರೆ (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  ಹಿಂತಿರುಗಿಸು 0;
}
