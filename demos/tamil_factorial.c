/* Tamil (Tamil) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define எனில் if
#define வரை while
#define க்கு for
#define திரும்பு return
#define முழு int
#define எழுத்து char
#define வெறுமை void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Tamil %d! = %d\n", i, fact(i));
  return 0;
}
