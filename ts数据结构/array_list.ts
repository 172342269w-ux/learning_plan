// 顺序表（数组列表）

// 图书类型
interface Book {
    id: number;
    name: string;
    price: number;
}

// 元素类型
type ElemType = number;

// 最大容量
const MAXSIZE = 100;

// 顺序表类
class ArrayList {
    private data: ElemType[];
    private length: number;

    // 创建顺序表
    constructor() {
        this.data = new Array<ElemType>(MAXSIZE).fill(0);
        this.length = 0;
    }

    // 在顺序表末尾添加元素
    add(e: ElemType): void {
        if (this.length < MAXSIZE && this.length >= 0) {
            this.data[this.length] = e;
            this.length++;
        }
    }

    // 在顺序表指定位置插入元素
    insert(pos: number, e: ElemType): number {
        if (pos < 1 || pos > this.length + 1) {
            return 0;
        }
        if (this.length >= MAXSIZE) {
            return 0;
        }
        for (let i = this.length - 1; i >= pos - 1; i--) {
            this.data[i + 1] = this.data[i]!;
        }
        this.data[pos - 1] = e;
        this.length++;
        return 1;
    }

    // 打印顺序表
    printList(): void {
        const output: string[] = [];
        for (let i = 0; i < this.length; i++) {
            output.push(String(this.data[i]));
        }
        console.log(output.join(" "));
    }

    // 删除顺序表指定位置的元素
    delete(pos: number): number {
        if (pos < 1 || pos > this.length) {
            return 0;
        }
        for (let i = pos - 1; i < this.length - 1; i++) {
            this.data[i] = this.data[i + 1]!;
        }
        this.length--;
        return 1;
    }

    // 查找顺序表中指定元素的位置
    find(e: ElemType): number {
        for (let i = 0; i < this.length; i++) {
            if (this.data[i] === e) {
                return i + 1;
            }
        }
        return 0;
    }
}

// 主函数
function main(): void {
    // 创建图书对象
    const b: Book = {
        id: 1,
        name: "C++ Primer",
        price: 100
    };
    console.log(`Book: id=${b.id}, name=${b.name}, price=${b.price}`);

    // 创建顺序表
    const L = new ArrayList();

    // 添加元素
    L.add(5);
    L.add(10);
    L.add(15);
    console.log("After add: ");
    L.printList();

    // 插入元素
    L.insert(2, 20);
    console.log("After insert at pos 2: ");
    L.printList();

    // 删除元素
    L.delete(1);
    console.log("After delete at pos 1: ");
    L.printList();

    // 查找元素
    console.log(`Element found at position: ${L.find(20)}`);
}

main();
