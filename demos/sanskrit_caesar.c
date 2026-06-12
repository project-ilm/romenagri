/* Sanskrit (Devanagari) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define यावत् while
#define प्रति for
#define प्रत्यागम return
#define लिख printf
#define पूर्णाङ्क int
#define वर्ण char
#define शून्य void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Sanskrit Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
