/* Urdu (Perso-Arabic (Nastaliq)) — HPS/ILM localized C
   اگر = if | جبتک = while | واپس = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define واپس return
#define صحیح int

int main(void) {
  int n = 0;
  جبتک (n < 5) {
    اگر (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  واپس 0;
}
