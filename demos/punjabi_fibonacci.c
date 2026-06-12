/* Punjabi (Gurmukhi) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਲਈ for
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int
#define ਅੱਖਰ char
#define ਖਾਲੀ void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Punjabi Fibonacci: ");
  ਲਈ(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
