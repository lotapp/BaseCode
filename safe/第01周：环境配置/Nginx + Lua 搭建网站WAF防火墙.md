- [前言](#%e5%89%8d%e8%a8%80)
- [1.在线安装](#1%e5%9c%a8%e7%ba%bf%e5%ae%89%e8%a3%85)
    - [1.1.修改yum源地址](#11%e4%bf%ae%e6%94%b9yum%e6%ba%90%e5%9c%b0%e5%9d%80)
    - [1.2.在线安装Nginx](#12%e5%9c%a8%e7%ba%bf%e5%ae%89%e8%a3%85nginx)
    - [1.3.端口放行](#13%e7%ab%af%e5%8f%a3%e6%94%be%e8%a1%8c)
    - [1.4.验证安装](#14%e9%aa%8c%e8%af%81%e5%ae%89%e8%a3%85)
- [2.知识拓展](#2%e7%9f%a5%e8%af%86%e6%8b%93%e5%b1%95)
    - [2.1.编译参数](#21%e7%bc%96%e8%af%91%e5%8f%82%e6%95%b0)
    - [2.2.安装目录](#22%e5%ae%89%e8%a3%85%e7%9b%ae%e5%bd%95)
    - [2.3.默认配置](#23%e9%bb%98%e8%ae%a4%e9%85%8d%e7%bd%ae)
    - [2.4.systemctl配置](#24systemctl%e9%85%8d%e7%bd%ae)
- [3.编译安装](#3%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85)
    - [3.1.安装编译环境](#31%e5%ae%89%e8%a3%85%e7%bc%96%e8%af%91%e7%8e%af%e5%a2%83)
    - [3.2.Nginx编译安装](#32nginx%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85)
        - [3.2.1.下载解压](#321%e4%b8%8b%e8%bd%bd%e8%a7%a3%e5%8e%8b)
        - [3.2.2.配置编译参数](#322%e9%85%8d%e7%bd%ae%e7%bc%96%e8%af%91%e5%8f%82%e6%95%b0)
        - [3.2.3.进行编译安装](#323%e8%bf%9b%e8%a1%8c%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85)
        - [3.2.4.配置systemctl](#324%e9%85%8d%e7%bd%aesystemctl)
        - [3.2.5.端口放行](#325%e7%ab%af%e5%8f%a3%e6%94%be%e8%a1%8c)
        - [3.2.6.验证](#326%e9%aa%8c%e8%af%81)
    - [3.3.编译安装Lua模块](#33%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85lua%e6%a8%a1%e5%9d%97)
        - [大体思路](#%e5%a4%a7%e4%bd%93%e6%80%9d%e8%b7%af)
        - [3.3.1.编译安装luajit并导入环境变量](#331%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85luajit%e5%b9%b6%e5%af%bc%e5%85%a5%e7%8e%af%e5%a2%83%e5%8f%98%e9%87%8f)
        - [3.3.2.配置nginx的编译参数](#332%e9%85%8d%e7%bd%aenginx%e7%9a%84%e7%bc%96%e8%af%91%e5%8f%82%e6%95%b0)
        - [3.3.3.重新编译安装nginx](#333%e9%87%8d%e6%96%b0%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85nginx)
        - [3.3.4.共享lua动态库](#334%e5%85%b1%e4%ba%ablua%e5%8a%a8%e6%80%81%e5%ba%93)
        - [3.3.5.验证Lua模块](#335%e9%aa%8c%e8%af%81lua%e6%a8%a1%e5%9d%97)
- [4.Nginx+Lua搭建WAF防火墙](#4nginxlua%e6%90%ad%e5%bb%bawaf%e9%98%b2%e7%81%ab%e5%a2%99)
    - [4.1.环境](#41%e7%8e%af%e5%a2%83)
    - [4.2.配置](#42%e9%85%8d%e7%bd%ae)
    - [4.3.生效](#43%e7%94%9f%e6%95%88)
    - [4.4.简单验证](#44%e7%ae%80%e5%8d%95%e9%aa%8c%e8%af%81)
    - [4.5.CC验证](#45cc%e9%aa%8c%e8%af%81)
    - [扩展：隐藏Nginx版本信息](#%e6%89%a9%e5%b1%95%e9%9a%90%e8%97%8fnginx%e7%89%88%e6%9c%ac%e4%bf%a1%e6%81%af)

## 前言

对于项目里面**只是使用代理等常用功能**，**在线安装**即可，如需**制定化模块**，则推荐**编译安装**
> PS：本文不仅仅包含Nginx相关的知识点，还包含了逆天学习方法（对待新事物的处理）

官方网站：<https://nginx.org/>
> Github：<https://github.com/nginx/nginx>

**Nginx书籍**：

> 1. [Nginx Cookbook 中文版](https://huliuqing.gitbooks.io/complete-nginx-cookbook-zh/content/) <https://huliuqing.gitbooks.io/complete-nginx-cookbook-zh/content/>
> 2. [Nginx官方中文文档](https://docshome.gitbooks.io/nginx-docs/content/) <https://docshome.gitbooks.io/nginx-docs/content/>
> 3. [Nginx入门教程](https://xuexb.github.io/learn-nginx/) <https://xuexb.github.io/learn-nginx/>
> 4. [淘宝Nginx文档](http://tengine.taobao.org/book/) <http://tengine.taobao.org/book/>

## 1.在线安装

### 1.1.修改yum源地址

清华源：<https://mirrors.tuna.tsinghua.edu.cn/help/centos/>

![清华源](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805113524992-767949312.png)

更新软件包缓存：`yum makecache`

![更新缓存](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805113629902-726330007.png)

### 1.2.在线安装Nginx

在线安装比较简单，参考官方文档即可：<https://nginx.org/en/linux_packages.html>
> PS：线上选`stable`的就行了，记得把`$releasever`改成你的版本号，eg：`7`

![1.yum.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190803220053666-3527523.png)

安装图示：

![1.在线安装.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804084506172-712926052.png)

```shell
# 创建nginx的yum
vi /etc/yum.repos.d/nginx.repo

# 内容如下：
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key

# 在线安装
yum install nginx -y
```

### 1.3.端口放行

放行80端口：`firewall-cmd --zone=public --add-port=80/tcp --permanent`
> PS：规则生效：`firewall-cmd --reload`

![1.防火墙.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121200824-1113214603.png)

### 1.4.验证安装

![1.ok.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121644729-360088761.png)

---

## 2.知识拓展

### 2.1.编译参数

离线安装可以参考在线安装的配置：**`nginx -V`：编译参数**（`nginx -v`：查看版本）

![1.nginx编译参数.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804084656595-233777162.png)

<details>
<summary>编译参数详解（点我展开）</summary>

```shell
# 1.编译选项
## Nginx的安装主目录
--prefix=/etc/nginx \
## Nginx的执行文件路径
--sbin-path=/usr/sbin/nginx \
## Nginx的模块目录
--modules-path=/usr/lib64/nginx/modules \
## Nginx的配置文件路径
--conf-path=/etc/nginx/nginx.conf \
## Nginx的错误日志路径
--error-log-path=/var/log/nginx/error.log \
## Nginx的访问日志
--http-log-path=/var/log/nginx/access.log \
## Nginx的pid文件路径
--pid-path=/var/run/nginx.pid \
## Nginx的lock路径
--lock-path=/var/run/nginx.lock \

# 2.编译选项（执行对应模块时Nginx缓存文件的存放地址）
--http-client-body-temp-path=/var/cache/nginx/client_temp \
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \

# 3.设置Nginx权限组（虽然root权限安装，但可以指定nginx的运行权限）
--user=nginx \
--group=nginx \

# 4.优化
## 启用gzip压缩模块（常用）
--with-http_gzip_static_module \
--with-http_gunzip_module \
# 文件使用aio异步操作
--with-file-aio \

## C系列优化
--with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' \
## 设置附加的参数，链接系统库
--with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' \
# HTTP内容替换
--with-http_sub_module \

# 其他优化选项 or 模块
--with-compat \
--with-threads \
--with-http_addition_module \
--with-http_auth_request_module \
--with-http_dav_module \
--with-http_flv_module \
--with-http_mp4_module \
--with-http_random_index_module \
--with-http_realip_module \
--with-http_secure_link_module \
--with-http_slice_module \
--with-http_ssl_module \
--with-http_stub_status_module \

--with-http_v2_module \
--with-mail \
--with-mail_ssl_module \
--with-stream \
--with-stream_realip_module \
--with-stream_ssl_module \
--with-stream_ssl_preread_module \
```

</details>

---

### 2.2.安装目录

**在线安装的包**都可以通过：`rpm -ql xxx`查看安装到哪些目录

<details>
<summary>安装目录详解（点我展开）</summary>

```shell
[root@localhost dnt]# rpm -ql nginx

# Nginx使用用logrotate服务对日志进行切割的配置文件（eg：按天切割）
/etc/logrotate.d/nginx

# Nginx的核心目录
/etc/nginx
# 主要配置文件，Nginx启动的时候会读取
/etc/nginx/nginx.conf
/etc/nginx/conf.d
# nginx.conf没变更久读default.conf（默认Server加载的文件）
/etc/nginx/conf.d/default.conf

# Nginx对Python的wsgi配置
/etc/nginx/uwsgi_params
# fastcgi配置
/etc/nginx/fastcgi_params
# scgi配置
/etc/nginx/scgi_params

# Nginx缓存目录
/var/cache/nginx

# Nginx日志目录
/var/log/nginx

# Nginx默认网站存放的路径
/usr/share/nginx/html
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html

# 设置http的Content-Type与扩展名对应关系的配置文件
/etc/nginx/mime.types

# Nginx模块所在目录
/usr/lib64/nginx/modules
/etc/nginx/modules

# 二进制执行文件
/usr/sbin/nginx
/usr/sbin/nginx-debug

# 编码转换的映射文件
/etc/nginx/koi-utf
/etc/nginx/koi-win
/etc/nginx/win-utf

# 配置CentOS守护进程对Nginx的管理方式
/usr/lib/systemd/system/nginx-debug.service
/usr/lib/systemd/system/nginx.service
/etc/sysconfig/nginx
/etc/sysconfig/nginx-debug

# Nginx的文档
/usr/share/doc/nginx-1.16.0
/usr/share/doc/nginx-1.16.0/COPYRIGHT
/usr/share/man/man8/nginx.8.gz

# Nginx检测更新命令
/usr/libexec/initscripts/legacy-actions/nginx
/usr/libexec/initscripts/legacy-actions/nginx/check-reload
/usr/libexec/initscripts/legacy-actions/nginx/upgrade
```

</details>

---

### 2.3.默认配置

配置语法检查：`nginx -t -c /etc/nginx/nginx.conf`
> PS：不重启的方式加载配置：`Nginx -s reload -c /etc/nginx/nginx.conf`

全局以及服务级别的配置：

| 参数                       | 说明                 |
| -------------------------- | -------------------- |
| `user`                       | 使用用户来运行nginx  |
| `worker_processes`           | 工作进程数           |
| `error_log`                  | nginx的错误日记      |
| pid                        | nginx启动时的pid     |

events相关配置：

| 参数                       | 说明                 |
| -------------------------- | -------------------- |
| `worker_connections` | 每个进程的最大连接数 |
| `use`                | 工作进程数           |

常用中间件配置：

```shell
http {
    ......
    server {
        listen          80;             # 端口号
        server_name     localhost;      # 域名
        # 路径访问控制（默认访问路径，eg：/ ==> 根目录）
        location / {
            root /usr/share/nginx/html; # 网站根目录
            index index.html index.htm index.py; # 首页配置
        }

        error_page 500 502 503 504 /50x.html; # 错误页面（可以自定义添404页面，error_page 404 /404.html;...）
        # 访问xxx/50x.html的时候去指定目录找
        location = /50x.html {
            root /usr/share/nginx/html; # 错误页面所在路径
        }
    }
    # 一个server配置一个虚拟 or 独立的站点（通过listen和server_name来区别多个server）
    server {
        ......
    }
}
```

---

### 2.4.systemctl配置

nginx:（等会编译安装的时候可以参考）

```shell
[root@localhost dnt]# cat /usr/lib/systemd/system/nginx.service
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/var/run/nginx.pid
ExecStart=/usr/sbin/nginx -c /etc/nginx/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```

nginx-debug：

```shell
[root@localhost dnt]# cat /usr/lib/systemd/system/nginx-debug.service
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/var/run/nginx.pid
ExecStart=/usr/sbin/nginx-debug -c /etc/nginx/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```

---

## 3.编译安装

### 3.1.安装编译环境

一步到位：`yum install gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y`

![一步到位](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805113900096-107108424.png)

简单拆分解析一下：

1. Nginx使用`C/C++`编写的，安装一下依赖：`yum install gcc-c++ -y`
2. Nginx需要使用PCRE来进行正则解析：`yum install pcre pcre-devel -y`
3. 现在服务器和浏览器一般都是使用gzip：`yum install -y zlib zlib-devel -y`
4. 让Nginx支持https：`yum install openssl openssl-devel -y`

### 3.2.Nginx编译安装

#### 3.2.1.下载解压

先编译安装一下，后面说lua模块的时候再重新编译下就行了

下载：`curl -o nginx.tar.gz http://nginx.org/download/nginx-1.16.0.tar.gz`

解压：`tar -zxvf nginx.tar.gz`

#### 3.2.2.配置编译参数

参考前面说的在线版Nginx来设置编译参数的配置：
> PS：`nginx -V`

切换到nginx的解压目录：`cd nginx-1.16.0` 然后执行下面命令
> PS：root权限编译哦~

```shell
./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie'
```

#### 3.2.3.进行编译安装

接着编译安装：`make && make install`
> PS：提速：`make -j 4 && make install`

![编译安装nginx](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805125816846-197595638.png)

#### 3.2.4.配置systemctl

利用systemctl添加自定义系统服务

![systemctl](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805133337562-1682109342.png)

```shell
# vi /usr/lib/systemd/system/nginx.service
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network-online.target remote-fs.target nss-lookup.target
Wants=network-online.target

[Service]
Type=forking
PIDFile=/var/run/nginx.pid
ExecStart=/usr/sbin/nginx -c /etc/nginx/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target
```

PS：如果不生效可以重载下systemctl：`systemctl daemon-reload`

#### 3.2.5.端口放行

放行80端口：`firewall-cmd --zone=public --add-port=80/tcp --permanent`
> PS：规则生效：`firewall-cmd --reload`

![1.防火墙.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121200824-1113214603.png)

#### 3.2.6.验证

![ok.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121644729-360088761.png)

运行的时候如果出现**`nginx: [emerg] getpwnam("nginx") failed`**的错误可以参考我写这篇文章：<https://www.cnblogs.com/dotnetcrazy/p/11304783.html>
> PS：核心：`useradd -s /sbin/nologin -M nginx`

---

### 3.3.编译安装Lua模块

#### 大体思路

**默认是不支持Lua的**，所以需要自己编译安装下
> PS：记得安装下Lua库：`yum install lua lua-devel -y`

主要就3步走：

1. 安装**Lua即时编译器**：`LuaJIT`
    - 目前最新：<http://luajit.org/download/LuaJIT-2.0.5.tar.gz>
2. 安装Nginx模块：`ngx_devel_kit` and `lua-nginx-module`
    1. ngx_devel_kit：<https://github.com/simplresty/ngx_devel_kit/archive/v0.3.1.tar.gz>
    2. lua-nginx-module：<https://github.com/openresty/lua-nginx-module/archive/v0.10.15.tar.gz>
3. 重新编译Nginx：复制在线安装的**编译参数**（`nginx -V`）然后**添加两个参数**
    1. `--add-module=../ngx_devel_kit-0.3.1`
    2. `--add-module=../lua-nginx-module-0.10.15`

#### 3.3.1.编译安装luajit并导入环境变量

解压缩

![1.解压缩.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805194405685-441957872.png)

```shell
# 编译安装
make install PREFIX=/usr/local/LuaJIT
# 导入环境变量
export LUAJIT_LIB=/usr/local/LuaJIT/lib
export LUAJIT_INC=/usr/local/LuaJIT/include/luajit-2.0
```

![2.编译安装luajit并导入环境变量.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805124819515-571074583.png)

#### 3.3.2.配置nginx的编译参数

![配置nginx的编译参数](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805195221743-1266406775.png)

完整参数附录：

```shell
./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' --add-module=../ngx_devel_kit-0.3.1 --add-module=../lua-nginx-module-0.10.15
```

#### 3.3.3.重新编译安装nginx

编译安装：`make && make install`

![4.编译安装nginx](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805125816846-197595638.png)

#### 3.3.4.共享lua动态库

加载lua库到ld.so.conf文件
> `echo "/usr/local/LuaJIT/lib" >> /etc/ld.so.conf`

![5.加载lua库到ld.so.conf文件](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805132350465-149944837.png)

执行`ldconfig`让动态函式库加载到缓存中

![ldconfig](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805201203341-254351151.png)

#### 3.3.5.验证Lua模块

验证下Lua是否已经可用：

在nginx.config的server节点下添加：
> PS：`vi /etc/nginx/nginx.conf`

![配置](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805212709044-895580884.png)

```shell
server {
    listen       80;
    server_name  localhost;
    charset utf-8; # 默认编码为utf-8

    location / {
        root   html;
        index  index.html index.htm;
    }
    ...
    # 测试Nginx的Lua（添加这一段）
    location /hello {
        default_type 'text/plain';
        content_by_lua 'ngx.say("欢迎访问逸鹏说道公众号~")';
    }
    ...
}
```

检查配置：`nginx -t -c /etc/nginx/nginx.conf`
> PS：配置生效：`nginx -s reload -c /etc/nginx/nginx.conf`

![生效](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805212840421-622740878.png)

看看效果：

![ok](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805213724113-1853622212.png)

扩展：你可以试试获取ip哦~

```shell
# 获取客户端ip
location /myip {
    default_type 'text/plain';
    content_by_lua '
        clientIP = ngx.req.get_headers()["x_forwarded_for"]
        ngx.say("IP:",clientIP)
    ';  
}
```

---

## 4.Nginx+Lua搭建WAF防火墙

市面上比较常用一块开源项目：`ngx_lua_waf`
> <https://github.com/loveshell/ngx_lua_waf>

1. 拦截Cookie类型工具
2. 拦截异常post请求
3. 拦截CC洪水攻击
4. 拦截URL
5. 拦截arg（提交的参数）

![demo](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805221849396-1625560169.png)

### 4.1.环境

clone代码并移动到nginx的waf目录下

![git](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805220109073-1722931442.png)

简单说下里面的规则分别有啥用：

1. args里面的规则get参数进行过滤的
2. url是只在get请求url过滤的规则
3. post是只在post请求过滤的规则
4. whitelist是白名单，里面的url匹配到不做过滤
5. user-agent是对user-agent的过滤规则

### 4.2.配置

修改必要配置

![waf](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805221410142-851034378.png)

详细说明我引用一下我的上篇文章：
> 参数简单说明下：**红色字体部分需要修改**
> ![pms](https://img2018.cnblogs.com/blog/1127869/201907/1127869-20190728203735867-1500419135.png)

`nginx.config`的`http`下添加如下内容：

![lua图示](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805221643284-1265490281.png)

```lua
lua_package_path "/etc/nginx/waf/?.lua";
lua_shared_dict limit 10m;
init_by_lua_file /etc/nginx/waf/init.lua;
access_by_lua_file /etc/nginx/waf/waf.lua;
```

### 4.3.生效

配置语法检查：`nginx -t -c /etc/nginx/nginx.conf`
> PS：不重启的方式加载配置：`Nginx -s reload -c /etc/nginx/nginx.conf`

![reload](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805222413208-1113204709.png)

### 4.4.简单验证

![ok](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805220850660-1419739260.png)

PS：其实绕过很简单，看看他默认规则即可，这款WAF的强大之处在于轻量级，而且规则可以自定化
> 过滤规则在wafconf下，可根据需求自行调整，每条规则需换行,或者用|分割

举个例子：`http://192.168.0.10/hello?id=1 or 1=1`
> PS：默认规则没有这点的防护

![old](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805223005559-1683681475.png)

那么我们可以在args规则中添加比如`\sor\s+`，然后`nginx -s reload`一下就行了
> PS：如果是从post进行注入，或者cookie中转注入，那么在对应规则里面添加就行，我这边只是演示下防火墙被绕过该怎么解决~（多看看日志）

![add](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805223550273-1730613674.png)

### 4.5.CC验证

留个课后作业：**使用ab来测试下nginx+lua的waf对cc的防御效果**

提示：可以使用`ab -n 2000 -c 200 http://192.168.0.10`来简单测试
> PS：测试前curl http://192.168.0.10/hello 看看返回内容，测试后再curl看看返回内容

### 扩展：隐藏Nginx版本信息

防止被黑客进行针对性渗透，隐藏下版本信息
> PS：其他配置今天就不详细讲解了，下次讲Nginx的时候会说的

原来：

![old](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805211009687-5012491.png)

配置下：`vi /etc/nginx/nginx.conf`
> http下添加：`server_tokens off;`

![conf](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805210732696-700232340.png)

检查下语法：`nginx -t`

不重启的方式加载配置文件：`nginx -s reload`

![nginx](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805211905130-789538968.png)

现在效果：

![new](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190805212008450-425015538.png)
