/* Assamese (Assamese (Bengali-Assamese)) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যেতিয়ালৈ while
#define বাবে for
#define ঘূৰাই return
#define কাৰ্য void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Assamese Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
