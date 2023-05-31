#include <stdio.h>
#include <math.h>
int main(){
float a0=0;
int a1=0;
int n;
 printf("\n кількість елементів масиву n=");
 scanf("%d",&n);
 int a[n];
for(int i = 1; i <= n; i++){
 printf(" a[%d]=", i);
 scanf("%d", &a[i]);
  if (a[i] > 0 && a[i] % 2==0){
   a0 += a[i];
   a1++;
}}
if (a1 > 0) {
 a0 /=a1;
 printf(" середнє арифметичне значення парних елементів масиву = %.1f", a0);
}
else{
 printf(" в масиві немає парних елементів ");
}
return 0;
}