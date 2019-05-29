create schema `roboter` default character set utf8mb4 ;


create table `roboter`.`bbs_member` (
  `id` int not null auto_increment comment '自动编号',
  `username` varchar(45) not null comment '账户名',
  `password` varchar(45) not null comment '账户密码',
  `email` varchar(45) not null comment '邮箱',
  `dz_uid` int default 0 comment '论坛的uid',
  `create_datetime` timestamp not null comment '添入时间',
  primary key (`id`)  comment '自动注册用户'
) engine=innodb auto_increment=0 default charset=utf8mb4 comment='Fake账户表';


create table `roboter`.`bbs_attachment` (
  `id` int not null auto_increment comment '自动编号',
  `file_name` varchar(255) not null comment '文件名',
  `key_name` varchar(80) default '' comment '七牛文件名',
  `down_link` varchar(150) default '' comment '下载地址',
  `md5sum` varchar(80) default '' comment '文件信息摘要Hash',
  `plate` int default 0 comment '版块',
  `status` int default 0 comment '是否发帖(0:未传;1:已传;2:已发)',
  `author` varchar(45) default '' comment '所属用户',
  `create_datetime` timestamp not null comment '添入时间',
  `upload_datetime` timestamp null comment '上传时间',
  primary key (`id`)  comment '自动上传七牛文件'
) engine=innodb auto_increment=0 default charset=utf8mb4 comment='上传七牛文件表';


create table `roboter`.`bbs_surplus` (
  `id` int not null auto_increment comment '自动编号',
  `fid` int default 0 comment '版块',
  `path` varchar(255) not null comment '文件名',
  `md5sum` varchar(80) default '' comment '文件信息摘要Hash',
  `plate` int default 0 comment '版块',
  `author` varchar(45) default '' comment '所属用户',
  `create_datetime` timestamp not null comment '记录时间',
  primary key (`id`)  comment '文件重复日志'
) engine=innodb auto_increment=0 default charset=utf8mb4 comment='文件重复日志表';


create table `roboter`.`bbs_thread` (
  `id` int not null auto_increment comment '自动编号',
  `thread_id` int not null comment '主题ID',
  `post_id` int not null comment '帖子ID',
  `plate_id` int default 0 comment '版块ID',
  `attachment_id` int default 0 comment '附件ID',
  `robot_data_id` int default 0 comment '入库文件ID',
  `create_datetime` timestamp not null comment '添入时间',
  primary key (`id`)  comment '自动发文件帖子'
) engine=innodb auto_increment=0 default charset=utf8mb4 comment='自动发文件帖子表';


create table `roboter`.`bbs_post` (
  `id` int not null auto_increment comment '自动编号',
  `uid` int not null default 0 comment 'Dz用户Id',
  `tid` int not null default 0 comment 'Dz主题Id',
  `pid` int not null default 0 comment 'Dz帖子Id',
  `fid` int not null default 0 comment '版块ID',
  `create_datetime` timestamp not null comment '自动回帖时间',
  primary key (`id`) comment '自动回帖'
) engine=innodb auto_increment=0 default charset=utf8mb4 comment='自动回帖表';


alter table `roboter`.`bbs_attachment` add index( `status`);