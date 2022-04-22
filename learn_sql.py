'''
App -> DBMS -> DB

0. Concepts
    - Database is a collection of data and a method for accessing and manipulating the data.
        - Database is a structured set of computerized data with an accessible interface.
    - Database Management System is the interface for your app to talk to the Database.
        - What makes DBMS unique are the features they offer, not the language(SQL). [like permission/security/speed]
    - SQL is the language we use to talk to our Databases.
    - MySQL is a DBMS and working with MySQL is pretty much writing SQL all the time.
    - 


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

3. 关系模型
    - 关系数据库是建立在关系模型上的。而关系模型本质上就是若干个存储数据的二维表，可以把它们看作很多Excel表。
        - 表的每一行称为记录（Record），记录是一个逻辑意义上的数据。
        - 表的每一列称为字段（Column），同一个表的每一行记录都拥有相同的若干字段。
            - 字段定义了数据类型（整型、浮点型、字符串、日期等），以及是否允许为NULL。
            - 注意NULL表示字段数据不存在。一个整型字段如果为NULL不表示它的值为0，同样的，一个字符串型字段为NULL也不表示它的值为空串''。
            - 通常情况下，字段应该避免允许为NULL。不允许为NULL可以简化查询条件，加快查询速度，也利于应用程序读取数据后无需判断是否为NULL。
        - 和Excel表有所不同的是，关系数据库的表和表之间需要建立“一对多”，“多对一”和“一对一”的关系，这样才能够按照应用程序的逻辑来组织和存储数据。在关系数据库中，关系是通过主键和外键来维护的。
            - 主键
                - 主键是关系表中记录的唯一标识。对于关系表，有个很重要的约束，就是任意两条记录不能重复，即能够通过某个字段唯一区分出不同的记录，这个字段被称为主键。
                - 对主键的要求，最关键的一点是：记录一旦插入到表中，主键最好不要再修改，因为主键是用来唯一定位记录的，修改了主键，会造成一系列的影响。
                    - 由于主键的作用十分重要，如何选取主键会对业务开发产生重要影响。如果我们以学生的身份证号作为主键，似乎能唯一定位记录。然而，身份证号也是一种业务场景，如果身份证号升位了，或者需要变更，作为主键，不得不修改的时候，就会对业务产生严重影响。所以，选取主键的一个基本原则是：不使用任何业务相关的字段作为主键。主键也不应该允许NULL。
                - 作为主键最好是完全业务无关的字段，我们一般把这个字段命名为id。常见的可作为id字段的类型有：
                    - 自增整数类型：数据库会在插入数据时自动为每一条记录分配一个自增整数，这样我们就完全不用担心主键重复，也不用自己预先生成主键；
                        - 对于大部分应用来说，通常自增类型的主键就能满足需求。我们在students表中定义的主键也是BIGINT NOT NULL AUTO_INCREMENT类型。
                        - 如果使用INT自增类型，那么当一张表的记录数超过2147483647（约21亿）时，会达到上限而出错。使用BIGINT自增类型则可以最多约922亿亿条记录。
                    - 全局唯一GUID类型：使用一种全局唯一的字符串作为主键，类似8f55d96b-8acc-4636-8cb8-76bf8abc2f57。GUID算法通过网卡MAC地址、时间戳和随机数保证任意计算机在任意时间生成的字符串都是不同的，大部分编程语言都内置了GUID算法，可以自己预算出主键。
                - 关系数据库实际上还允许通过多个字段唯一标识记录，即两个或更多的字段都设置为主键，这种主键被称为联合主键。对于联合主键，允许一列有重复，只要不是所有主键列都重复即可。没有必要的情况下，我们尽量不使用联合主键，因为它给关系表带来了复杂度的上升。
            - 外键
                - 关系数据库通过外键可以实现一对多、多对多和一对一的关系。外键既可以通过数据库来约束，也可以不设置约束，仅依靠应用程序的逻辑来保证。
                - 在students表中，通过class_id的字段，可以把数据与另一张表关联起来，这种列称为外键。外键并不是通过列名实现的，而是通过定义外键约束实现的：
                    ALTER TABLE students
                    ADD CONSTRAINT fk_class_id
                    FOREIGN KEY (class_id)
                    REFERENCES classes (id);
                    其中，外键约束的名称fk_class_id可以任意，FOREIGN KEY (class_id)指定了class_id作为外键，REFERENCES classes (id)指定了这个外键将关联到classes表的id列（即classes表的主键）。
                - 通过定义外键约束，关系数据库可以保证无法插入无效的数据。即如果classes表不存在id=99的记录，students表就无法插入class_id=99的记录。
                - 由于外键约束会降低数据库的性能，大部分互联网应用程序为了追求速度，并不设置外键约束，而是仅靠应用程序自身来保证逻辑的正确性。这种情况下，class_id仅仅是一个普通的列，只是它起到了外键的作用而已。
                - 要删除一个外键约束，也是通过ALTER TABLE实现的
                    ALTER TABLE students
                    DROP FOREIGN KEY fk_class_id;
                    注意：删除外键约束并没有删除外键这一列。删除列是通过DROP COLUMN ...实现的。
                - 多对多关系实际上是通过两个一对多关系实现的，即通过一个中间表，关联两个一对多关系，就形成了多对多关系。
                - 一对一关系是指，一个表的记录对应到另一个表的唯一一个记录。
                    - 如果业务允许，完全可以把两个表合为一个表。
                    - 还有一些应用会把一个大表拆成两个一对一的表，目的是把经常读取和不经常读取的字段分开，以获得更高的性能。
        - 索引：通过对数据库表创建索引，可以提高查询速度。数据库索引对于用户和应用程序来说都是透明的。
            - 索引是关系数据库中对某一列或多个列的值进行预排序的数据结构。通过使用索引，可以让数据库系统不必扫描整个表，而是直接定位到符合条件的记录，这样就大大加快了查询速度。
            - 如果要经常根据score列进行查询，就可以对score列创建索引
                ALTER TABLE students
                ADD INDEX idx_score (score);
                使用ADD INDEX idx_score (score)就创建了一个名称为idx_score，使用列score的索引。
                
                索引名称是任意的，索引如果有多列，可以在括号里依次写上
                ALTER TABLE students
                ADD INDEX idx_score (score, name);
            - 索引的效率取决于索引列的值是否散列，即该列的值如果越互不相同，那么索引效率越高。
            - 可以对一张表创建多个索引。索引的优点是提高了查询效率，缺点是在插入、更新和删除记录时，需要同时修改索引，因此，索引越多，插入、更新和删除记录的速度就越慢。(利于查询；不利于读写)
            - 对于主键，关系数据库会自动对其创建主键索引。使用主键索引的效率是最高的，因为主键会保证绝对唯一。
            - 通过创建唯一索引 / 使用唯一约束，可以保证某一列的值具有唯一性。
                唯一索引：
                ALTER TABLE students
                ADD UNIQUE INDEX uni_name (name);
                
                唯一约束：
                ALTER TABLE students
                ADD CONSTRAINT uni_name UNIQUE (name); 

4. 查询数据
    - 使用SELECT查询的基本语句SELECT * FROM <表名>可以查询一个表的所有行和所有列的数据。
    - SELECT查询的结果是一个二维表。    
    - 虽然SELECT可以用作计算，但它并不是SQL的强项。但是，不带FROM子句的SELECT语句有一个有用的用途，就是用来判断当前到数据库的连接是否有效。许多检测工具会执行一条SELECT 1;来测试数据库连接。
    - 条件查询：SELECT语句可以通过WHERE条件来设定查询条件，查询结果是满足查询条件的记录。  
        条件	表达式举例1	表达式举例2	说明
        使用=判断相等	score = 80	name = 'abc'	字符串需要用单引号括起来
        使用>判断大于	score > 80	name > 'abc'	字符串比较根据ASCII码，中文字符比较根据数据库设置
        使用>=判断大于或相等	score >= 80	name >= 'abc'	
        使用<判断小于	score < 80	name <= 'abc'	
        使用<=判断小于或相等	score <= 80	name <= 'abc'	
        使用<>判断不相等	score <> 80	name <> 'abc'	
        使用LIKE判断相似	name LIKE 'ab%'	name LIKE '%bc%'	%表示任意字符，例如'ab%'将匹配'ab'，'abc'，'abcd'
    - 投影查询：使用SELECT *表示查询表的所有列，使用SELECT 列1, 列2, 列3则可以仅返回指定列，这种操作称为投影查询。
        - SELECT语句可以对结果集的列进行重命名:
            SELECT id, score points, name FROM students
            SELECT 列1 别名1, 列2 别名2, 列3 别名3 FROM ...。
    - 排序：使用ORDER BY可以对结果集进行排序，还可以对多列进行升序、倒序排序。
        - 默认的排序规则是ASC：“升序”，即从小到大。ASC可以省略，即ORDER BY score ASC和ORDER BY score效果一样。
        - 需要倒序排列就加个关键字DESC。
        - 如果有WHERE子句，那么ORDER BY子句要放到WHERE子句后面。
    - 分页查询：分页实际上就是从结果集中“截取”出第M~N条记录。这个查询可以通过LIMIT <N-M> OFFSET <M>子句实现。
        - 分页查询需要先确定每页的数量和当前页数，然后确定LIMIT和OFFSET的值。
        - LIMIT 3 OFFSET 0表示，对结果集从0号记录开始，最多取3条。注意SQL记录集的索引从0开始。
        - 如果要查询第2页，那么我们只需要“跳过”头3条记录，也就是对结果集从3号记录开始查询，把OFFSET设定为3。
            LIMIT 3 OFFSET 3
        - LIMIT 3表示的意思是“最多3条记录”，最终结果集按实际数量显示。
        - OFFSET超过了查询的最大数量并不会报错，而是得到一个空的结果集。
        - OFFSET是可选的，如果只写LIMIT 15，那么相当于LIMIT 15 OFFSET 0。
        - 在MySQL中，LIMIT 15 OFFSET 30还可以简写成LIMIT 30, 15。
        - 使用LIMIT <M> OFFSET <N>分页时，随着N越来越大，查询效率也会越来越低。
    - 聚合查询：使用聚合函数进行查询，就是聚合查询，它可以快速获得结果。
        - 使用SQL提供的聚合查询，我们可以方便地计算总数COUNT、合计值SUM、平均值AVG、最大值MAX和最小值MIN；
        - 通常，使用聚合查询时，我们应该给列名设置一个别名，便于处理结果
        - 除了COUNT()函数【计算某一列的行数】外，SQL还提供了如下聚合函数：
            函数	说明
            SUM	计算某一列的合计值，该列必须为数值类型
            AVG	计算某一列的平均值，该列必须为数值类型
            MAX	计算某一列的最大值
            MIN	计算某一列的最小值
            注意，MAX()和MIN()函数并不限于数值类型。如果是字符类型，MAX()和MIN()会返回排序最后和排序最前的字符。
        - 要特别注意：如果聚合查询的WHERE条件没有匹配到任何行，COUNT()会返回0，而SUM()、AVG()、MAX()和MIN()会返回NULL
        - 每页3条记录，如何通过聚合查询获得总页数？
            SELECT CEILING(COUNT(*)/3) FROM students;
        - 对于聚合查询，SQL还提供了“分组聚合”的功能，该功能通过GROUP BY实现。也可以使用多个列进行分组。
        - 聚合查询也可以添加WHERE条件。（WHERE, GROUP BY, HAVING）
    - 多表查询：使用多表查询可以获取M x N行记录；多表查询的结果集可能非常巨大，要小心使用。
        - SELECT * FROM students, classes
            这种一次查询两个表的数据，查询的结果也是一个二维表，它是students表和classes表的“乘积”，即students表的每一行与classes表的每一行都两两拼在一起返回。结果集的列数是students表和classes表的列数之和，行数是students表和classes表的行数之积。这种多表查询又称笛卡尔查询。
        - 注意，多表查询时，要使用表名.列名这样的方式来引用列和设置别名，这样就避免了结果集的列名重复问题。
        - 用表名.列名这种方式列举两个表的所有列实在是很麻烦，所以SQL还允许给表设置一个别名。注意到FROM子句给表设置别名的语法是FROM <表名1> <别名1>, <表名2> <别名2>。
        - 多表查询也是可以添加WHERE条件的。
    - 连接查询：JOIN查询需要先确定主表，然后把另一个表的数据“附加”到结果集上
        - 连接查询是另一种类型的多表查询。连接查询对多个表进行JOIN运算，简单地说，就是先确定一个主表作为结果集，然后，把其他表的行有选择性地“连接”在主表结果集上。
        - 内连接——INNER JOIN：INNER JOIN只返回同时存在于两张表的行数据
            注意INNER JOIN查询的写法是：
                1. 先确定主表，仍然使用FROM <表1>的语法；
                2. 再确定需要连接的表，使用INNER JOIN <表2>的语法；
                3. 然后确定连接条件，使用ON <条件...>，这里的条件是s.class_id = c.id，表示students表的class_id列与classes表的id列相同的行需要连接；
                4. 可选：加上WHERE条件查询子句、ORDER BY排序等子句。
        - RIGHT OUTER JOIN返回右表都存在的行。如果某一行仅在右表存在，那么结果集就会以NULL填充剩下的字段。
        - LEFT OUTER JOIN返回左表都存在的行。如果某一行仅在左表存在，那么结果集就会以NULL填充剩下的字段。
        - FULL OUTER JOIN返回两张表的所有记录，并且，自动把对方不存在的列填充为NULL。

5. 修改数据
    - 关系数据库的基本操作就是增删改查，即CRUD：Create、Retrieve、Update、Delete。其中，对于查询，我们已经详细讲述了SELECT语句的详细用法。而对于增、删、改，对应的SQL语句分别是：
        INSERT：插入新记录；
        DELETE：删除已有记录；
        UPDATE：更新已有记录。
    - INSERT：使用INSERT，我们就可以一次向一个表中插入一条或多条记录。
        - INSERT INTO <表名> (字段1, 字段2, ...) VALUES (值1, 值2, ...);
        - 自增主键，它的值可以由数据库自己推算出来。此外，如果一个字段有默认值，那么在INSERT语句中也可以不出现。
        - 要注意，字段顺序不必和数据库表的字段顺序一致，但值的顺序必须和字段顺序一致。
        - 还可以一次性添加多条记录，只需要在VALUES子句中指定多个记录值，每个记录是由(...)包含的一组值
            INSERT INTO students (class_id, name, gender, score) VALUES
                (1, 'A', 'F', 100),
                (2, 'B', 'M', 100);
    - DELETE: 使用DELETE，我们就可以一次删除表中的一条或多条记录。
        - DELETE FROM <表名> WHERE ...;
        - DELETE语句的WHERE条件也是用来筛选需要删除的行，因此和UPDATE类似，DELETE语句也可以一次删除多条记录
            --  删除id=5,6,7的记录
            DELETE FROM students WHERE id >= 5 AND id <= 7;
        - 如果WHERE条件没有匹配到任何记录，DELETE语句不会报错，也不会有任何记录被删除。
        - 最后，要特别小心的是，和UPDATE类似，不带WHERE条件的DELETE语句会删除整个表的数据。所以，在执行DELETE语句时也要非常小心，最好先用SELECT语句来测试WHERE条件是否筛选出了期望的记录集，然后再用DELETE删除。
            -- 删除整个students表
            DELETE FROM students
        - MySQL
            - 在使用MySQL这类真正的关系数据库时，DELETE语句也会返回删除的行数以及WHERE条件匹配的行数。
    - UPDATE:使用UPDATE，我们就可以一次更新表中的一条或多条记录。
        - UPDATE <表名> SET 字段1=值1, 字段2=值2, ... WHERE ...;
        - 注意到UPDATE语句的WHERE条件和SELECT语句的WHERE条件其实是一样的，因此完全可以一次更新多条记录;
            -- 更新id=5,6,7的记录
            UPDATE students SET name='a', score=60 WHERE id >= 5 AND id <= 7;
        - 在UPDATE语句中，更新字段时可以使用表达式。
            -- 更新score<80的记录
            UPDATE students SET score=score+10 WHERE score<80;
        - 如果WHERE条件没有匹配到任何记录，UPDATE语句不会报错，也不会有任何记录被更新。
        - 最后，要特别小心的是，UPDATE语句可以没有WHERE条件。这时，整个表的所有记录都会被更新。所以，在执行UPDATE语句时要非常小心，最好先用SELECT语句来测试WHERE条件是否筛选出了期望的记录集，然后再用UPDATE更新。
        - MySQL
            - 在使用MySQL这类真正的关系数据库时，UPDATE语句会返回更新的行数以及WHERE条件匹配的行数。

6. 一种最流行的开源数据库MySQL的基本安装和使用方法
    - MySQL是目前应用最广泛的开源关系数据库。MySQL最早是由瑞典的MySQL AB公司开发，该公司在2008年被SUN公司收购，紧接着，SUN公司在2009年被Oracle公司收购，所以MySQL最终就变成了Oracle旗下的产品。
    - 和其他关系数据库有所不同的是，MySQL本身实际上只是一个SQL接口，它的内部还包含了多种数据引擎，常用的包括：
        - InnoDB：由Innobase Oy公司开发的一款支持事务的数据库引擎，2006年被Oracle收购；
        - MyISAM：MySQL早期集成的默认数据库引擎，不支持事务。
    - MySQL接口和数据库引擎的关系就好比某某浏览器和浏览器引擎（IE引擎或Webkit引擎）的关系。对用户而言，切换浏览器引擎不影响浏览器界面，切换MySQL引擎不影响自己写的应用程序使用MySQL的接口。使用MySQL时，不同的表还可以使用不同的数据库引擎。如果你不知道应该采用哪种引擎，记住总是选择InnoDB就好了。
    - 因为MySQL一开始就是开源的，所以基于MySQL的开源版本，又衍生出了各种版本：
        - MariaDB：由MySQL的创始人创建的一个开源分支版本，使用XtraDB引擎。
        - Aurora：由Amazon改进的一个MySQL版本，专门提供给在AWS托管MySQL用户，号称5倍的性能提升。
        - PolarDB：由Alibaba改进的一个MySQL版本，专门提供给在阿里云托管的MySQL用户，号称6倍的性能提升。
    - 命令行程序mysql实际上是MySQL客户端，真正的MySQL服务器程序是mysqld，在后台运行。
    - 管理MySQL
        - MySQL Workbench可以用可视化的方式查询、创建和修改数据库表，但是，归根到底，MySQL Workbench是一个图形客户端，它对MySQL的操作仍然是发送SQL语句并执行。因此，本质上，MySQL Workbench和MySQL Client命令行都是客户端，和MySQL交互，唯一的接口就是SQL。
        - 因此，MySQL提供了大量的SQL语句用于管理。虽然可以使用MySQL Workbench图形界面来直接管理MySQL，但是，很多时候，通过SSH远程连接时，只能使用SQL命令，所以，了解并掌握常用的SQL管理操作是必须的。
        - 数据库
            - 在一个运行MySQL的服务器上，实际上可以创建多个数据库（Database）。
            - 要列出所有数据库，使用命令：SHOW DATABASES;
                - 其中，information_schema、mysql、performance_schema和sys是系统库，不要去改动它们。其他的是用户创建的数据库。
            - 要创建一个新数据库，使用命令：CREATE DATABASE test;
            - 要删除一个数据库，使用命令：DROP DATABASE test;
                - 注意：删除一个数据库将导致该数据库的所有表全部被删除。
            - 对一个数据库进行操作时，要首先将其切换为当前数据库：USE test;
        - 表
            - 列出当前数据库的所有表，使用命令：SHOW TABLES;
            - 要查看一个表的结构，使用命令：DESC students;
            - 还可以使用以下命令查看创建表的SQL语句: SHOW CREATE TABLE students;
            - 创建表使用CREATE TABLE语句，而删除表使用DROP TABLE语句: 
                CREATE TABLE students(
                    'id' bigint(20) NOT NULL AUTO_INCREMENT,
                    'class_id' bigint(20) NOT NULL,
                    'name' varchar(100) NOT NULL,
                    'gender' varchar(1) NOT NULL,
                    'score' int(11) NOT NULL,
                    PRIMARY KEY ('id')
                ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

                 DROP TABLE students;
            - 修改表就比较复杂。如果要给students表新增一列birth，使用：
                ALTER TABLE students ADD COLUMN birth VARCHAR(10) NOT NULL;
            - 要修改birth列，例如把列名改为birthday，类型改为VARCHAR(20)：
                ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(20) NOT NULL;
            - 要删除列，使用：
                ALTER TABLE students DROP COLUMN birthday;
            - 使用EXIT命令退出MySQL
                mysql> EXIT
                Bye
            - 注意EXIT仅仅断开了客户端和服务器的连接，MySQL服务器仍然继续运行。
        - 实用SQL语句
            - 插入或替换
                - 如果我们希望插入一条新记录（INSERT），但如果记录已经存在，就先删除原记录，再插入新记录。此时，可以使用REPLACE语句，这样就不必先查询，再决定是否先删除再插入：
                REPLACE INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99);
                若id=1的记录不存在，REPLACE语句将插入新记录，否则，当前id=1的记录将被删除，然后再插入新记录。
            - 插入或更新
                - 如果我们希望插入一条新记录（INSERT），但如果记录已经存在，就更新该记录，此时，可以使用INSERT INTO ... ON DUPLICATE KEY UPDATE ...语句
                INSERT INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99) ON DUPLICATE KEY UPDATE name='小明', gender='F', score=99;
            - 插入或忽略
                - 如果我们希望插入一条新记录（INSERT），但如果记录已经存在，就啥事也不干直接忽略，此时，可以使用INSERT IGNORE INTO ...语句：
                INSERT IGNORE INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99);
            - 快照
                - 复制一份当前表的数据到一个新表，可以结合CREATE TABLE和SELECT:
                    CREATE TABLE students_of_class1 SELECT * FROM students WHERE class_id=1;
                    新创建的表结构和SELECT使用的表结构完全一致。
            - 写入查询结果集:
                - 如果查询结果集需要写入到表中，可以结合INSERT和SELECT，将SELECT语句的结果集直接插入到指定表中:
                    CREATE TABLE statistics (
                        id BIGINT NOT NULL AUTO_INCREMENT,
                        class_id BIGINT NOT NULL,
                        average DOUBLE NOT NULL,
                        PRIMARY KEY (id)
                    );
                    ----------------------------------------------------------------
                    INSERT INTO statistics (class_id, average) SELECT class_id, AVG(score) FROM students GROUP BY class_id;
            - 强制使用指定索引
                - 在查询的时候，数据库系统会自动分析查询语句，并选择一个最合适的索引。但是很多时候，数据库系统的查询优化器并不一定总是能使用最优索引。如果我们知道如何选择索引，可以使用FORCE INDEX强制查询使用指定的索引。
                    SELECT * FROM students FORCE INDEX (idx_class_id) WHERE class_id = 1 ORDER BY id DESC;
                    指定索引的前提是索引idx_class_id必须存在。
                    ALTER TABLE students
                    ADD INDEX idx_class_id (class_id);

7. 事务
    - 把多条语句作为一个整体进行操作的功能，被称为数据库事务。
    - 数据库事务可以确保该事务范围内的所有操作都可以全部成功或者全部失败。如果事务失败，那么效果就和没有执行这些SQL一样，不会对数据库数据有任何改动。（事务范围内操作要么都做，要么都没做）
    - 数据库事务具有ACID这4个特性：
        A：Atomic，原子性，将所有SQL作为原子工作单元执行，要么全部执行，要么全部不执行；
        C：Consistent，一致性，事务完成后，所有数据的状态都是一致的，即A账户只要减去了100，B账户则必定加上了100；
        I：Isolation，隔离性，如果有多个事务并发执行，每个事务作出的修改必须与其他事务隔离；
        D：Duration，持久性，即事务完成后，对数据库数据的修改被持久化存储。
    - 对于单条SQL语句，数据库系统自动将其作为一个事务执行，这种事务被称为隐式事务。
    - 要手动把多条SQL语句作为一个事务执行，使用BEGIN开启一个事务，使用COMMIT提交一个事务，这种事务被称为显式事务。
        BEGIN;
        UPDATE accounts SET balance = balance - 100 WHERE id = 1;
        UPDATE accounts SET balance = balance + 100 WHERE id = 2;
        COMMIT;
        --COMMIT是指提交事务，即试图把事务内的所有SQL所做的修改永久保存。如果COMMIT语句执行失败了，整个事务也会失败。
    - 有些时候，我们希望主动让事务失败，这时，可以用ROLLBACK回滚事务，整个事务会失败
        BEGIN;
        UPDATE accounts SET balance = balance - 100 WHERE id = 1;
        UPDATE accounts SET balance = balance + 100 WHERE id = 2;
        ROLLBACK;
    - 数据库事务是由数据库系统保证的，我们只需要根据业务逻辑使用它就可以。
    - 隔离级别
        - 对于两个并发执行的事务，如果涉及到操作同一条记录的时候，可能会发生问题。因为并发操作会带来数据的不一致性，包括脏读、不可重复读、幻读等。数据库系统提供了隔离级别来让我们有针对性地选择事务的隔离级别，避免数据不一致的问题（隔离性）。
        - SQL标准定义了4种隔离级别，分别对应可能出现的数据不一致的情况
            solation Level	脏读（Dirty Read）	不可重复读（Non Repeatable Read）	幻读（Phantom Read）
            Read Uncommitted	Yes	            Yes	                                Yes
            Read Committed	    -	            Yes                                 Yes
            Repeatable Read	    -	            -	                                Yes
            Serializable	    -	            -	                                -
        
        - Read Uncommitted
            - Read Uncommitted是隔离级别最低的一种事务级别。在这种隔离级别下，一个事务会读到另一个事务更新后但未提交的数据，如果另一个事务回滚，那么当前事务读到的数据就是脏数据，这就是脏读（Dirty Read）。
                SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
            - 在Read Uncommitted隔离级别下，一个事务可能读取到另一个事务更新但未提交的数据，这个数据有可能是脏数据。
        - Read Committed
            - 在Read Committed隔离级别下，一个事务可能会遇到不可重复读（Non Repeatable Read）的问题。
                SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
            - Non Repeatable Read 不可重复读是指，在一个事务内，多次读同一数据，在这个事务还没有结束时，如果另一个事务恰好修改了这个数据，那么，在第一个事务中，两次读取的数据就可能不一致。
            - 在Read Committed隔离级别下，事务不可重复读同一条记录，因为很可能读到的结果不一致。
        - Repeatable Read
            - 在Repeatable Read隔离级别下，一个事务可能会遇到幻读（Phantom Read）的问题。
                SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
            - 幻读是指，在一个事务中，第一次查询某条记录，发现没有（哪怕是在另一个事物INSERT INTO这条记录并COMMIT之后，重复读这条记录还是不存在，确保重复读的正确性），但是，当试图更新这条不存在的记录时，竟然能成功(可以是另一个事务INSERT INTO这条记录并COMMIT了)，并且，再次读取同一条记录，它就神奇地出现了。
            - 幻读就是没有读到的记录，以为不存在，但其实是可以更新成功的，并且，更新成功后，再次读取，就出现了。
        - Serializable 
            - Serializable是最严格的隔离级别。在Serializable隔离级别下，所有事务按照次序依次执行，因此，脏读、不可重复读、幻读都不会出现。
            - 虽然Serializable隔离级别下的事务具有最高的安全性，但是，由于事务是串行执行，所以效率会大大下降，应用程序的性能会急剧降低。如果没有特别重要的情景，一般都不会使用Serializable隔离级别。
            - 如果没有指定隔离级别，数据库就会使用默认的隔离级别。
                - 在MySQL中，如果使用InnoDB，默认的隔离级别是Repeatable Read。
        - 四种隔离级别用最简单的话来说：
            - READ UNCOMMITTED: 新事务可以读到其他事务还没提交（commit）的修改，可能读到脏数据【脏读+不可重复读+幻读】。
            - READ COMMITTED：新事务不可以读到其他事务还没提交的修改，但可以读到提交后的修改，可能两次读同一记录读到不同的数据【不可重复读+幻读】。
            - READ REPEATABLE：新事务重复读一个记录以第一次读到的结果为准，不管后续是否别的事务有没有对记录做修改，那可能别人改了你读不出来，但可以UPDATE你读不出来的记录。【幻读】
            - SERIALIZABLE：新事务得等之前事务结束后再执行，即串行执行。【无脏读/不可重复读/幻读问题，但效率低】

'''
