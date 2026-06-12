/* Punjabi (Gurmukhi) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਲਈ for
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int
#define ਅੱਖਰ char
#define ਖਾਲੀ void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  ਲਈ(i=1; i<=10; i++) printf("Punjabi %d! = %d\n", i, fact(i));
  return 0;
}
