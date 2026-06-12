/* Marathi (Devanagari) — HPS/ILM localized C
   जर = if | पर्यंत = while | परत = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जर if
#define पर्यंत while
#define परत return
#define पूर्णांक int

int main(void) {
  int n = 0;
  पर्यंत (n < 5) {
    जर (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  परत 0;
}
