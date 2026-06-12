/* Marathi (Devanagari) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जर if
#define पर्यंत while
#define साठी for
#define परत return
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Marathi Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  परत 0;
}
