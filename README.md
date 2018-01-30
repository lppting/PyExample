网易蜗牛阅读改时长
需要的环境和工具：
ROOT过的手机一台
RootExplorer浏览器
NeoTerm：21世纪的终端
Python2.7
git工具

基本思路：
每天有领取的时长，但是不联网的时候时长还是掉，所以肯定在本地存储了一个数值。
十二点领了时长之后，通过RE浏览器以时间排序，找到/data/data/com.netease.snailread/database/snailRead.db
有改动的痕迹。
同时com.netease.snailread/file文件夹下的后缀为temp的文件里面有更新剩余时长的记录，看到关键词ReadLeftTime。
在snailRead.db里有ReadLeftTime表，用RE查看表，果然有left_time的值。
因为在酷安找不着可以改数据库的软件，于是改用python。
NeoTerm在su用户下可以用Python，所以就可以有权限改snailRead数据库。

NeoTerm用来改数据，RE用来看，确定数值变了后，再打开蜗牛读书。
切记！！！先断网再进蜗牛读书！！！先断网！！！
每次进蜗牛读书，软件会从服务器读取剩余时长，然后更新数据库。
不断网进入，修改的数据会直接被修改成服务器时长。

我用的最惨的方法，看有没有大神从服务器端入手。
仅供参考QAQ
