/* Sanskrit (Devanagari) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define यावत् while
#define प्रति for
#define प्रत्यागम return
#define लिख printf
#define पूर्णाङ्क int
#define वर्ण char
#define शून्य void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Sanskrit %d! = %d\n", i, fact(i));
  return 0;
}
