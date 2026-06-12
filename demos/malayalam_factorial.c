/* Malayalam (Malayalam) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define എങ്കിൽ if
#define വരെ while
#define വേണ്ടി for
#define മടക്കുക return
#define പൂർണ്ണസംഖ്യ int
#define അക്ഷരം char
#define ശൂന്യം void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Malayalam %d! = %d\n", i, fact(i));
  return 0;
}
