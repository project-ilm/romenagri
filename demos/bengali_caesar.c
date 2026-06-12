/* Bengali (Bengali) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যতক্ষণ while
#define জন্য for
#define ফেরত return
#define পূর্ণসংখ্যা int
#define অক্ষর char
#define শূন্য void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Bengali Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
