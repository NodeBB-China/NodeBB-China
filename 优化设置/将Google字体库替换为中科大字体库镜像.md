现在国内的Google字体库镜像中最好用的就是中科大的了，链接是：https://lug.ustc.edu.cn/wiki/lug/services/googlefonts，你会看到`fonts.googleapis.com`对应于`fonts.lug.ustc.edu.cn`这个加速链接。

### 修改方法：

以默认主题为例，在`nodebb/node_modules/nodebb-theme-persona/less/style.less`文件中有一条字体地址：`https://fonts.googleapis.com/css?family=Roboto:300,400,500,700`，将`fonts.googleapis.com`替换成`fonts.lug.ustc.edu.cn`就可以了。
注意，`1.4.x`版本在修改完这些`CSS`资源后需要手动运行`./nodebb build`编译一下才可以，不然的话`NodeBB`运行中依然不会去使用你修改之后的`CSS`。具体参见官方说明：[Introducing the build system in v1.4.x](https://blog.nodebb.org/introducing-the-build-system-in-v1-4-3/)。

可能这时候已经找不到`fonts.googleapis.com`但是网站还是还会加载谷歌字体，原因是`bootswatch`这个在搞鬼，它会动态加载谷歌字体
进入nodebb目录下，用`grep -rn "maxcdn.bootstrapcdn.com/bootswatch/latest/" .|grep -v "build"|grep -v "test"` 查找出
nodebb 1.5.2版本有两个地方需要更改
```
./src/middleware/header.js #220行
./public/src/client/account/settings.js #58行
```
因为是跟皮肤(Skin)关联的，需要下载多个css文件，根据主题个数一个一个下吧😂，我偷懒只下了三个。下载下来之后把第一行的 `@import url("https://fonts.googleapis.com.....`删掉或者替换为中科大的

我的配置如下：
本地css文件
```
public/css
└── bootswatch
    └── latest
        ├── darkly
        │   └── bootstrap.min.css
        ├── lumen
        │   └── bootstrap.min.css
        └── united
            └── bootstrap.min.css
```        

上面两个js路径更改为:
```
55                         if (skinName === 'default') {
56                                 skinName = config.defaultBootswatchSkin;
57                         }
58                         var cssSource = '/assets/bootswatch/latest/' + skinName + '/bootstrap.min.css';
59                         if (css.length) {
60                                 css.attr('href', cssSource);
61                         } else {
62                                 css = $('<link id="bootswatchCSS" href="' + cssSource + '" rel="stylesheet" media="screen">');
63                                 $('head').append(css);
64                         }
```