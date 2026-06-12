/* Telugu (Telugu) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ఒకవేళ if
#define వరకు while
#define కొరకు for
#define తిరిగి return
#define పూర్ణాంకం int
#define అక్షరం char
#define శూన్య void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Telugu %d! = %d\n", i, fact(i));
  return 0;
}
