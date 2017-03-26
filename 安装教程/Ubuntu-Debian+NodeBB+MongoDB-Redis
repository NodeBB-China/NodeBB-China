**该文章是 PA Team 安装本社区时使用的方法**
### 1.配置环境
#### 1.1Node.js
Node.js 是由 Chrome JavaScript V8 引擎衍生出的一种高性能，高并发，易扩展的框架。
NodeBB也正是因为它，才具有了快捷，高效的特性。

* 截止目前，NodeBB 要求 Node.js 的最低版本为 v4.x
>目前，推荐使用 `nvm` 来快速安装nodejs。

##### 1.1.1 使用 NVM 来安装 Node.js LTS (推荐)
* 首先，我们现在服务器上安装 `NVM` 
```
#截止17.3.18,NVM最新版本为0.33.1
$ sudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash 
```
***可以在 [Github](https://github.com/creationix/nvm/) 中获取 NVM 最新的安装指令*** 
* 添加 NVM 到环境变量
```
$ sudo export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
```
* 使环境变量的修改生效
```
$ sudo source ~/.bashrc
```
* 检查是否成功安装
```
$ command -v nvm
```
如果没有抛出任何错误信息，那么我们继续下面的步骤吧。（如果有，请到Github中寻找解决方案。）
* 使用 NVM 安装 Node.js 的 LTS 版本  

***如果你使用的机器是国内的话，建议使用以下代码让NVM使用淘宝镜像来下载源码(腾讯云的下载速度只有可怜的1x.kb/s...)***
```
#让NVM使用淘宝源
$ sudo export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node
$ sudo export NVM_IOJS_ORG_MIRROR=http://npm.taobao.org/mirrors/iojs
```
好，我们使用下面的代码来安装LTS版本
```
#安装Node.js LTS
$ sudo nvm install --lts
```  

等待执行完成，如果使用`node -v` ，`npm -v`都能正确输出版本号的话，说明nodejs已经成功安装。
> 在国内，NPM源的速度比较慢，可以使用`sudo npm config set registry http://registry.npm.taobao.org/`来将npm更换到国内的淘宝源
----
##### 1.1.2使用源码编译安装Node.js
首先，我们要去Node.js官网获得源代码文件`https://nodejs.org`。
我们推荐使用LTS作为NodeBB的驱动环境。截止发稿，目前Node.js的LTS最新版本为6.9.5。  
你可以通过下面的Linux指令将Node.js下载到你想要的目录中。
```
$ sudo wget https://nodejs.org/dist/v6.9.5/node-v6.9.5.tar.gz #国内速度比较慢，可以使用这个链接代替：https://npm.taobao.org/mirrors/node/v{版本号}/node-v{版本号}.tar.gz
```
然后，我们需要解压这个压缩包，并且开始编译它。
```
$ sudo tar -xzf node*.tar.gz #解压
$ cd node* #进入解压后的文件夹
$ sudo ./configure #进行环境配置（检测），如果出现warning 建议使用 Oneinstack 安装Nginx 以解决环境依赖问题 （Nginx稍后会使用到）
$ sudo make #编译 （可能需要数十分钟）
$ sudo make install #安装 
#先别急，我们看看安装是否成功
$ node -v #检查是否输出的是你要安装的版本
$ npm -v #同上
```
**在国内，NPM源的速度比较慢，可以使用`sudo npm config set registry http://registry.npm.taobao.org/`来将npm更换到国内的淘宝源**

#### 1.2 数据库

* Mongodb （推荐）
Mongodb是目前流行的NoSQL数据库。它具有高性能，高可用，易扩展，富查询的特性。相比Redis ，它更能节省内存开支。  
 
   - **Ubuntu**
Mongodb 目前只给LTS版本提供安装包。例如，12.04 LTS (precise), 14.04 LTS (trusty), 16.04 LTS (xenial)。
导入公钥
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```
为Mongodb建立一个.list文件
```
#（目前最新版本是3.4，安装其他版本可以将3.4替换为其他版本。这个方法可能向上兼容到3.2。）

#如果你是Ubuntu 12.04 LTS 执行下面的代码
$ sudo echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

#如果你是Ubuntu 14.04 LTS ，请执行下面的代码
$ sudo echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

#如果你是Ubuntu 16.04 LTS 请执行下面的代码
$ sudo echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

```
  更新apt源
```
$ sudo apt-get update
```
  安装Mongodb
```
$ sudo apt-get install -y mongodb-org #安装Mongodb社区版
```
  
-----
  
  - Debian
  导入公钥
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
```
  新建一个.list文件
```
#（目前最新版本是3.4，安装其他版本可以将下面的3.4替换为其他版本。这个方法可能向上兼容到3.2。）

#如果你是 Debian 7 Wheezy，请使用执行下面的命令
$ sudo echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

#如果你是Debian 8 Jessie ,请执行下面的命令
$ sudo echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
```
  更新apt源
```
$ sudo apt-get update
```
  安装Mongodb
```
$ sudo apt-get install -y mongodb-org
```
  
*由于国内可能源不稳定，我们可以使用`http://mirrors.tuna.tsinghua.edu.cn/apt/{ubuntu或者debian}` 来代替上面的官方源*
   
   
**有关如何配置Mongodb数据库，[请点击这里](https://www.nodebb-cn.org/topic/14/nodebb安装实战-配置mongodb)**
  
  

* redis （不推荐大型社区使用）
可以参考 在CentOS中安装 的数据库配置部分
```
$ sudo apt-get install redis #安装redis
```
### 2.安装
#### 2.1 获取 NodeBB 程序
截止发稿时间，NodeBB 目前最新稳定版本为1.4.3。
首先，我们先得安装好Git（如果有，可跳过）
```
$ sudo apt-get install -y git build-essential
```
找到一个你喜欢的位置，然后使用`git`指令获取程序。
```
$ cd /home #修改为你喜欢的位置
$ sudo git clone -b v1.x.x https://github.com/NodeBB/NodeBB.git nodebb #这将在 /home 下面 新建一个名叫nodebb的文件夹并且会把程序从Github克隆到里面
```
然后，我们先把依赖安装完毕。  
```
$ cd nodebb
$ sudo npm update
$ sudo npm install --production
```
现在，我们就可以对开始程序的配置了。
```
$ sudo ./nodebb setup
```
*可以根据括号中的提示完成信息的填写，nodebb监听的默认端口是`4567`，Mongodb 监听的端口是 `27017`*  
使用`sudo ./nodebb start` 启动，享受NodeBB给你带来的快乐吧！
### 让NodeBB开机自启
方法可以参考 Ghost 的安装，不过我们还是建议你把NodeBB注册为服务。

首先，先新建一个叫做nodebb的用户和用户组并且把nodebb目录下所有文件的所有权转移给这个用户（组）。
```
$ sudo adduser --system --group nodebb
$ sudo chown -R nodebb:nodebb /{你之前填写的目录}/nodebb
```
现代化的Linux系统都使用 `systemd` 作为默认的初始化系统。让我们给 NodeBB 新建一个 systemd 单元吧。使用`vim /lib/systemd/system/nodebb.service`编辑，请将下面的内容复制进去。
```
[Unit]
Description=NodeBB forum for Node.js.
Documentation=http://nodebb.readthedocs.io/en/latest/
After=system.slice multi-user.target

[Service]
Type=simple
User=nodebb

StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=nodebb

Environment=NODE_ENV=production
WorkingDirectory=/home/nodebb
#请把上面的目录替换为你的nodebb目录
ExecStart=/usr/bin/node loader.js --no-daemon --no-silent
#请修改/usr/bin/node 为which node所打印的位置
Restart=always

[Install]
WantedBy=multi-user.target
```
好了，我们启用并且运行nodebb服务吧！
***如果前面使用`./nodebb start` 运行了nodebb的话，请先使用 `./nodebb stop`停止。***
```
$ sudo systemctl enable nodebb
$ sudo service nodebb start
$ sudo service nodebb status
```

### 3.使用Web服务器反代NodeBB
* Nginx
在这里推荐你使用 Oneinstack 安装Nginx。下面的内容是基于你使用这个安装包安装了Nginx后的。
```
$ cd ~/oneinstack #跳转到你解压oneinstack的目录
$ sudo ./vhost.sh add #配置你需要使用的域名（可以开启ssl）
$ sudo vim /usr/local/nginx/conf/vhost/domains.conf 
```

* 编辑你刚才填写的域名的配置文件。

* 在文件中，我们删除所有的 location块。并且我们需要把下面的 location 复制进你的conf文件中。

* 如果你启用了ssl，请稍后将正确的证书编辑进相应的文件（通常目录为/usr/local/nginx/conf/ssl/）
```
location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;

        proxy_pass http://127.0.0.1:4567;
        proxy_redirect off;

        # Socket.IO Support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

```
最后，我们需要使用下面的指令重载Nginx（如果报错，修改指定位置即可。）
```
$ sudo service nginx reload
```
---
下面是Apache的配置方法，如果您需要，可以点击查看。
* [Apache v2.4.x+](http://nodebb.readthedocs.io/en/latest/configuring/proxies/apache.html)
* [Apache v2.x](http://nodebb.readthedocs.io/en/latest/configuring/proxies/apache2.2.html)    

如需转载，请注明来源。
PA Team 
>参考：  
>[NodeBB-Docs](http://nodebb.readthedocs.io/en/latest/index.html)  
>[Mongodb-Docs](http://docs.mongodb.com)  
>[Oneinstack](http://oneinstack.com)
