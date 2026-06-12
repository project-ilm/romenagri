/* Hebrew (Hebrew) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define אם if
#define כלעוד while
#define עבור for
#define החזר return
#define פונקציה void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Hebrew Caesar +3: ");
  עבור(i=0; msg[i]; i++) {
    אם(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); החזר 0;
}
