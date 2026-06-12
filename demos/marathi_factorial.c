/* Marathi (Devanagari) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जर if
#define पर्यंत while
#define साठी for
#define परत return
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int fact(int n) { जर(n<=1) परत 1; परत n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Marathi %d! = %d\n", i, fact(i));
  परत 0;
}
