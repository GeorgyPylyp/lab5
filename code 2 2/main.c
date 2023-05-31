#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
const int n, Low=-100, High=100;
printf("Введіть розмір масиву = ");
scanf("%d", &n);
srand(time(0));
int a[n];
for (int i=0; i<n; i++)
a[i]=Low+rand()%High;
for (int i=0; i<n; i++)
printf("\n a[%d]=%d\t", i, a[i]);
int min = 0;
int min2 = 0;
int a1 =1;
int i=0;
for(int i = 0; i < n; i++){
if(a[i] < min){
min = a[i];
min2 =i;}
if (a==0)
  break;
if( a[i]>0)
 a1*=a[i];
}
printf("\n номер мінімального елемента масиву= %d\t", min2);
printf("\n Добуток елементів масиву до першого нульового елемента= %d\n", a1);
return 0;
}