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
