/* Arabic (Arabic) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define إذا if
#define طالما while
#define لكل for
#define أرجع return
#define اكتب printf
#define صحيح int
#define حرف char
#define فراغ void
صحيح main(void) {
  صحيح n=10, a=0, b=1, c, i;
  اكتب("Arabic Fibonacci: ");
  لكل(i=0; i<n; i++) {
    اكتب("%d ", a);
    c = a+b; a = b; b = c;
  }
  اكتب("\n");
  أرجع 0;
}
