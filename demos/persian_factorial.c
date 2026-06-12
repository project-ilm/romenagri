/* Persian (Perso-Arabic) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define برای for
#define بازگرد return
#define صحیح int
#define نویسه char
#define تهی void
صحیح fact(صحیح n) { اگر(n<=1) بازگرد 1; بازگرد n*fact(n-1); }
صحیح main(void) {
  صحیح i;
  برای(i=1; i<=10; i++) printf("Persian %d! = %d\n", i, fact(i));
  بازگرد 0;
}
