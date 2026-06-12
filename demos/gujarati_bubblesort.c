/* Gujarati (Gujarati) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define જો if
#define જ્યાંસુધી while
#define માટે for
#define પાછા return
#define પૂર્ણાંક int
#define અક્ષર char
#define શૂન્ય void
int main(void) {
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  for(i=0; i<n-1; i++)
    for(j=0; j<n-i-1; j++)
      if(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Gujarati sorted: ");
  for(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  return 0;
}
