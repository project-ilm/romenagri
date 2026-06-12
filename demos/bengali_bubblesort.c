/* Bengali (Bengali) — Bubble sort (HPS/ILM)
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
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  for(i=0; i<n-1; i++)
    for(j=0; j<n-i-1; j++)
      if(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Bengali sorted: ");
  for(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  return 0;
}
