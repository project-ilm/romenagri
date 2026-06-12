/* Tamil (Tamil) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define எனில் if
#define வரை while
#define க்கு for
#define திரும்பு return
#define முழு int
#define எழுத்து char
#define வெறுமை void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Tamil Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
