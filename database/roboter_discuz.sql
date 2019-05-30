-- # 增加ID列作为默认主键:
-- # 通过mapper建立映射的数据表必须带有主键, 如果没有主键就无法定位某
-- # 个table的某行, 就无法做Object-relational mapping这样的映射

-- sqlalchemy.exc.ArgumentError: Mapper Mapper|ForumMemberRecommend|bbs_forum_memberrecommend 
-- could not assemble any primary key columns for mapped table 'bbs_forum_memberrecommend'

alter table `discuzx`.`bbs_forum_memberrecommend`
add column `id` int not null auto_increment first,
add primary key (`id`);
