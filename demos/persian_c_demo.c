/* Persian (Perso-Arabic) — HPS/ILM localized C
   اگر = if | تازمانیکه = while | بازگرد = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define بازگرد return
#define صحیح int

int main(void) {
  int n = 0;
  تازمانیکه (n < 5) {
    اگر (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  بازگرد 0;
}
