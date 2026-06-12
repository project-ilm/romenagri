/* Prakrit (Devanagari (historically Brahmi)) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जइ if
#define जाव while
int fact(int n) { जइ(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Prakrit %d! = %d\n", i, fact(i));
  return 0;
}
