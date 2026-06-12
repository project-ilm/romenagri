/* Arabic (Arabic) — Recursive factorial (HPS/ILM)
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
صحيح fact(صحيح n) { إذا(n<=1) أرجع 1; أرجع n*fact(n-1); }
صحيح main(void) {
  صحيح i;
  لكل(i=1; i<=10; i++) اكتب("Arabic %d! = %d\n", i, fact(i));
  أرجع 0;
}
