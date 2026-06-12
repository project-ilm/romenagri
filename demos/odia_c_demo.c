/* Odia (Odia) — HPS/ILM localized C
   ଯଦି = if | ଯେପର୍ଯ୍ୟନ୍ତ = while | ଫେରାଅ = return | printf = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ଯଦି if
#define ଯେପର୍ଯ୍ୟନ୍ତ while
#define ଫେରାଅ return
#define ପୂର୍ଣ୍ଣସଂଖ୍ୟା int

int main(void) {
  int n = 0;
  ଯେପର୍ଯ୍ୟନ୍ତ (n < 5) {
    ଯଦି (n % 2 == 0)
      printf("%d\n", n);
    n++;
  }
  ଫେରାଅ 0;
}
