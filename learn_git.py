'''
Ref: https://www.liaoxuefeng.com/wiki/896043488029600/896067008724000

# Summary
1. Git是目前世界上最先进的分布式版本控制系统（没有之一）。2008年，GitHub网站上线了，它为开源项目免费提供Git存储，无数开源项目开始迁移至GitHub，包括jQuery，PHP，Ruby等等。

2. 集中式vs分布式版本控制系统：
    - 集中式版本控制系统：版本库是集中存放在中央服务器的，而干活的时候，用的都是自己的电脑，所以要先从中央服务器取得最新的版本，然后开始干活，干完活了，再把自己的活推送给中央服务器。最大的毛病就是必须联网才能工作，如果在局域网内还好，带宽够大，速度够快，可如果在互联网上，遇到网速慢的话，可能提交一个10M的文件就需要5分钟，这还不得把人给憋死啊。
    - 分布式版本控制系统【不必联网；强大的分支管理】：
        - 根本没有“中央服务器”，每个人的电脑上都是一个完整的版本库，这样，你工作的时候，就不需要联网了，因为版本库就在你自己的电脑上。
            - 分布式版本控制系统通常也有一台充当“中央服务器”的电脑，但这个服务器的作用仅仅是用来方便“交换”大家的修改，没有它大家也一样干活，只是交换修改不方便而已。
        - 和集中式版本控制系统相比，分布式版本控制系统的安全性要高很多，因为每个人电脑里都有完整的版本库，某一个人的电脑坏掉了不要紧，随便从其他人那里复制一个就可以了。而集中式版本控制系统的中央服务器要是出了问题，所有人都没法干活了。

3. Mac安装git：直接从AppStore安装Xcode，Xcode集成了Git，不过默认没有安装，你需要运行Xcode，选择菜单“Xcode”->“Preferences”，在弹出窗口中找到“Downloads”，选择“Command Line Tools”，点“Install”就可以完成安装了。Xcode是Apple官方IDE，功能非常强大，是开发Mac和iOS App的必选装备，而且是免费的！

4. 版本库又名仓库，英文名repository，你可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

5. 所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。

6. Git命令必须在Git仓库目录内执行（git init除外），在仓库目录外执行是没有意义的。
    - 初始化一个Git仓库，使用git init命令。
    - 添加文件到Git仓库，分两步：
        1. 使用命令git add <file>，注意，可反复多次使用，添加多个文件,实际上就是把工作区的文件修改添加到暂存区；
        2. 使用命令git commit -m <message>，完成，实际上就是把暂存区stage的所有内容提交到当前分支。(A commit is a specific snapshot of your working directory at a particular time.)
    - Amend latest commit (changing commit message or add forgotten files):
        - git add [forgotten-file]
        - git commit --amend
        ! Please note that this new amended commit will replace the previous commit.
    - Revert a file to its state at the time of the most recent commit:
        - git checkout -- [file]
        This command is useful if you would like to actually undo your work. Let’s say that you have modified a certain file since committing previously, but you would like your file back to how it was before your modifications.
    - 要随时掌握工作区的状态，使用git status命令。
    - 如果git status告诉你有文件被修改过，用git diff可以查看修改内容。
    - HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
    - 穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
    - 要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。
    - 丢弃某文件在工作区的修改，使用git checkout -- filename (git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。);
    - 丢弃某文件在暂存区的修改，先用git reset HEAD filename将暂存区修改移回到工作区，再使用git checkout -- filename丢弃
    - 撤销某次本地版本库的提交，直接用git reset --hard commit_id回退版本。如果已经git push到了远程库就不可了。
    - 命令git rm用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

7. 每当你觉得文件修改到一定程度的时候，就可以“保存一个快照”，这个快照在Git中被称为commit。一旦你把文件改乱了，或者误删了文件，还可以从最近的一个commit恢复，然后继续工作，而不是把几个月的工作成果全部丢失。每提交一个新版本，实际上Git就会把它们自动串成一条时间线。

8. 为什么Git比其他版本控制系统设计得优秀，因为Git跟踪并管理的是修改，而非文件。每次修改，如果不用git add到暂存区，那就不会加入到commit中。

9. 远程仓库
    - GitHub提供Git仓库托管服务的，所以，只要注册一个GitHub账号，就可以免费获得Git远程仓库。
    - 本地Git仓库和GitHub仓库之间的传输是通过SSH加密的。
    - GitHub允许你添加多个Key。假定你有若干电脑，你只要把每台电脑的Key都添加到GitHub，就可以在每台电脑上往GitHub推送了。
    - 在GitHub上免费托管的Git仓库，任何人都可以看到喔（但只有你自己才能改）。所以，不要把敏感信息放进去。
    - 要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git(like git remote add origin git@github.com:michaelliao/learn-git.git;实际上，Git支持多种协议，默认的git://使用ssh，但也可以使用https等其他协议，但ssh协议速度最快。), 关联一个远程库时必须给远程库指定一个名字，origin是默认习惯命名；
    - 关联后，使用命令git push -u origin master第一次推送master分支的所有内容。此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；
    - 如果添加的时候地址写错了，或者就是想删除远程库，可以用git remote rm <name>命令。使用前，建议先用git remote -v查看远程库信息;
    - 要克隆一个仓库，首先必须知道仓库的地址，然后使用git clone命令克隆;
    - git fetch [remote-name]: This is analogous to downloading the commits. It does not incorporate them into your own code.
        - Fetching the changes will only update your local copy of the remote code but not merge the changes into your own code.
        - For a more particular example, let’s say that your partner creates a new branch on the remote called fixing-ai-heuristics. You can view that branch’s commits with the following steps:
            $ git fetch origin
            $ git branch review-ai-fix origin/fixing-ai-heuristics
            $ git checkout review-ai-fix
            - The second command creates a new branch called review-ai-fix that tracks the fixing-ai-heuristics branch on the origin remote.
    - git pull [remote-name] [remote-branch-name]: This is equivalent to a fetch + merge. Not only will pull fetch the most recent changes, it will also merge the changes into your HEAD branch.
    

10. 分支管理【branch】
    - 每次提交，Git都把它们串成一条时间线，这条时间线就是一个分支。截止到目前，只有一条时间线，在Git里，这个分支叫主分支，即master分支。HEAD严格来说不是指向提交，而是指向master，master才是指向提交的，所以，HEAD指向的就是当前分支。一开始的时候，master分支是一条线，Git用master指向最新的提交，再用HEAD指向master，就能确定当前分支，以及当前分支的提交点。每次提交，master分支都会向前移动一步，这样，随着你不断提交，master分支的线也越来越长。
    - git checkout命令加上-b参数表示创建并切换分支。切换分支使用git checkout <branch>，而前面讲过的撤销修改则是git checkout -- <file>，同一个命令，有两种作用，确实有点令人迷惑。
    - 实际上，切换分支这个动作，用switch更科学。因此，最新版本的Git提供了新的git switch命令来切换分支。创建并切换到新的dev分支，可以使用git switch -c dev。直接切换到已有的master分支，可以使用：git switch master；
    - 查看分支：git branch；
    - 创建分支：git branch <name>；
    - 切换分支：git checkout <name>或者git switch <name>；
    - 创建+切换分支：git checkout -b <name>或者git switch -c <name>；
    - 合并某分支到当前分支：git merge <name>；
    - 删除分支：git branch -d <name>；
    - 因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在master分支上工作效果是一样的，但过程更安全。
    - 当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。
    - 用git log --graph命令可以看到分支合并图(git log --graph --pretty=oneline --abbrev-commit更好看)。
    - 分支策略
        - 首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
        - 那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本
        - 你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。
    - 合并分支时，加上--no-ff参数就可以用普通模式合并(git merge --no-ff -m "comment" dev)，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。
    - Bug分支
        - 软件开发中，bug就像家常便饭一样。有了bug就需要修复，在Git中，由于分支是如此的强大，所以，每个bug都可以通过一个新的临时分支来修复，修复后，合并分支，然后将临时分支删除。
        - Git还提供了一个stash功能，可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作。
        - 修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；
        - 当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场(还可以用git stash list看一下stash的情况，因为可能有多次stash，需要选一个要返回的WIP状态)；
        - 在master分支上修复的bug，想要合并到当前dev分支，可以用git cherry-pick <commit>命令，把bug提交的修改“复制”到当前分支，避免重复劳动。
    - Feature分支
        - 开发一个新feature，最好新建一个分支；
        - 如果要丢弃一个没有被合并过的分支，可以通过git branch -D/-d <name>强行删除。
    - 多人协作
        - 查看远程库信息，使用git remote -v；
        - 本地新建的分支如果不推送到远程，对其他人就是不可见的；
        - 推送分支：分支完全可以在本地自己藏着玩，是否推送，视你的心情而定！
            - master分支是主分支，因此要时刻与远程同步；
            - dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
            - bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；
            - feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。
        - 从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；
        - 在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
        - 建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
        - 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
    - Rebase
        - rebase操作可以把本地未push的分叉提交历史整理成直线;
        - rebase操作的特点：把分叉的提交历史“整理”成一条直线，看上去更直观。缺点是本地的分叉提交已经被修改过了；
        - rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。

11. 标签管理【tag】
    - 发布一个版本时，我们通常先在版本库中打一个标签（tag），这样，就唯一确定了打标签时刻的版本。标签也是版本库的一个快照。
    - Git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针（跟分支很像对不对？但是分支可以移动，标签不能移动），所以，创建和删除标签都是瞬间完成的。
    - Git有commit，为什么还要引入tag？因为tag就是一个让人容易记住的有意义的名字（unlike commit号是6a5819e...），它跟某个commit绑在一起，方便切换到某个历史快照。
    - 注意，使用git tag看现有标签时，标签不是按时间顺序列出，而是按字母排序的。
    - 注意：标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。
    - 命令git tag <tagname> <commit id, Default=HEAD> 用于新建一个标签；
    - 命令git tag -a <tagname> -m "blablabla..." <commit id, Default=HEAD>可以指定标签信息；
    - 命令git tag可以查看所有标签；
    - git show <tagname>可以查看某标签信息，包含commit id，tagger， date等等；
    - 命令git push origin <tagname>可以推送一个本地标签；
    - 命令git push origin --tags可以推送全部未推送过的本地标签；
    - 命令git tag -d <tagname>可以删除一个本地标签；
    - 命令git push origin :refs/tags/<tagname>可以删除一个远程标签。

12. Github
    - 在GitHub上，可以任意Fork开源仓库；
    - 自己拥有Fork后的仓库的读写权限；
    - 可以推送pull request给官方仓库来贡献代码。

13. 自定义Git
    - 忽略某些文件时，需要编写.gitignore；
        - .gitignore文件本身要放到版本库里，并且可以对.gitignore做版本管理！
        - 把指定文件排除在.gitignore规则外的写法就是!+文件名，所以，只需把例外文件添加进去即可（like !App.class）。
        - 哪怕.gitignore里限制不追踪某个文件，也可以用git add -f强制添加进去(like git add -f App.class)。
        - 需要找出来到底哪个规则写错了，可以用git check-ignore命令检查（like  git check-ignore -v App.class）
    - 给Git配置好别名，就可以输入命令时偷个懒。我们鼓励偷懒。(like git config --global alias.ci commit)

14. 搭建Git服务器
    - 远程仓库实际上和本地仓库没啥不同，纯粹为了7x24小时开机并交换大家的修改。
    - GitHub就是一个免费托管开源代码的远程仓库。但是对于某些视源代码如生命的商业公司来说，既不想公开源代码，又舍不得给GitHub交保护费，那就只能自己搭建一台Git服务器作为私有仓库使用。GitHub就是一个免费托管开源代码的远程仓库。但是对于某些视源代码如生命的商业公司来说，既不想公开源代码，又舍不得给GitHub交保护费，那就只能自己搭建一台Git服务器作为私有仓库使用。
    - 搭建Git服务器需要准备一台运行Linux的机器，强烈推荐用Ubuntu或Debian，这样，通过几条简单的apt命令就可以完成安装。
    - 搭建Git服务器非常简单，通常10分钟即可完成，详见：https://www.liaoxuefeng.com/wiki/896043488029600/899998870925664.

15. 使用SourceTree
    - 当我们对Git的提交、分支已经非常熟悉，可以熟练使用命令操作Git后，再使用GUI工具，就可以更高效。
    - 使用SourceTree可以以图形界面操作Git，省去了敲命令的过程，对于常用的提交、分支、推送等操作来说非常方便。
    - SourceTree使用Git命令执行操作，出错时，仍然需要阅读Git命令返回的错误信息。
'''
