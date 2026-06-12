/* Assamese (Assamese (Bengali-Assamese)) — Fibonacci sequence (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define যদি if
#define যেতিয়ালৈ while
#define বাবে for
#define ঘূৰাই return
#define কাৰ্য void
int main(void) {
  int n=10, a=0, b=1, c, i;
  printf("Assamese Fibonacci: ");
  for(i=0; i<n; i++) {
    printf("%d ", a);
    c = a+b; a = b; b = c;
  }
  printf("\n");
  return 0;
}
