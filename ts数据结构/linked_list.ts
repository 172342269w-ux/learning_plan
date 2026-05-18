// 单链表

// 元素类型
type ElemType = number;

// 链表节点
class Node {
    data: ElemType;
    next: Node | null;

    constructor(data: ElemType = 0, next: Node | null = null) {
        this.data = data;
        this.next = next;
    }
}

// 单链表类
class LinkedList {
    private head: Node;

    // 创建单链表
    constructor() {
        this.head = new Node(0, null);
    }

    // 头加上元素
    add(e: ElemType): void {
        const newnode = new Node(e);
        newnode.next = this.head.next;
        this.head.next = newnode;
    }

    // 尾部加上元素
    addTail(e: ElemType): void {
        const newnode = new Node(e);
        newnode.next = null;
        // 找到链表的尾部
        let tail = this.head;
        while (tail.next !== null) {
            tail = tail.next;
        }
        // 将新节点添加到尾部
        tail.next = newnode;
    }

    // 删除单链表指定位置的元素
    delete(pos: number): void {
        if (pos <= 0) {
            return;
        }
        let current: Node | null = this.head;
        let count = 0;
        while (current !== null && count < pos - 1) {
            current = current.next;
            count++;
        }
        if (current === null || current.next === null) {
            return;
        }
        const temp = current.next; // 保存要删除的节点
        current.next = temp.next;
        // JS 自动垃圾回收，无需手动 free
    }

    // 插入元素
    insert(pos: number, e: ElemType): number {
        if (pos < 1) {
            return 0;
        }
        let current: Node | null = this.head.next;
        let count = 1;
        while (current !== null && count < pos - 1) {
            current = current.next;
            count++;
        }
        if (current === null) {
            return 0;
        }
        const newnode = new Node(e);
        newnode.next = current.next;
        current.next = newnode;
        return 1;
    }

    // 遍历单链表
    printList(): void {
        let current = this.head.next;
        const output: string[] = [];
        while (current !== null) {
            output.push(String(current.data));
            current = current.next;
        }
        console.log(output.join(" "));
    }

    // 获取单链表长度
    length(): number {
        let count = 0;
        let current = this.head.next;
        while (current !== null) {
            current = current.next;
            count++;
        }
        return count;
    }

    // 释放单链表内存（JS 自动回收，置空引用即可）
    freeList(): void {
        this.head.next = null;
    }

    // 练习：找出倒数第 pos 个元素（方法一：先遍历求总数，再定位）
    xiti(pos: number): void {
        // 先遍历链表，找出总体个数
        let current = this.head.next;
        let count = 1;
        while (current !== null) {
            current = current.next;
            count++;
        }

        const target = count - pos + 1;
        let current2 = this.head.next;
        count = 1;
        while (current2 !== null && count < target - 1) {
            current2 = current2.next;
            count++;
        }
        if (current2 === null) {
            console.log("Position is out of bounds.");
            return;
        }
        console.log(`The ${pos}-th element from the end is: ${current2.data}`);
    }

    // 练习：找出倒数第 pos 个元素（方法二：快慢指针）
    xiti2(pos: number): void {
        let fast = this.head.next;
        let slow = this.head.next;
        // 快慢指针，快指针先走 pos 步；
        for (let i = 0; i < pos; i++) {
            if (fast !== null) {
                fast = fast.next;
            }
        }
        // 快慢指针同时走，直到快指针到达链表末尾，此时慢指针指向的就是倒数第 pos 个元素
        while (fast !== null) {
            fast = fast.next;
            slow = slow!.next;
        }
        console.log(`The ${pos}-th element from the end is: ${slow!.data}`);
    }

    // 判断链表是否有环（快慢指针法）
    isCircle(): number {
        let fast = this.head.next;
        let slow = this.head.next;
        // 相当于跑步比赛，快指针每次走两步，慢指针每次走一步，如果链表有环，快指针和慢指针最终会相遇；如果链表无环，快指针会先到达链表末尾
        while (fast !== null && fast.next !== null) {
            fast = fast.next.next;
            slow = slow!.next;
            if (fast === slow) {
                return 1; // 链表有环
            }
        }
        return 0; // 链表无环
    }
}

// 主函数
function main(): void {
    const list = new LinkedList();
    list.add(1);
    list.add(2);
    list.add(3);
    list.addTail(4);
    list.addTail(5);
    list.insert(3, 10);
    list.delete(2);
    console.log("List: ");
    list.printList();
    console.log(`Length of the list: ${list.length()}`);
    list.xiti(2);
    list.xiti2(3);
    list.freeList();
    console.log("list is safely freed!");
}

main();
