# 使用centos7安装nodebb
## 教程改编自官方文档，官方文档地址：https://docs.nodebb.org/en/latest/installing/os/centos.html
## 一、安装
### 首先更新下centos
```
yum -y update
yum -y install epel-release  (centos6不用运行这条命令)
```
### 然后安装基础软件redis,npm等
```
yum -y groupinstall "Development Tools"
yum -y install git redis ImageMagick npm
```
### 现在使用nvm进行安装nodejs
```
curl https://raw.githubusercontent.com/creationix/nvm/v0.13.1/install.sh | bash
source ~/.bash_profile
export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node
export NVM_IOJS_ORG_MIRROR=http://npm.taobao.org/mirrors/iojs
nvm list-remote
nvm install v6.0.0
```
### 使用cnpm代替npm
```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```
### 启动redis并设置开机自启
```
systemctl start redis
systemctl enable redis
```
### 从github上下载nodebb安装文件
```
cd /path/to/nodebb/install/location (可不运行，直接下载至根目录)
git clone -b v1.x.x https://github.com/NodeBB/NodeBB nodebb
```
### 进行安装nodebb
```
cd nodebb
cnpm install
```
一般几分钟就搞定了
### 进行初始化设置
```
./nodebb setup
```
一路向下就ok了，记得将数据库改为redis，默认设置是mongo，然后运行'./nodebb start'，ok，访问你的网址:4567，看是否成功了。
## 二、nginx设置
### 上一步我们安装好了nodebb，但是需要通过4567端口访问，现在我们设置一下，通过域名访问网站。
### 首先安装nginx
```
yum install nginx
```
### 设置nginx规则
```
cd /etc/nginx/conf.d
nano example.conf
```
规则如下（www重定向至no-www，如果不需要，可以自己修改）
```
server {
    listen       80;
    server_name  www.example.com;
    return       301 http://example.com$request_uri;
}

server {
    listen 80;

    server_name example.com;

    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;

        proxy_pass http://127.0.0.1:4567/;
        proxy_redirect off;

        # Socket.IO Support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```
保存，退出<br>
启动nginx
```
service nginx restart
```
如果出现如下错误
```
nginx: [emerg] could not build server_names_hash, you should increase server_names_hash_bucket_size: 32
nginx: configuration file /etc/nginx/nginx.conf test failed
```
修改nginx.conf，在http{}添加<br>
```
server_names_hash_bucket_size  64;
```
保存，退出，启动nginx
