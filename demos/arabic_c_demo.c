/* Arabic (Arabic) — HPS/ILM localized C
   إذا = if | طالما = while | أرجع = return | اكتب = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define إذا if
#define طالما while
#define أرجع return
#define اكتب printf
#define صحيح int

int main(void) {
  int n = 0;
  طالما (n < 5) {
    إذا (n % 2 == 0)
      اكتب("%d\n", n);
    n++;
  }
  أرجع 0;
}
