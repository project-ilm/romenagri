/* Punjabi (Gurmukhi) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਲਈ for
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int
#define ਅੱਖਰ char
#define ਖਾਲੀ void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Punjabi Caesar +3: ");
  ਲਈ(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
