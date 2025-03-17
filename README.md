# Tools
常用脚本

# 移动云电脑 DD Debian12
1. 用官方程序进入移动云电脑
2. [永久关闭windows安全中心软件](http://icloud.zxxoo.work:5244/d/iCloud/Share/%E8%A3%85%E6%9C%BA%E5%BF%85%E5%A4%87/DefenderRemover.exe?sign=SVIVxCeBB_hEW-5ZzOC16qHa_4bZ7L2YrYGTaVOso8M=:0)
3. 下载[reinstall.bat](https://sina.zxyxndc.top/reInstall)
4. 将`reinstall.bat`移到桌面
5. 打开`cmd`，进入桌面路径，输入`reinstall.bat alpine-3.18`
6. 上一步等待重启完成后alpine系统安装就成功了，登陆用户名`root` 密码`123@@@`，登陆后输入命令`apk add wget curl bash`安装依赖
7. 下载[DD脚本](https://sina.zxyxndc.top/Install)
8. 在云电脑终端输入命令`wget `[https://sina.zxyxndc.top/Install](https://sina.ymoo.buzz/Install) -O Install.sh 获取DD脚本
9. 赋予脚本可执行权限，输入`chmod +x Install.sh`
10. DD Debian系统，输入`bash Install.sh -debian 12 -pwd 123 -port 22`这个命令是指定DD到 Debian 12 系统，root 密码为123，SSH 端口为 22
11. 等待脚本执行完毕后根据提示输入`reboot`重启，随后开始DD系统，期间从官方程序可以看到进度
12. 安静等待系统安装完成后自动重启，登陆用户名`root` 密码`123`
13. 安装并加入 ZeroTier 网络(可选)

```Plain Text
#安装 ZeroTier
curl -s https://install.zerotier.com/ | bash

#加入 ZeroTier网络
zerotier-cli join <你的网络ID>
```
14. 随后就可以通过SSH工具登陆DD后的移动云电脑了
