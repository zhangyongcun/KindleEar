Readme of english version refers to [Readme_EN.md](https://github.com/cdhigh/KindleEar/blob/master/readme_EN.md)

# 简介
这是一个运行在Google App Engine(GAE)上的Kindle个人推送服务应用，生成排版精美的杂志模式mobi/epub格式自动每天推送至您的Kindle或其他邮箱。

此应用目前的主要功能有：  

* 支持类似Calibre的recipe格式的不限量RSS/ATOM或网页内容收集
* 不限量自定义RSS，直接输入RSS/ATOM链接和标题即可自动推送
* 多账号管理，支持多用户和多Kindle
* 生成带图的杂志格式mobi或带图的有目录epub
* 自动每天定时推送
* 强大而且方便的邮件中转服务
* 和Evernote/Pocket/Instapaper等系统的集成

> 注：如果您要求不高，自定义RSS推送功能足以应付一般应用，如果要求排版和完美，可以参照books目录下的文件范本自己添加一个文件再重新上传即可，books目录下的书籍文件都不是随意预置的，每个文件都至少演示一个适用的books编写技巧。
在您懂python的前提下，您可以完全的操控网页，可以生成您需要的最完美的MOBI/EPUB文件。

# 标准部署步骤
1. 创建 APP 引擎
打开 APP 引擎中心，创建一个 APP 引擎。（如果你之前没有创建过 Project ,需要先创建一个项目。） 
![](https://cdn.sspai.com/2017/08/19/95355b0c83414d566616b2553bd67675.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)
![](https://cdn.sspai.com/2017/08/19/3eba4a66dab988bb6b286eb3988a54a9.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)
点击 【Next】开始创建
![](https://cdn.sspai.com/2017/08/19/da82b29c6d678d3e2abe97c65c0ca8ac.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)
创建完成，根据教程，点击继续，打开控制台 shell，如果弹出教程，【退出教程】即可。
![](https://cdn.sspai.com/2017/08/19/8250d3b84e679a4842192d0c2045b433.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

激活远端 shell 之后，分别输入命令进行下载安装和部署
```shell
wget http://qn.zhangyongcun.com/file/kindleEar.sh  
chmod +x kindleEar.sh
./kindleEar.sh
```

执行阶段会提示输入你的 Gmail 邮箱和当前的 APP ID，键入回车键之后，就开始自动部署了。
![](https://cdn.sspai.com/2017/08/19/78b830ff39796ad49da113c56bb58487.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

刷新  APP 引擎中心 页面，就可以看到部署信息了。点击图示的链接，即可访问服务。
![](https://cdn.sspai.com/2017/08/19/61a1623f004c3708a76c268d25a8ed9d.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)
打开链接，默认账号密码均为：admin

![](https://cdn.sspai.com/2017/08/19/97278dafc8cf2ce0cc594d9be9db2a58.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

登陆之后，点击 【我的订阅】进行设置，如果出现 【internal server error】，是因为系统没有完全部署完成，稍等五分钟左右就可以正常使用。
![](https://cdn.sspai.com/2017/08/19/50025e542a6426752f3762457550df6f.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

注意：推送之前，你需要完成以下操作。
设置 Gmail 邮箱到 Kindle 信任邮箱中，在 我的亚马逊 中【管理我的内容和设备】--【设置】在 【已认可的发件人电子邮箱列表】中添加。
打开 APP 引擎中心 ，添加 【已获授权的发件人】
![](https://cdn.sspai.com/2017/08/19/adb7d1b6c6a352617b9ac4306f012fa1.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

设置投递选项，注意修改之后需要选择 【保存设置】
![](https://cdn.sspai.com/2017/08/19/93abd96b8e2464a71a994b8fadef05b1.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

【投递日志】可以查看投递的状态。由于 RSS 内容抓取需要一定的时间，所以日志可能会有延迟。
![](https://cdn.sspai.com/2017/08/19/c0c2ec72ff300a48c19ea53529e169b1.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

# 许可协议
KindleEar is licensed under the [AGPLv3](http://www.gnu.org/licenses/agpl-3.0.html) license.  
大体的许可框架是此应用代码你可以任意使用，任意修改，可以商用，但是必须将你修改后的代码开源并保留原始版权声明。

# 捐赠
如果你希望支持一下KindleEar，可以戳 [Wiki捐赠页面](https://github.com/cdhigh/KindleEar/wiki/Donate)
