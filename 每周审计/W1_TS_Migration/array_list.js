"use strict";
// W1_TS_Migration/array_list.ts
class ArrayList {
    // 2. 构造函数：初始化物理空间
    constructor(capacity) {
        this.capacity = capacity;
        this.size = 0;
        // 在 TS 中，这会声明一个空数组，但我们在逻辑上限制它的容量
        this.data = new Array(capacity);
    }
    // 3. 核心逻辑：向末尾插入元素
    push(element) {
        // 底层边界审计：检查是否满了
        if (this.size >= this.capacity) {
            console.log("Error: ArrayList is full!");
            return false;
        }
        // 请你亲手写出：将 element 放入 data 的 size 位置，并将 size 自增
        // 【请在这里手敲你的核心逻辑】
        this.data[this.size] = element;
        this.size++;
        return true;
    }
    // 4. 核心逻辑：打印顺序表（用于验证）
    print() {
        let res = "";
        for (let i = 0; i < this.size; i++) {
            res += this.data[i] + " -> ";
        }
        console.log(res + "END");
    }
    // 继续在 ArrayList 类内部追加：
    /**
     * 核心逻辑：根据下标删除元素
     * @param index 要删除的元素的下标
     * @return 返回被删除的元素，如果下标非法则返回 -1
     */
    removeAt(index) {
        // 1. 边界审计：检查 index 是否小于 0 或者大于等于当前有效大小 size
        if (index < 0 || index >= this.size) {
            console.log("Error: Index out of bounds!");
            return -1;
        }
        // 2. 暂存被删除的值，用于最后返回
        const deletedValue = this.data[index];
        // 3. 数据搬移：请手敲数据向前覆盖的逻辑
        // 提示：从 index 开始，把后面的元素往前挪一位（this.data[i] = this.data[i+1]）
        // 【请在这里手敲你的搬移循环逻辑】
        for (let i = index; i < this.size - 1; i++) {
            this.data[i] = this.data[i + 1];
        }
        // 4. 维护有效大小 size
        // 【请手敲：size 应该怎么变？】
        this.size--;
        return deletedValue;
    }
    /**
     * 核心逻辑：查找某个元素在顺序表中的下标
     * @param element 要查找的值
     * @return 找到则返回第一次出现的下标，找不到返回 -1
     */
    find(element) {
        // 【请手敲：利用 for 循环遍历 data，找到相等的值就返回下标，遍历完没找到返回 -1】
        for (let i = 0; i < this.size; i++) {
            if (this.data[i] === element) {
                return i;
            }
        }
        return -1;
    }
}
// ---- 以下是测试用例 ----
const myList = new ArrayList(5);
myList.push(10);
myList.push(20);
myList.push(30);
myList.print(); // 预期输出: 10 -> 20 -> 30 -> END
// 测试删除与查找
myList.removeAt(1); // 删除 20
myList.print(); // 预期输出: 10 -> 30 -> END
console.log("Find 30 at index:", myList.find(30)); // 预期输出: 1
