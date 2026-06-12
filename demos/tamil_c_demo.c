/* Tamil (Tamil) — HPS/ILM localized C
   எனில் = if | வரை = while | திரும்பு = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define எனில் if
#define வரை while
#define திரும்பு return
#define முழு int

int main(void) {
  int n = 0;
  வரை (n < 5) {
    எனில் (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  திரும்பு 0;
}
