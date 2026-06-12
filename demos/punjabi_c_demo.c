/* Punjabi (Gurmukhi) — HPS/ILM localized C
   ਜੇ = if | ਜਦਤੱਕ = while | ਵਾਪਸ = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int

int main(void) {
  int n = 0;
  ਜਦਤੱਕ (n < 5) {
    ਜੇ (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  ਵਾਪਸ 0;
}
