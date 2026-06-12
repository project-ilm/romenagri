/* Hindi (Devanagari) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबतक while
#define हेतु for
#define लौटाओ return
#define लिखो printf
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Hindi %d! = %d\n", i, fact(i));
  return 0;
}
