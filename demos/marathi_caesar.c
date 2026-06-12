/* Marathi (Devanagari) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define जर if
#define पर्यंत while
#define साठी for
#define परत return
#define पूर्णांक int
#define अक्षर char
#define शून्य void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Marathi Caesar +3: ");
  for(i=0; msg[i]; i++) {
    जर(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); परत 0;
}
