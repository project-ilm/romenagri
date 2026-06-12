/* Kannada (Kannada) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ಆದರೆ if
#define ತನಕ while
#define ಗಾಗಿ for
#define ಹಿಂತಿರುಗಿಸು return
#define ಪೂರ್ಣಾಂಕ int
#define ಅಕ್ಷರ char
#define ಶೂನ್ಯ void
int main(void) {
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  for(i=0; i<n-1; i++)
    for(j=0; j<n-i-1; j++)
      if(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Kannada sorted: ");
  for(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  return 0;
}
