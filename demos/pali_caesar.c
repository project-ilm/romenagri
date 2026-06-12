/* Pali (Devanagari (also Sinhala, Thai, Burmese, Khmer historically)) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define सचे if
#define याव while
#define अत्थाय for
#define पटिनिवत्त return
#define किच्च void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Pali Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
