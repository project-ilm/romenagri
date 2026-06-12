/* Odia (Odia) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ଯଦି if
#define ଯେପର୍ଯ୍ୟନ୍ତ while
#define ପାଇଁ for
#define ଫେରାଅ return
#define ପୂର୍ଣ୍ଣସଂଖ୍ୟା int
#define ଅକ୍ଷର char
#define ଶୂନ୍ୟ void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Odia %d! = %d\n", i, fact(i));
  return 0;
}
