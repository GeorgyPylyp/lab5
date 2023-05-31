#include <stdio.h>
int main() {
int n;
printf("Введіть розмір масиву = ");
scanf("%d", &n);
int a[n];
printf("Введіть елементи масиву\n");
 for (int i = 0; i < n; i++) {
 printf("a[%d] = ", i);
 scanf("%d", &a[i]);}
 int min = a[0];
 int min2 = 0;
 int a1 = 1;
 int i = 0;
 while (i<n && a[i] !=0){
 if (a[i] < min) {
  min = a[i];
  min2 = i;
  }
 a1 *= a[i];
 i++;
}
 printf("Номер мінімального елемента масиву: %d\n", min2);
 printf("Добуток елементів масиву до першого нульового елемента: %d\n", a1);

return 0;
}