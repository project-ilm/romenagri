/* Farsi systems-programming demo — Hindawi/ILM localized C
   native: اگر / تا زمانی / بنویس
   Keyword localization per ILM langspec registry; identifiers are
   Romenagri (trigraph _-forms), fully C-identifier-legal.
   Copyright (C) 1993-2026 Abhishek Choudhary. GPL. */
#include <stdio.h>
#define agar_f if
#define ta_zamani while
#define benevis printf
int main(void){
  int gi_n_tee = 0;                 /* counter */
  ta_zamani (gi_n_tee < 5) {
    agar_f (gi_n_tee % 2 == 0) benevis("%d sam\n", gi_n_tee);
    gi_n_tee++;
  }
  return 0;
}
