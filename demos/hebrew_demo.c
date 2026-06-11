/* Hebrew systems-programming demo — Hindawi/ILM localized C
   native: אם / כאשר / הדפס
   Keyword localization per ILM langspec registry; identifiers are
   Romenagri (trigraph _-forms), fully C-identifier-legal.
   Copyright (C) 1993-2026 Abhishek Choudhary. GPL. */
#include <stdio.h>
#define ima if
#define kaasher while
#define hadpes printf
int main(void){
  int gi_n_tee = 0;                 /* counter */
  kaasher (gi_n_tee < 5) {
    ima (gi_n_tee % 2 == 0) hadpes("%d sam\n", gi_n_tee);
    gi_n_tee++;
  }
  return 0;
}
