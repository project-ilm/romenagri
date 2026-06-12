/* Nepali (Devanagari) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबसम्म while
#define लागि for
#define फर्काऊ return
#define कार्य void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Nepali Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
