/* Gujarati (Gujarati) — HPS/ILM localized C
   જો = if | જ્યાંસુધી = while | પાછા = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define જો if
#define જ્યાંસુધી while
#define પાછા return
#define પૂર્ણાંક int

int main(void) {
  int n = 0;
  જ્યાંસુધી (n < 5) {
    જો (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  પાછા 0;
}
