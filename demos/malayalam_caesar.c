/* Malayalam (Malayalam) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define എങ്കിൽ if
#define വരെ while
#define വേണ്ടി for
#define മടക്കുക return
#define പൂർണ്ണസംഖ്യ int
#define അക്ഷരം char
#define ശൂന്യം void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Malayalam Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
