/* Marathi (Devanagari) — Bubble sort (HPS/ILM)
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
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  for(i=0; i<n-1; i++)
    for(j=0; j<n-i-1; j++)
      जर(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Marathi sorted: ");
  for(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  परत 0;
}
