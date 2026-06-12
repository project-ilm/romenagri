/* Malayalam (Malayalam) — HPS/ILM localized C
   എങ്കിൽ = if | വരെ = while | മടക്കുക = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define എങ്കിൽ if
#define വരെ while
#define മടക്കുക return
#define പൂർണ്ണസംഖ്യ int

int main(void) {
  int n = 0;
  വരെ (n < 5) {
    എങ്കിൽ (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  മടക്കുക 0;
}
