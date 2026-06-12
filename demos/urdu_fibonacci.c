/* Urdu (Perso-Arabic (Nastaliq)) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define برائے for
#define واپس return
#define صحیح int
#define حرف char
#define خالی void
صحیح main(void) {
  صحیح n=10, a=0, b=1, c, i;
  printf("Urdu Fibonacci: ");
  برائے(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  واپس 0;
}
