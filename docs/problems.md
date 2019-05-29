## 异常问题

    会报异常如下:
    sqlalchemy.exc.ArgumentError: Mapper Mapper|iky_forum_memberrecommend|
    iky_forum_memberrecommend could not assemble any primary key columns for
    mapped table 'iky_forum_memberrecommend'

    执行以下SQL修改表结构:
    alter table `iky_forum_memberrecommend`
    add `id` int(11) not null auto_increment
    primary key comment '自增编号' first ;
