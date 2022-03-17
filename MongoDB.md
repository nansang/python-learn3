### MongoDB

关系数据库：ACID

### cap定理

## 概念解析(文档，集合，数据库)

### 和关系型的差别与联系，如下:

```
database --> database 数据库
    table --> collection 数据库表/集合
    row  --> document 数据记录行/文档
    column--> field 数据字段/域
    index --> index 索引
    table joins 表连接，mongodb不支持
    primary key --> primary key 主键，
    mongdb自动将_id字段设置为主键
```

[Mongodb for mac 的安装与配置](http://m.blog.csdn.net/article/details?id=51319368)

[python调用MongoDB](http://www.cnblogs.com/qingtianyu2015/p/5968398.html)

[MongoDB：关闭服务](http://francs3.blog.163.com/blog/static/405767272012101483936886/)

mongod 启动服务器

mongo 终端命令环境 [MongoDB命令学习](http://www.runoob.com/mongodb/mongodb-create-database.html)

```
show dbs
    db
    use local
```

存放位置：/usr/local/mongodb/bin/

127.0.0.1:27017

字典类型数据{key:value} json

Robomongo ---｛MongoDB客户端} 还是这个用着舒服点
