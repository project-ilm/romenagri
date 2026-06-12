/* Assamese (Assamese (Bengali-Assamese)) — Recursive factorial (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যেতিয়ালৈ while
#define বাবে for
#define ঘূৰাই return
#define কাৰ্য void
int fact(int n) { if(n<=1) return 1; return n*fact(n-1); }
int main(void) {
  int i;
  for(i=1; i<=10; i++) printf("Assamese %d! = %d\n", i, fact(i));
  return 0;
}
