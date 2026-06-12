/* Telugu (Telugu) — HPS/ILM localized C
   ఒకవేళ = if | వరకు = while | తిరిగి = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ఒకవేళ if
#define వరకు while
#define తిరిగి return
#define పూర్ణాంకం int

int main(void) {
  int n = 0;
  వరకు (n < 5) {
    ఒకవేళ (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  తిరిగి 0;
}
