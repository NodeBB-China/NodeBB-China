现在国内的Google字体库镜像中最好用的就是中科大的了，链接是：https://lug.ustc.edu.cn/wiki/lug/services/googlefonts，你会看到`fonts.googleapis.com`对应于`fonts.lug.ustc.edu.cn`这个加速链接。

### 修改方法：

以默认主题为例，在`nodebb/node_modules/nodebb-theme-persona/less/style.less`文件中有一条字体地址：`https://fonts.googleapis.com/css?family=Roboto:300,400,500,700`，将`fonts.googleapis.com`替换成`fonts.lug.ustc.edu.cn`就可以了。
注意，`1.4.x`版本在修改完这些`CSS`资源后需要手动运行`./nodebb build`编译一下才可以，不然的话`NodeBB`运行中依然不会去使用你修改之后的`CSS`。具体参见官方说明：[Introducing the build system in v1.4.x](https://blog.nodebb.org/introducing-the-build-system-in-v1-4-3/)。