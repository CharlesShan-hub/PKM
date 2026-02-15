
# HJSON

直觉是，不常用。wiki 都没有介绍它，说是更人性化了，但少量的心智负担的降低，并不能抵消给生产环节添加的复杂度。

## Links

* 官网：[https://hjson.github.io/](https://hjson.github.io/)
* hjson给各个编程语言的适配：[https://github.com/hjson](https://github.com/hjson)
* rfc 标准：[https://hjson.github.io/rfc.html](https://hjson.github.io/rfc.html)
* 中文版本详细 blog：[https://blog.csdn.net/weixin\_43863487/article/details/129905402](https://blog.csdn.net/weixin\_43863487/article/details/129905402)

## Notes

1. 与 Json 的对比
   1. **注释：可以用 python 的井号，可以用 C 的单行多行注释。**
   2. **字符串：单行字符串可以不加引号，多行字符串用 python 一样的三个单引号。**
   3. **对象：键可以不加引号，值后边可以不写逗号。**
   4. **文件名：hjson**
2. rfc 中的 Demo

```toml
   # comments are useful

   # specify rate in requests/second
   rate: 1000

   #  you may also use
   // c style
   /* or block
      comments */

   # key names do not need to be placed in
   # quotes unless they contain a punctuator
   # character {}[],:
   key: 1

   # strings may also omit quotes if they do
   # not start with a punctuator
   text: look ma, no quotes!

   # quoteless strings do not use escapes
   # and end at the LF/newline

   # commas are optional
   commas:
   {
     one: 1
     two: 2
   }

   # trailing commas are allowed
   trailing:
   {
     one: 1,
     two: 2,
   }

   # multiline string
   haiku:
     '''
     JSON I love you.
     But you strangle my expression.
     This is so much better.
     '''

   # Hjson is a superset of JSON so you
   # may use any valid JSON syntax:
   favNumbers: [ 1, 2, 3, 6, 42 ]
```

