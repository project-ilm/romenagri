/* Arabic (Arabic) — Bubble sort (HPS/ILM)
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define إذا if
#define طالما while
#define لكل for
#define أرجع return
#define اكتب printf
#define صحيح int
#define حرف char
#define فراغ void
صحيح main(void) {
  صحيح arr[]={64,34,25,12,22,11,90}, n=7, i, j, tmp;
  لكل(i=0; i<n-1; i++)
    لكل(j=0; j<n-i-1; j++)
      إذا(arr[j]>arr[j+1]){tmp=arr[j];arr[j]=arr[j+1];arr[j+1]=tmp;}
  اكتب("Arabic sorted: ");
  لكل(i=0; i<n; i++) اكتب("%d ",arr[i]);
  اكتب("\n");
  أرجع 0;
}
