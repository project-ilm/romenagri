/* Bengali (Bengali) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যতক্ষণ while
#define জন্য for
#define ফেরত return
#define পূর্ণসংখ্যা int
#define অক্ষর char
#define শূন্য void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Bengali %d! = %d\n", i, fact(i));
  return 0;
}
