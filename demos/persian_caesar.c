/* Persian (Perso-Arabic) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define برای for
#define بازگرد return
#define صحیح int
#define نویسه char
#define تهی void
صحیح main(void) {
  char msg[]="hello"; صحیح shift=3, i;
  printf("Persian Caesar +3: ");
  برای(i=0; msg[i]; i++) {
    اگر(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); بازگرد 0;
}
