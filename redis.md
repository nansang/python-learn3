## redis下载，安装，运行

[redis下载地址](http://redis.io/download)

```
$ wget http://download.redis.io/releases/redis-3.2.4.tar.gz
$ tar xzf redis-3.2.4.tar.gz
$ cd redis-3.2.4
$ make

$ src/redis-server
```

[Mac环境下安装Redis](http://www.jianshu.com/p/6b5eca8d908b)

### python 和 redis 说白了都是数据结构

哪些数据结构，类比

字面上的意思,redis发布订阅，订阅频道

redis事务可以一次执行多个命令，并且带有以下两个重要的保证：

```
1.事务是一个单独的隔离操作：事务中的所有命令都会序列化，按顺序地执行。事务在执行的过程中，不会被其它客户端发送来的命令请求所打断。
2.事务是一个原子操作：事务中的命令要么全部被执行，要么全部都不执行。
```

键，字符串，哈希，列表，集合，有序集合，hyperloglog

管道技术

redis 是一种基于客户端－服务端模型以及请求/响应协议的tcp服务。这意味着通常情况下一个请求会遵循以下步聚

Redis 管道技术可以在服务端未响应时，客户端可以继续向服务端发送请求，并最终一次性读取所有服务端的响应。
