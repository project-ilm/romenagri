/* Malayalam (Malayalam) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define എങ്കിൽ if
#define വരെ while
#define വേണ്ടി for
#define മടക്കുക return
#define പൂർണ്ണസംഖ്യ int
#define അക്ഷരം char
#define ശൂന്യം void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Malayalam Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
