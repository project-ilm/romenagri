/* Sanskrit (Devanagari) — HPS/ILM localized C
   यदि = if | यावत् = while | प्रत्यागम = return | लिख = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define यावत् while
#define प्रत्यागम return
#define लिख printf
#define पूर्णाङ्क int

int main(void) {
  int n = 0;
  यावत् (n < 5) {
    यदि (n % 2 == 0)
      लिख("%d\n", n);
    n++;
  }
  प्रत्यागम 0;
}
