// 单链表
#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>
typedef int ElemType;
typedef struct Node  {
    ElemType data;
    struct Node* next;
}Node;
//创建单链表
Node* initlist(){
    Node* head=(Node*)malloc(sizeof(Node));
    head->data=0;
    head->next=NULL;
    return head;
}
//头加上元素
void add(Node*L ,ElemType e){
    Node *newnode=(Node*)malloc(sizeof(Node));
    newnode->data=e;
    newnode->next=L->next;
    L->next=newnode;
}
//尾部加上元素
void addtail(Node*L,ElemType e){
    Node* newnode=(Node*)malloc(sizeof(Node));
    newnode->data=e;
    newnode->next=NULL;
    //找到链表的尾部
    Node* tail=L;
    while(tail->next!=NULL){
        tail=tail->next;
    }
    //将新节点添加到尾部
    tail->next=newnode;
}
//删除单链表指定位置的元素
void delet(Node*L,int pos){
    if(pos<=0){
        return;
    }
    Node* current=L;
    int count=0;
    while(current!=NULL&&count<pos-1){
        current=current->next;
        count++;
    }
    if(current==NULL||current->next==NULL){
        return;
    }
    Node* temp=current->next;//保存要删除的节点
    current->next=temp->next;
    free(temp);//释放内存

}
//插入元素
int insert(Node*L,int pos,ElemType e){
    if(pos<1){
        return 0;
    }
    Node* current=L->next;
    int count=1;
    while(current!=NULL&&count<pos-1){
        current=current->next;
        count++; 
    }
    if(current==NULL){
        return 0;
    }
    Node* newnode=(Node*)malloc(sizeof(Node));
    newnode->data=e;
    newnode->next=current->next;
    current->next=newnode;
    return 1;

}
//遍历单链表
void printlist(Node*L){
    Node* current=L->next;
    while(current!=NULL){
        printf("%d ",current->data);
        current=current->next;
    }printf("\n");
}
//获取单链表长度
int length(Node*L){
    int count=0;
    Node* current=L->next;
    while(current!=NULL){
        
        current=current->next;
        count++;
    }
    return count;
}
//释放单链表内存
void freelist(Node** L){
    Node* current =* L;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    *L = NULL;
}
void xiti(Node*L,int pos);
void xiti2(Node*L,int pos);
int main(){
    Node*list=initlist();
    add(list,1);
    add(list,2);
    add(list,3);
    addtail(list,4);
    addtail(list,5);
    insert(list,3,10);
    delet(list,2);
    printlist(list);
    printf("Length of the list: %d\n", length(list));
    xiti(list,2);
    xiti2(list,3);
    freelist(&list);
    if (list == NULL) {
        printf("list is NULL, safely freed!\n");
    }
    return 0;
}
//练习
void xiti(Node*L,int pos){
     //先遍历链表，找出总体个数
     Node* current=L->next;
     int count=1;
     while(current!=NULL){
       current=current->next;
       count++;
     } 

     int target=count-pos+1;
     Node* current2=L->next;
     count=1;
     while(current2!=NULL&&count<target-1){
        current2=current2->next;
        count++;
    }
    if(current2==NULL){
        printf("Position is out of bounds.\n");
        return;}
    printf("The %d-th element from the end is: %d\n", pos, current2->data);



}
void xiti2(Node*L,int pos){
    Node *fast=L->next;
    Node *slow=L->next;
    //快慢指针，快指针先走pos步；
    for(int i=0;i<pos;i++){
        fast=fast->next;
    }
    //快慢指针同时走，直到快指针到达链表末尾，此时慢指针指向的就是倒数第pos个元素
    while(fast!=NULL){
        fast=fast->next;
        slow=slow->next;
    }
    printf("The %d-th element from the end is: %d\n", pos, slow->data);
}
int iscircle(Node*L){
    Node* fast=L->next;
    Node* slow=L->next;
    //相当于跑步比赛，快指针每次走两步，慢指针每次走一步，如果链表有环，快指针和慢指针最终会相遇；如果链表无环，快指针会先到达链表末尾
    while(fast!=NULL&&fast->next!=NULL){
        fast=fast->next->next;
        slow=slow->next;
        if(fast==slow){
            return 1;//链表有环
        }
    }
    return 0;//链表无环
}