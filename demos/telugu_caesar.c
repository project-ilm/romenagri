/* Telugu (Telugu) — Caesar cipher (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ఒకవేళ if
#define వరకు while
#define కొరకు for
#define తిరిగి return
#define పూర్ణాంకం int
#define అక్షరం char
#define శూన్య void
int main(void) {
  char msg[]="hello"; int shift=3, i;
  printf("Telugu Caesar +3: ");
  for(i=0; msg[i]; i++) {
    if(msg[i]>='a' && msg[i]<='z')
      printf("%c", (msg[i]-'a'+shift)%26+'a');
    else printf("%c", msg[i]);
  }
  printf("\n"); return 0;
}
