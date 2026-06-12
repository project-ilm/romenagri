/* Telugu (Telugu) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ఒకవేళ if
#define వరకు while
#define కొరకు for
#define తిరిగి return
#define పూర్ణాంకం int
#define అక్షరం char
#define శూన్య void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Telugu Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
