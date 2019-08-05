- [前言](#%e5%89%8d%e8%a8%80)
- [1.环境](#1%e7%8e%af%e5%a2%83)
    - [1.1.在线安装](#11%e5%9c%a8%e7%ba%bf%e5%ae%89%e8%a3%85)
        - [1.1.2.端口放行](#112%e7%ab%af%e5%8f%a3%e6%94%be%e8%a1%8c)
        - [1.1.3.验证安装](#113%e9%aa%8c%e8%af%81%e5%ae%89%e8%a3%85)
    - [1.2.扩展说明](#12%e6%89%a9%e5%b1%95%e8%af%b4%e6%98%8e)
        - [1.2.1.编译参数](#121%e7%bc%96%e8%af%91%e5%8f%82%e6%95%b0)
        - [1.2.2.安装目录](#122%e5%ae%89%e8%a3%85%e7%9b%ae%e5%bd%95)
        - [1.2.3.默认配置](#123%e9%bb%98%e8%ae%a4%e9%85%8d%e7%bd%ae)
    - [1.2.编译安装](#12%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85)
        - [1.2.1.安装编译环境](#121%e5%ae%89%e8%a3%85%e7%bc%96%e8%af%91%e7%8e%af%e5%a2%83)
        - [1.2.2.编译安装Lua模块](#122%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85lua%e6%a8%a1%e5%9d%97)
        - [1.2.3.编译安装Nginx](#123%e7%bc%96%e8%af%91%e5%ae%89%e8%a3%85nginx)
- [附录](#%e9%99%84%e5%bd%95)
    - [依赖](#%e4%be%9d%e8%b5%96)

## 前言

官方网站：<https://nginx.org/>
> Github：<https://github.com/nginx/nginx>

**Nginx书籍**：

> 1. [Nginx Cookbook 中文版](https://huliuqing.gitbooks.io/complete-nginx-cookbook-zh/content/) <https://huliuqing.gitbooks.io/complete-nginx-cookbook-zh/content/>
> 2. [Nginx官方中文文档](https://docshome.gitbooks.io/nginx-docs/content/) <https://docshome.gitbooks.io/nginx-docs/content/>
> 3. [Nginx入门教程](https://xuexb.github.io/learn-nginx/) <https://xuexb.github.io/learn-nginx/>
> 4. [淘宝Nginx文档](http://tengine.taobao.org/book/) <http://tengine.taobao.org/book/>

## 1.环境

对于项目里面**只是使用代理等常用功能**，**在线安装**即可，如需**制定化模块**，则推荐**编译安装**

### 1.1.在线安装

在线安装比较简单，参考官方文档即可：<https://nginx.org/en/linux_packages.html>
> PS：线上选`stable`的就行了，记得把`$releasever`改成你的版本号，eg：`7`

![1.yum.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190803220053666-3527523.png)

安装图示：

![1.在线安装.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804084506172-712926052.png)

#### 1.1.2.端口放行

放行80端口：`firewall-cmd --zone=public --add-port=80/tcp --permanent`
> PS：规则生效：`firewall-cmd --reload`

![1.防火墙.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121200824-1113214603.png)

#### 1.1.3.验证安装

![1.ok.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190804121644729-360088761.png)

---

### 1.2.扩展说明

#### 1.2.1.编译参数

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

#### 1.2.2.安装目录

在线安装的包都可以通过：`rpm -ql xxx`查看安装到哪些目录

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

#### 1.2.3.默认配置

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

### 1.2.编译安装

#### 1.2.1.安装编译环境

一步到位：`yum install gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y`

简单拆分解析一下：

1. Nginx使用`C/C++`编写的，安装一下依赖：`yum install gcc-c++ -y`
2. Nginx需要使用PCRE来进行正则解析：`yum install pcre pcre-devel -y`
3. 现在服务器和浏览器一般都是使用gzip：`yum install -y zlib zlib-devel -y`
4. 让Nginx支持https：`yum install openssl openssl-devel -y`

下载Nginx：`curl -o nginx.1.17.2.tar.gz https://nginx.org/download/nginx-1.17.2.tar.gz`
> PS：服务器推荐使用稳定版本，开发用最新无碍

![2.尝鲜.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190803214948142-1222832177.png)

![2.下载源文件.png](https://img2018.cnblogs.com/blog/1127869/201908/1127869-20190803214736774-950778757.png)

#### 1.2.2.编译安装Lua模块

主要就3步走：

1. 安装**Lua即时编译器**：`LuaJIT`
    - 目前最新：<http://luajit.org/download/LuaJIT-2.0.5.tar.gz>
2. 安装Nginx模块：`ngx_devel_kit` and `lua-nginx-module`
    1. ngx_devel_kit：<https://github.com/simplresty/ngx_devel_kit/archive/v0.3.1.tar.gz>
    2. lua-nginx-module：<https://github.com/openresty/lua-nginx-module/archive/v0.10.15.tar.gz>
3. 重新编译Nginx：复制在线安装的**编译参数**（`nginx -V`）然后**添加两个参数**
    1. `--add-module=/etc/nginx/modules/ngx_devel_kit-0.3.1`
    2. `--add-module=/etc/nginx/modules/lua-nginx-module-0.10.15`

完整参数附录：

```shell
./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie' --add-module=/etc/nginx/modules/ngx_devel_kit-0.3.1 --add-module=/etc/nginx/modules/lua-nginx-module-0.10.15
```

#### 1.2.3.编译安装Nginx

todo

---

## 附录

### 依赖

```shell
[root@localhost ~]# yum install gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel -y

```
