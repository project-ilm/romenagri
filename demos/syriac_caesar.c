/* Syriac (Syriac (Estrangela)) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ܐܢ if
#define ܟܡܐ while
#define ܦܢܐ return
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Syriac Caesar +3: ");
  for(i=0; msg[i]; i++) {
    ܐܢ(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); ܦܢܐ 0;
}
