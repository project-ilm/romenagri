/* Tamil (Tamil) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define எனில் if
#define வரை while
#define க்கு for
#define திரும்பு return
#define முழு int
#define எழுத்து char
#define வெறுமை void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Tamil Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
