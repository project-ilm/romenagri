/* Arabic (Arabic) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define إذا if
#define طالما while
#define لكل for
#define أرجع return
#define اكتب printf
#define صحيح int
#define حرف char
#define فراغ void
صحيح main(void) {
  char msg[]="hello"; صحيح shift=3, i;
  اكتب("Arabic Caesar +3: ");
  لكل(i=0; msg[i]; i++) {
    إذا(msg[i]>='a' && msg[i]<='z')
      اكتب("%c", (msg[i]-'a'+shift)%26+'a');
    else اكتب("%c", msg[i]);
  }
  اكتب("\n"); أرجع 0;
}
