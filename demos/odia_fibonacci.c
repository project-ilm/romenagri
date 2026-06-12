/* Odia (Odia) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ଯଦି if
#define ଯେପର୍ଯ୍ୟନ୍ତ while
#define ପାଇଁ for
#define ଫେରାଅ return
#define ପୂର୍ଣ୍ଣସଂଖ୍ୟା int
#define ଅକ୍ଷର char
#define ଶୂନ୍ୟ void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Odia Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
