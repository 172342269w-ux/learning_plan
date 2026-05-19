"use strict";
// 每周审计/W1_TS_Migration/linked_list.ts
// 1. 定义链表节点类（等价于 C++ 的 struct Node）
class ListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
// 2. 定义单链表管理类
class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }
    /**
     * 核心逻辑：尾插法插入新元素
     */
    append(element) {
        const newNode = new ListNode(element);
        // 情况 A：如果链表是空的，新节点直接作为头节点
        if (this.head === null) {
            this.head = newNode;
        }
        else {
            // 情况 B：链表不为空，需要人肉依靠循环找到最后一个节点
            let current = this.head;
            // 【请在这里手敲你的链表遍历逻辑】
            // 提示：利用 while 循环，只要 current.next 不为空，就一直往后跳
            // 循环结束后，将 current.next 指向 newNode
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        this.size++;
    }
    // 打印链表（用于测试）
    print() {
        let current = this.head;
        let res = "";
        while (current !== null) {
            res += current.data + " -> ";
            current = current.next; // 等价于 C++ 的 current = current->next;
        }
        console.log(res + "NULL");
    }
    // 继续在 LinkedList 类内部追加：
    /**
     * 核心逻辑：在指定下标位置插入新元素（等价于 C++ 的 insert_at）
     * @param index 插入的目标下标（从 0 开始）
     * @param element 要插入的值
     */
    insertAt(index, element) {
        // 1. 边界审计：index 不能小于 0，且不能大于当前链表长度 size（注意：index 等于 size 时等价于尾插）
        if (index < 0 || index > this.size) {
            console.log("Error: Index out of bounds!");
            return false;
        }
        const newNode = new ListNode(element);
        // 情况 A：插入到头部（index === 0）
        if (index === 0) {
            // 请手敲：让新节点的 next 指向当前的头节点，然后将头节点更新为新节点
            // 【请在这里手敲头插逻辑】
            newNode.next = this.head;
            this.head = newNode;
        }
        else {
            // 情况 B：插入到中间或尾部
            let prev = this.head;
            // 依靠循环找到目标位置的前驱节点（即 index - 1 位置的节点）
            for (let i = 0; i < index - 1; i++) {
                if (prev !== null)
                    prev = prev.next;
            }
            if (prev !== null) {
                // 请手敲修改连线的核心逻辑
                // 提示：1. 先让新节点的 next 指向 prev 的下一个节点
                //      2. 再让 prev 的 next 指向新节点（注意顺序绝对不能颠倒，否则链表会断开！）
                // 【请在这里手敲核心挂载逻辑】
                newNode.next = prev.next;
                prev.next = newNode;
            }
        }
        this.size++;
        return true;
    }
    /**
     * 核心逻辑：根据值删除第一个匹配的节点
     * @param element 要删除的值
     * @return 是否删除成功
     */
    remove(element) {
        if (this.head === null)
            return false;
        // 情况 A：如果要删的是头节点
        if (this.head.data === element) {
            this.head = this.head.next; // 直接让头指针跳过第一个节点
            this.size--;
            return true;
        }
        // 情况 B：要删的是中间或尾部节点
        let prev = this.head;
        // 循环条件：只要当前节点的下一个节点不为空，且下一个节点的数据不是我们要找的，就一直往后走
        while (prev.next !== null && prev.next.data !== element) {
            prev = prev.next;
        }
        // 循环结束后，如果 prev.next 不为空，说明找到了那个要删的节点（就是 prev.next）
        if (prev.next !== null) {
            // 请手敲：让 prev.next 指向要删节点的下一个节点（即 prev.next.next）
            // 【请在这里手敲物理连线抹除逻辑】
            prev.next = prev.next.next;
            this.size--;
            return true;
        }
        return false; // 没找到
    }
}
// ---- 测试用例 ----
const myLinkedList = new LinkedList();
myLinkedList.append(100);
myLinkedList.append(200);
myLinkedList.append(300);
myLinkedList.print(); // 预期输出: 100 -> 200 -> 300 -> NULL
// 测试链表的高级增删
const testList = new LinkedList();
testList.append(10);
testList.append(30);
testList.insertAt(1, 20); // 在下标 1 插入 20
testList.print(); // 预期输出: 10 -> 20 -> 30 -> NULL
testList.remove(20); // 删除 20
testList.print(); // 预期输出: 10 -> 30 -> NULL
