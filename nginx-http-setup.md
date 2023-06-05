# Установка nginx + brotli + http3

Логика действий:

- Скачиваем и устанавливаем openssl+quic текущей версии.
- Скачиваем модуль nginx + brotli
- Скачиваем исходники nginx с флагом -b quic
- Скачиваем boringssl
- Устанавливаем сначала boringssl
- Затем устанавливаем nginx с конфигурацией, как у меня, с указанием путей к исходникам openssl и модулю ngx_brotli
- Устанавливаем certbot
- Настраиваем конфигурацию сервера, тестируем её, запускаем сервер
- Клонируем свою репу
- Линкуем конфиг
- Проверяем http2, http3, brotli

Вам потребуется Ubuntu сервер и доменное имя:

- [Дешевые ru сервера](https://firstbyte.ru)
- [Дешевые сервера с зарубежным ip](https://aeza.net)
- [Найти доменное имя по лучшей цене](https://ru.tld-list.com)
- [Бесплатное доменное имя на год с Github for Students](https://education.github.com/pack?sort=popularity&tag=Domains)

Заходим как root через SSH: `ssh root@123.123.123.123`
Обычно сразу кидает в папку /root

Вот в ней (/root) выполняем следующие команды...

## Зависимости

На случай, если что-то из этого не стоит на сервере:
`apt install -y git curl mercurial libpcre3 libpcre3-dev gcc make autoconf zlib1g zlib1g-dev`

## ngx_brotli

Клонируем модуль nginx brotli:

```bash
  git clone https://github.com/google/ngx_brotli.git ;
  cd ngx_brotli && git submodule update --init ;
  cd /root
```

## Openssl+Quic

```bash
git clone --depth 1 -b openssl-3.0.5+quic \
https://github.com/quictls/openssl && cd openssl && \
./config enable-tls1_3 --prefix=$PWD/build && \
make -j$(nproc) && \
make install_sw && \
cd /root
```

## Boringssl

Здесь нам нужен golang поновее:

```bash
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.11.3 2> /dev/null && \
  echo '. "$HOME/.asdf/asdf.sh"' >> ~/.bashrc && \
  source ~/.bashrc && \
  asdf plugin add golang && \
  asdf install golang latest && \
  asdf global golang latest
```

Выполняем для установки boringssl:

```bash
 apt-get update && \
    apt-get install -y gcc make g++ cmake perl libunwind-dev && \
    git clone https://boringssl.googlesource.com/boringssl && \
    mkdir boringssl/build && \
    cd boringssl/build && \
    cmake .. && \
    make && \
    cd /root
```

[Такая ошибка](bugs.chromium.org/p/boringssl/issues/detail?id=520) возникала из-за малого объема оперативной памяти

```log
[ 86%] Linking CXX static library libssl.a
[ 86%] Built target ssl
Scanning dependencies of target ssl_test
[ 86%] Building CXX object ssl/CMakeFiles/ssl_test.dir/span_test.cc.o
[ 86%] Building CXX object ssl/CMakeFiles/ssl_test.dir/ssl_test.cc.o
c++: fatal error: Killed signal terminated program cc1plus
compilation terminated.
make[2]: *** [ssl/CMakeFiles/ssl_test.dir/build.make:76: ssl/CMakeFiles/ssl_test.dir/ssl_test.cc.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:602: ssl/CMakeFiles/ssl_test.dir/all] Error 2
make: *** [Makefile:130: all] Error 2
root@devq:~/boringssl/build# yum -y install gcc-c++
-bash: yum: command not found
root@devq:~/boringssl/build# apt install yum
Reading package lists... Done
Building dependency tree
Reading state information... Done
```

## Nginx

Собираем сам nginx cо всеми модулями:

```bash
 apt-get install -y mercurial libperl-dev libpcre3-dev zlib1g-dev libxslt1-dev libgd-ocaml-dev libgeoip-dev && \
    hg clone -b quic https://hg.nginx.org/nginx-quic   && \
    hg clone http://hg.nginx.org/njs -r "0.6.2" && \
    cd nginx-quic && \
    hg update quic && \
    auto/configure `nginx -V 2>&1 | sed "s/ \-\-/ \\\ \n\t--/g" | grep "\-\-" | grep -ve opt= -e param= -e build=` \
        --prefix=/etc/nginx \
        --sbin-path=/usr/sbin/nginx \
        --with-openssl=../openssl \
        --conf-path=/etc/nginx/nginx.conf \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --with-pcre  \
        --lock-path=/var/lock/nginx.lock \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module \
        --with-http_image_filter_module=dynamic \
        --modules-path=/etc/nginx/modules \
        --with-http_v2_module \
        --with-stream=dynamic \
        --with-http_addition_module \
        --with-http_mp4_module  \
        --add-module=../ngx_brotli \
        --build=nginx-quic --with-debug  \
        --with-http_v3_module \
        --with-cc-opt="-I/src/boringssl/include" --with-ld-opt="-L/src/boringssl/build/ssl -L/src/boringssl/build/crypto" && \
    make && make install
```

## Проверяем Brotli

Делаем запросик: `curl -H 'Accept-Encoding: br' -I http://localhost`

В ответе должен присутствовать заголовок `Content-Encoding: br`


## Генерируем dhparam

```bash
  mkdir /etc/nginx/crt ; \
  openssl dhparam -out /etc/nginx/crt/dhparam.pem 4096
```

## Конфиг

Создаём http3 snippet `/etc/nginx/snippets/http3.conf`:

```conf
ssl_protocols TLSv1.2 TLSv1.3;
quic_retry on;
ssl_early_data on;
ssl_dhparam /etc/nginx/crt/dhparam.pem;
ssl_session_cache shared:SSL:5m;
ssl_session_timeout 1h;
ssl_session_tickets off;
ssl_buffer_size 4k;
proxy_request_buffering off;
add_header alt-svc 'h3=":443"; ma=86400';
add_header Strict-Transport-Security max-age=15768000;
gzip off;
```

Создаём в корне Django проекта файл nginx.conf (меняйте под себя):

```conf
server {
    listen 80;
    listen [::]:80;
    client_max_body_size 10M;
    server_name domain.com www.domain.com;
    return 301 https://domain.com$request_uri;
}

server {
    listen 443 ssl http3;
    listen [::]:443 ssl http3;
    client_max_body_size 10M;
    server_name www.domain.com;
    return 301 https://domain.com$request_uri;

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/domain.com/chain.pem;

    include snippets/http3.conf;
}

server {
    listen 443 ssl http3;
    listen [::]:443 ssl http3;
    client_max_body_size 10M;
    server_name domain.com;
    root /var/www/domain;

    location /api {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }

    location /admin {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }

    location /swagger {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }

    location /redoc {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }


    location /static/ {
        alias /var/www/domain/backend/static/;
    }

    location /media/ {
        alias /var/www/domain/backend/media/;
    }


    location / {
        alias /var/www/domain/frontend/dist/;
        try_files $uri $uri/ /index.html;
    }

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/domain.com/chain.pem;

    include snippets/http3.conf;
}
```

Проверяем, что нет ошибок в конфиге: `nginx -t`

## Настраиваем DNS записи

Нужно добавить несколько A записей на сайте вашего DNS провайдера
(вторую запись можно не ставить, если DNS провайдер не поддерживает)

| Type | Host       | Answer          |
|------|------------|-----------------|
|  A   | site.com   | 123.123.123.123 |
|  A   | *.site.com | 123.123.123.123 |

## Установка Certbot

Выполняем каждую команду отдельно:

```bash
apt update
apt policy snapd
apt install snapd
snap install core; snap update core
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot
certbot --version
certbot --nginx
```

Вводим всё, что просит:
```
your-email@gmail.com
y, y
domain.com www.domain.com
```

## Запускаем

Клонируем в `/var/www/` репозиторий:

`git clone <repo_url> /var/www/`

Линкуем nginx.conf:

`ln -s /var/www/domain/nginx.conf /etc/nginx/conf.d/domain.conf`

Перезапускаем Nginx

`service nginx restart`

Запускаем Django проект

## Результат

![HTTP3 support](https://github.com/web-polytech/2023/assets/73958047/f6a7d7f5-b9ab-47bf-9c21-1abcba531224)
