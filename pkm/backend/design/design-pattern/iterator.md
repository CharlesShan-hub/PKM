# 迭代器模式

> 按照《图解设计模式》进行整理

迭代器模式的核心逻辑：把迭代逻辑本身与数据存储结构分离。比如底层用array，List还是任何其他的内容都不会改变上层的调用方式。

## 案例一：访问书架上的书

`Aggregate` 接口负责声明某一个类使用了迭代器模式：
```java
public interface Aggregate{
    public abstract Iterator iterator();
}
```

`Iterator`接口负责声明迭代器本身提供的访问逻辑：
```java
public interface Iterator{
    public abstract boolean hasNext();
    public abstract Object next();
}
```

`Book`是本案例中被访问的对象
```java
public class Book{
    private String name;
    public Book(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
}
```

```java
public class Bookshelf implements Aggregate{
    private Book[] books:
    private int last 0;
    public Bookshelf(int maxsize){
        this.books = new Book[maxsize];
    }
    public Book getBookAt (int index)(
        return books[index];
    }
    public void appendBook(Book book)(
        this.books[last]book;
        last++;
    }
    public int getLength()(
        return last;
    }
    public Iterator iterator(){
        return new BookshelfIterator(this);
    }
}
```
## 案例二：书架扩容

