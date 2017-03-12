### 2017-2-26 日更新：

360前端团队已于2016年12月7日[重新启动了前端静态资源库服务](http://wangzhan.360.com/notice/detail/10005)，请前往[360 前端静态资源库](https://cdn.baomitu.com/index/fonts)页面，但是感觉不如以前好用了。

---

#注意，由于360公共前端库已经停止服务，所以本教程作废。另外经过测试发现Google字体库的中国区服务器位于北京和上海，访问速度非常快，已经没必要再换其他字体库了。

>关于Google字体库的测试说明参见我写的知乎问答：https://www.zhihu.com/question/24955477/answer/120232550

---

#以下是原文章

#更换Google字体库为360公共前端库

---

##查找使用Google字体库的文件

可以nodebb目录下使用命令grep -r -l "googleapis" * 查找出所有包含Google字体库链接的文件，
对于默认主题来说只需要更改`nodebb/node_modules/nodebb-theme-persona/less/style.less`文件里面的链接即可。

##替换链接

以下摘录[360公共前端库](http://libs.useso.com/ "360公共前端库")的说明：

>* 首先在程序源代码中找到调用Google免费字体库的地址，比如：

	<link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,600&subset=latin,latin-ext' rel='stylesheet'>

>* 将Google免费字体库的域名 fonts.googleapis.com 修改为：fonts.useso.com 即可，如下所示：

	<link href='http://fonts.useso.com/css?family=Open+Sans:300,400,600&subset=latin,latin-ext' rel='stylesheet'>

##重启NodeBB

改完后重启nodebb就能生效。

##测试效果

按下F12然后Ctrl+F5刷新页面，在Sources一栏里就能看到fonts.googleapis.com已经变成了fonts.useso.com。在Network一栏里搜font，点击一下也能看到字体链接不再是fonts.gstatic.com而是fontstatic.useso.com。

##附录

下面这个链接是官方论坛里一个类似的问题，但是所用的主题是lavender

https://community.nodebb.org/topic/2178/i-want-to-remove-the-google-fonts-link-what-shoud-i-do/6