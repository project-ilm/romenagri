/* Bengali (Bengali) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যতক্ষণ while
#define জন্য for
#define ফেরত return
#define পূর্ণসংখ্যা int
#define অক্ষর char
#define শূন্য void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Bengali Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
