/* Persian (Perso-Arabic) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define اگر if
#define تازمانیکه while
#define برای for
#define بازگرد return
#define صحیح int
#define نویسه char
#define تهی void
صحیح main(void) {
  صحیح arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  برای(i=0; i<n-1; i++)
    برای(j=0; j<n-i-1; j++)
      اگر(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Persian sorted: ");
  برای(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  بازگرد 0;
}
