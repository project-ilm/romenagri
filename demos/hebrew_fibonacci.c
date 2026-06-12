/* Hebrew (Hebrew) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define אם if
#define כלעוד while
#define עבור for
#define החזר return
#define פונקציה void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Hebrew Fibonacci: ");
  עבור(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  החזר 0;
}
