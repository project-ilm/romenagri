/* Urdu (Perso-Arabic (Nastaliq)) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define برائے for
#define واپس return
#define صحیح int
#define حرف char
#define خالی void
صحیح fact(صحیح n) { اگر(n<=1) واپس 1; واپس n*fact(n-1); }
صحیح main(void) {
  صحیح i;
  برائے(i=1; i<=10; i++) printf("Urdu %d! = %d\n", i, fact(i));
  واپس 0;
}
