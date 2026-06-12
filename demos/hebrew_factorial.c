/* Hebrew (Hebrew) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define אם if
#define כלעוד while
#define עבור for
#define החזר return
#define פונקציה void
int fact(int n) { אם(n<=1) החזר 1; החזר n*fact(n-1); }
int main(void) {
  int i;
  עבור(i=1; i<=10; i++) printf("Hebrew %d! = %d\n", i, fact(i));
  החזר 0;
}
