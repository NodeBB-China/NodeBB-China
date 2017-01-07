> 服务器选用 64 位 CentOS，因为 MongoDB 现在只有64位版本
> 基本概念不作任何解释，本教程适合有建站基础的朋友

# NodeBB安装及部署

## MongoDB篇

### 关闭 SELinux

配置文件在/etc/sysconfig/selinux

```
SELINUX=disabled
```

### 配置 MongoDB 的官方 Yum 源

创建文件

```
touch /etc/yum.repos.d/mongodb-org-3.2.repo
```

文件内容为：

```
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
```

### 安装最新的 MongoDB

```
yum install mongodb-org
```

> 如果您是国内服务器，那么这样安装 MongoDB 会很慢，可以将repo里面的链接换成阿里云的镜像，
> 
> `baseurl=http://mirrors.aliyun.com/mongodb/yum/redhat/6/mongodb-org/stable/x86_64/`

### 关闭巨型页

安装完成后，为了消除 MongoDB 的性能警告，需要关闭 Linux 巨型页：

```
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

### 启动 MongoDB

使用以下命令启动 MongoDB

```
service mongod start
```

> 参考资料：https://docs.mongodb.org/manual/tutorial/install-mongodb-on-red-hat/#install-mongodb-community-edition

## Node.js 篇

这个不详细讲了，[下载LTS版本](https://nodejs.org/en/download/)（为了安全稳定）的**二进制包**即可（无需编译），解压之后将超长目录重命名为 `node` 并整个移动到 `/usr/local/` 目录下。

在/etc/profile里追加一行并更新环境变量*（Linux 基础知识不作解释）*：

```
echo export PATH=$PATH:/usr/local/node/bin >> /etc/profile
source /etc/profile
```

## 安装 NodeBB

**提前切换成root用户，免得麻烦。**

**不要直接下载 Github 上发布的 release 压缩包**，那里面没有 `.git/config` 配置文件，而在安装过程中需要读取配置文件的值。正确的做法是使用 Git 从 GitHub 上克隆源代码。

### 安装 Git

yum安装 Git 或者[编译安装最新的Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 下载 NodeBB

切换到/var/目录，克隆源代码：

`git clone -b v1.x.x https://github.com/NodeBB/NodeBB nodebb`

> 注意： `v1.x.x` 是最新的稳定版分支的名字，不要随意改成数字！

### 安装 NodeBB 的运行依赖

首先装好依赖包：

```
cd nodebb
npm install
```

### 新建数据库

使用以下命令进入 MongoDB 的命令行管理界面：

```
mongo
```
新建数据库：

```
use nodebb # 新建数据库，名叫 nodebb
```

### 添加用户角色：

```
db.createUser( { user: "nodebb", pwd: "<Enter in a secure password>", roles: [ "readWrite" ] } )
```
> NodeBB 需要 MongoDB 版本至少为 2.6

### 打开 MongoDB 权限认证

打开 `/etc/mongod.conf`，找到 `security:` 这一行，取消注释并改为：
```
security:
   authorization: enabled
```
### 重启 MongodB

```
service mongod restart
```
> 参考资料：
> 
> https://docs.nodebb.org/en/latest/configuring/databases/mongo.html
> 
> https://docs.mongodb.org/manual/administration/configuration/#security-considerations

