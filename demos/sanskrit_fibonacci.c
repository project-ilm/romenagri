/* Sanskrit (Devanagari) — Fibonacci sequence (HPS/ILM)
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
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Sanskrit Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
