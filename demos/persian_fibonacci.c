/* Persian (Perso-Arabic) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define برای for
#define بازگرد return
#define صحیح int
#define نویسه char
#define تهی void
صحیح main(void) {
  صحیح n=10, a=0, b=1, c, i;
  printf("Persian Fibonacci: ");
  برای(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  بازگرد 0;
}
