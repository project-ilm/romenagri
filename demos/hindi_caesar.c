/* Hindi (Devanagari) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबतक while
#define हेतु for
#define लौटाओ return
#define लिखो printf
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Hindi Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
