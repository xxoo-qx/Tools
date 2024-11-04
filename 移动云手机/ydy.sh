#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [[ ! $(id -u) == '0' ]]; then
    echo -e "${RED}ROOT?${NC}"
    exit
fi

function install() {
    pkill httpd
    rm -rf /data/139
    mkdir /data/139
    wget -q -O /data/139/httpd "https://proxy.zxyxndc.top/https://raw.githubusercontent.com/xxoo-qx/Tools/refs/heads/main/%E7%A7%BB%E5%8A%A8%E4%BA%91%E6%89%8B%E6%9C%BA/busybox"
    chmod 777 /data/139/httpd
    /data/139/httpd -p 10003
    httpdstatus=$(ps -ef | grep httpd | grep -v grep | awk '{print $2}')
    if [[ $httpdstatus ]]; then
        echo -e "${GREEN} httpd 启动成功${NC}"
    else
        echo -e "${RED} httpd 启动失败${NC}"
        uninstall
        exit
    fi
}

function uninstall() {
    echo -e "${YELLOW}======回车删除环境======${NC}"
    read
    pkill httpd
    rm -rf /data/139
}

echo -e "${YELLOW}========安装环境========${NC}"
install
ip=$(curl -s -4 "43.136.48.19:10103")
echo -e " 当前IP: ${GREEN}${ip}${NC}"
echo " 开始探测端口"
echo -e "${YELLOW}========等待一会========${NC}"
for a in {000..999}; do
    a="10${a}"
    url="http://${ip}:${a}"
    status=$(curl --connect-timeout 0.1 --max-time 0.1 -o /dev/null -s -w "%{http_code}" "${url}")
    if [[ ${status} == '404' ]]; then
        port=${a}
        break
    fi
done
if [[ ${port} ]]; then
    echo -e " 端口：10002 ———— ${GREEN}$((${port} - 1))${NC}"
    echo -e " 端口：10003 ———— ${GREEN}${port}${NC}"
    echo -e " 端口：10004 ———— ${GREEN}$((${port} + 1))${NC}"
else
    echo '========================'
    echo -e "${RED}未找到可用端口${NC}"
fi
uninstall
