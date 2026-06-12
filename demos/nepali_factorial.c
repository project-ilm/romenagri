/* Nepali (Devanagari) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबसम्म while
#define लागि for
#define फर्काऊ return
#define कार्य void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Nepali %d! = %d\n", i, fact(i));
  return 0;
}
