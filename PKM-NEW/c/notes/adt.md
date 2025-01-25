
# ADT

<details>

<summary>Demo</summary>



```cpp
/** 线性表 - 单链表 - 带头结点 - 头插法与尾插法
 *  内容包括:
 *  带头结点的单链表的定义
 *  头插法
 *  尾插法
 *  销毁
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// 链式储存类型定义  
#define InitSize 10 // 默认最大长度
typedef struct LNode
{
	int data;
	struct LNode *next ;
}LNode, *LinkList;

// 输出操作
bool PrintList(LinkList L){
	LNode* p = L->next;
	if(p==NULL) return false;
	do{
		printf("%d ",p->data);
		p = p->next;
	}while(p!=NULL);
	printf("\n");
	return true;
}

// 销毁
void DestroyList(LinkList &L)
{
	LNode *p = L, *q = L;
	while(p){
		q=p;
		p = p->next;
		free(q);
	}
	L=NULL;
}

// 头插法 (包含初始化)
LinkList List_HeadInsert(LinkList &L)
{
	// 初始化
	L = (LNode*)malloc(sizeof(LNode));       // 0
	if(L==NULL) return L; // 内存不足
	L->next=NULL; // 进行初始化 如果初始化, 可能指向随机的内存.
	// 添加结点
	fflush(stdin);
	int x,count=0;
	LNode* s;
	while(InitSize>count && scanf("%d",&x))
	{
		s = (LNode*)malloc(sizeof(LNode));
		if(s==NULL) return L; // 内存不足
		s->data = x;
		s->next = L->next;
		L->next = s;
		count++;
	}
	return L;
}

// 尾插法 (包含初始化)
LinkList List_TailInsert(LinkList &L)
{
	// 初始化
	L = (LNode*)malloc(sizeof(LNode));
	if(L==NULL) return L; // 内存不足
	//L->next=NULL; // 进行初始化  - 尾插法可以不加, 但最好都加上, 养成好习惯.
	// 添加结点
	fflush(stdin);
	int x,count=0; 
	LNode* p = L;
	while(InitSize>count && scanf("%d",&x))
	{
		// 对头节点进行后插操作
		p->next = (LNode*)malloc(sizeof(LNode));
		if(p->next==NULL) return L; // 内存不足
		p->next->data = x;
		p = p->next; 
		count++;
	}
	p->next = NULL;
	return L;
}

// 链表逆置
LinkList List_Inverse(LinkList &L1){
	// 头插法的性质应用
	// 初始化新链表
	LinkList L2 = (LNode*)malloc(sizeof(LNode)); 
	L2->next = NULL;
	// 逆置
	LNode* p = L1->next;
	while(p!=NULL){
		// 分配新节点
		LNode* s = (LNode*)malloc(sizeof(LNode));
		if(s==NULL)
			return L2;
		// 赋值
		s->next = L2->next;
		s->data = p->data;
		L2->next = s;
		// 移动
		p = p->next;
	}
	return L2;
}

int main(void){
	printf("线性表 - 单链表 - 头插法\n");

	// 单链表 - 带头结点
	LinkList L1;

	// 头插法
	List_HeadInsert(L1);

	// 打印
	PrintList(L1);

	// 练习 - 链表逆置
	LinkList L3 = List_Inverse(L1);
	printf("练习 - 链表逆置\n");
	PrintList(L3);

	// 销毁
	DestroyList(L1);

	printf("线性表 - 单链表 - 尾插法\n");

	// 单链表 - 带头结点
	LinkList L2;

	// 尾插法
	List_TailInsert(L2);

	// 打印
	PrintList(L2);

	// 销毁
	DestroyList(L2);

	return 0;
}
```

</details>

后边衔接数据结构了，请看我的 github：[https://github.com/CharlesShan-hub/DataStructureNotes](https://github.com/CharlesShan-hub/DataStructureNotes)
