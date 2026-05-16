// 顺序表（数组列表）
#include "array_list.h"
#include <stdio.h>
#include <string.h>
typedef struct{
    int id;
    char name[20];
    int price;
}book;
typedef int ElemType;
#define maxsize 100
typedef struct{
    int data[maxsize];
    int length;
}list;

//创建顺序表
void initlist(list*L){
    L->length=0;
}
//在顺序表末尾添加元素
void add(list *L,ElemType e){
    if(L->length<maxsize&&L->length>=0){
        L->data[L->length]=e;
        L->length++;
    }
}
//在顺序表指定位置插入元素
int insert(list*L,int pos ,ElemType e){
  if(pos<1||pos>L->length+1){
      return 0;
  }
    if(L->length>=maxsize){
        return 0;
    }
    for(int i=L->length-1;i>=pos-1;i--){
        L->data[i+1]=L->data[i];
    }
    L->data[pos-1]=e;
    L->length++;
    return 1;
}
void  printlist(list*L){
    for(int i=0;i<L->length;i++){
        printf("%d ",L->data[i]);
    }
    printf("\n");
}
//删除顺序表指定位置的元素
int delete(list*L,int pos){
    if(pos<1||pos>L->length){
        return 0;
    }
   for(int i=pos-1;i<L->length-1;i++){
    L->data[i]=L->data[i+1];
   }
   L->length--;
   return 1;
}
//查找顺序表中指定元素的位置
int find(list*L,ElemType e){
    for(int i=0;i<L->length;i++){
        if(L->data[i]==e){
            return i+1;
        }
    }
    return 0;
}
//主函数
int main(){
     book b;
     b.id=1;
     strcpy(b.name,"C++ Primer");
     b.price=100;
     list L;
        initlist(&L);
        add(&L, 5);
        add(&L, 10);
        add(&L, 15);
        printlist(&L); 
        insert(&L, 2, 20);
        printlist(&L);
        delete(&L, 1);
        printlist(&L);
        
        printf("Element found at position: %d\n", find(&L, 20));
    return 0;
}