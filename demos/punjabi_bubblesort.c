/* Punjabi (Gurmukhi) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define ਜੇ if
#define ਜਦਤੱਕ while
#define ਲਈ for
#define ਵਾਪਸ return
#define ਪੂਰਨਅੰਕ int
#define ਅੱਖਰ char
#define ਖਾਲੀ void
int main(void) {
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  ਲਈ(i=0; i<n-1; i++)
    ਲਈ(j=0; j<n-i-1; j++)
      if(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Punjabi sorted: ");
  ਲਈ(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  return 0;
}
