/* Urdu systems-programming demo — Hindawi/ILM localized C
   native: اگر / جب تک / لکھو
   Keyword localization per ILM langspec registry; identifiers are
   Romenagri (trigraph _-forms), fully C-identifier-legal.
   Copyright (C) 1993-2026 Abhishek Choudhary. GPL. */
#include <stdio.h>
#define agar if
#define jab_taka while
#define likho printf
int main(void){
  int gi_n_tee = 0;                 /* counter */
  jab_taka (gi_n_tee < 5) {
    agar (gi_n_tee % 2 == 0) likho("%d sam\n", gi_n_tee);
    gi_n_tee++;
  }
  return 0;
}
