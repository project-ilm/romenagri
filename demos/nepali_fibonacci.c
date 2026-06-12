/* Nepali (Devanagari) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबसम्म while
#define लागि for
#define फर्काऊ return
#define कार्य void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Nepali Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
