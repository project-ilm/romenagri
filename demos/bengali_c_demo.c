/* Bengali (Bengali) — HPS/ILM localized C
   যদি = if | যতক্ষণ = while | ফেরত = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যতক্ষণ while
#define ফেরত return
#define পূর্ণসংখ্যা int

int main(void) {
  int n = 0;
  যতক্ষণ (n < 5) {
    যদি (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  ফেরত 0;
}
