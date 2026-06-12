/* Urdu (Perso-Arabic (Nastaliq)) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define برائے for
#define واپس return
#define صحیح int
#define حرف char
#define خالی void
صحیح main(void) {
  char msg[]="hello"; صحیح shift=3, i;
  printf("Urdu Caesar +3: ");
  برائے(i=0; msg[i]; i++) {
    اگر(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); واپس 0;
}
