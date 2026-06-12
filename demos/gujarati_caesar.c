/* Gujarati (Gujarati) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define જો if
#define જ્યાંસુધી while
#define માટે for
#define પાછા return
#define પૂર્ણાંક int
#define અક્ષર char
#define શૂન્ય void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Gujarati Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
