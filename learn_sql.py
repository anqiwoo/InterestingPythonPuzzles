'''
1. SQL是访问和操作关系数据库的计算机标准语言(SQL是结构化查询语言Structured Query Language的缩写)。
    - 无论用什么编程语言（Java、Python、C++……）编写程序，只要涉及到操作关系数据库，比如，一个电商网站需要把用户和商品信息存入数据库，或者一个手机游戏需要把用户的道具、通关信息存入数据库，都必须通过SQL来完成。
    - 所以，现代程序离不开关系数据库，要使用关系数据库就必须掌握SQL。
    - NoSQL: 非SQL的数据库，包括MongoDB、Cassandra、Dynamo等等，它们都不是关系数据库。
        1970: NoSQL = We have no SQL
        1980: NoSQL = Know SQL
        2000: NoSQL = No SQL!
        2005: NoSQL = Not only SQL
        2013: NoSQL = No, SQL!
    - 今天，SQL数据库仍然承担了各种应用程序的核心数据存储，而NoSQL数据库作为SQL数据库的补充，两者不再是二选一的问题，而是主从关系。所以，无论使用哪种编程语言，无论是Web开发、游戏开发还是手机开发，掌握SQL，是所有软件开发人员所必须的。
    - 虽然SQL已经被ANSI组织定义为标准，不幸地是，各个不同的数据库对标准的SQL支持不太一致。并且，大部分数据库都在标准的SQL上做了扩展。也就是说，如果只使用标准SQL，理论上所有数据库都可以支持，但如果使用某个特定数据库的扩展SQL，换一个数据库就不能执行了。例如，Oracle把自己扩展的SQL称为PL/SQL，Microsoft把自己扩展的SQL称为T-SQL。
    - 现实情况是，如果我们只使用标准SQL的核心功能，那么所有数据库通常都可以执行。不常用的SQL功能，不同的数据库支持的程度都不一样。而各个数据库支持的各自扩展的功能，通常我们把它们称之为“方言”。
    - 总的来说，SQL语言定义了这么几种操作数据库的能力：
        - DDL：Data Definition Language
            DDL允许用户定义数据，也就是创建表、删除表、修改表结构这些操作。通常，DDL由数据库管理员执行。
        - DML：Data Manipulation Language
            DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。
        - DQL：Data Query Language
            DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。
    - 语法特点：SQL语言关键字不区分大小写！！！但是，针对不同的数据库，对于表名和列名，有的数据库区分大小写，有的数据库不区分大小写。同一个数据库，有的在Linux上区分大小写，有的在Windows上不区分大小写。所以，建议：SQL关键字总是大写，以示突出，表名和列名均使用小写。

2. 关系数据库
    - 为什么需要数据库？因为应用程序需要保存用户的数据。数据库作为一种专门管理数据的软件就出现了。应用程序不需要自己管理数据，而是通过数据库软件提供的接口来读写数据。至于数据本身如何存储到文件，那是数据库软件的事情，应用程序自己并不关心。这样一来，编写应用程序的时候，数据读写的功能就被大大地简化了！
    - 数据模型：数据库按照数据结构来组织、存储和管理数据，实际上，数据库一共有三种模型
        - 层次模型：以“上下级”的层次关系来组织数据的一种方式，层次模型的数据结构看起来就像一颗树
        - 网状模型：把每个数据节点和其他很多节点都连接起来，它的数据结构看起来就像很多城市之间的路网
        - 关系模型：把数据看作是一个二维表格，任何数据都可以通过行号+列号来唯一确定，它的数据模型看起来就是一个Excel表
    - 随着时间的推移和市场竞争，最终，基于关系模型的关系数据库获得了绝对市场份额。Why？因为相比层次模型和网状模型，关系模型理解和使用起来最简单。
    - 数据类型
        - 对于一个关系表，除了定义每一列的名称外，还需要定义每一列的数据类型。
        - 关系数据库支持的标准数据类型包括数值、字符串、时间等。
        - 选择数据类型的时候，要根据业务规则选择合适的类型。通常来说，BIGINT能满足整数存储的需求，VARCHAR(N)能满足字符串存储的需求，这两种类型是使用最广泛的。
    - 主流关系数据库
        - 商用数据库，例如：Oracle，Microsoft SQL Server，IBM DB2等；
        - 开源数据库，例如：MySQL，PostgreSQL等；
        - 桌面数据库，以微软Access为代表，适合桌面应用程序使用；
        - 嵌入式数据库，以Sqlite为代表，适合手机应用和桌面程序。

3. 如何使用SQL操作数据库

4. 一种最流行的开源数据库MySQL的基本安装和使用方法
    - MySQL是目前应用最广泛的开源关系数据库。MySQL最早是由瑞典的MySQL AB公司开发，该公司在2008年被SUN公司收购，紧接着，SUN公司在2009年被Oracle公司收购，所以MySQL最终就变成了Oracle旗下的产品。
    - 和其他关系数据库有所不同的是，MySQL本身实际上只是一个SQL接口，它的内部还包含了多种数据引擎，常用的包括：
        - InnoDB：由Innobase Oy公司开发的一款支持事务的数据库引擎，2006年被Oracle收购；
        - MyISAM：MySQL早期集成的默认数据库引擎，不支持事务。
    - MySQL接口和数据库引擎的关系就好比某某浏览器和浏览器引擎（IE引擎或Webkit引擎）的关系。对用户而言，切换浏览器引擎不影响浏览器界面，切换MySQL引擎不影响自己写的应用程序使用MySQL的接口。使用MySQL时，不同的表还可以使用不同的数据库引擎。如果你不知道应该采用哪种引擎，记住总是选择InnoDB就好了。
    - 因为MySQL一开始就是开源的，所以基于MySQL的开源版本，又衍生出了各种版本：
        - MariaDB：由MySQL的创始人创建的一个开源分支版本，使用XtraDB引擎。
        - Aurora：由Amazon改进的一个MySQL版本，专门提供给在AWS托管MySQL用户，号称5倍的性能提升。
        - PolarDB：由Alibaba改进的一个MySQL版本，专门提供给在阿里云托管的MySQL用户，号称6倍的性能提升。
    



'''
