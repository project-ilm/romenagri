/* Kannada (Kannada) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ಆದರೆ if
#define ತನಕ while
#define ಗಾಗಿ for
#define ಹಿಂತಿರುಗಿಸು return
#define ಪೂರ್ಣಾಂಕ int
#define ಅಕ್ಷರ char
#define ಶೂನ್ಯ void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Kannada Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
