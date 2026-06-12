/* Hebrew (Hebrew) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define אם if
#define כלעוד while
#define עבור for
#define החזר return
#define פונקציה void
int main(void) {
  int arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  עבור(i=0; i<n-1; i++)
    עבור(j=0; j<n-i-1; j++)
      אם(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  printf("Hebrew sorted: ");
  עבור(i=0; i<n; i++) printf("%d ",arr[i]);
  printf("\n");
  החזר 0;
}
