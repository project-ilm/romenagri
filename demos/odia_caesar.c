/* Odia (Odia) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ଯଦି if
#define ଯେପର୍ଯ୍ୟନ୍ତ while
#define ପାଇଁ for
#define ଫେରାଅ return
#define ପୂର୍ଣ୍ଣସଂଖ୍ୟା int
#define ଅକ୍ଷର char
#define ଶୂନ୍ୟ void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Odia Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
