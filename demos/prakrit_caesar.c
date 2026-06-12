/* Prakrit (Devanagari (historically Brahmi)) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जइ if
#define जाव while
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Prakrit Caesar +3: ");
  for(i=0; msg[i]; i++) {
    जइ(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
