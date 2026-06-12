/* Urdu (Perso-Arabic (Nastaliq)) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define جبتک while
#define برائے for
#define واپس return
#define صحیح int
#define حرف char
#define خالی void
صحیح main(void) {
  صحیح arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  برائے(i=0; i<n-1; i++)
    برائے(j=0; j<n-i-1; j++)
      اگر(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Urdu sorted: ");
  برائے(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  واپس 0;
}
