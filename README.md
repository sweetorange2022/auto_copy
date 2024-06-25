# auto_copy
这是一个用于自动复制的小工具。希望它能帮助你提升你的工作效率。

如果你只是使用这个软件，不关心他的代码和生成过程，可以直接下载编译后的版本，我会把最新的链接放在这里:[入口]();


版本更新：
v1.0 : 2024.06.25
当你点击启动软件后，它自动会把你接下来选中的文本的复制下来，然后你可以使用ctrl + v 进行粘贴。


代码见仓库文件：

复现方法：
一、前置条件：
1、默认windows系统，因为我常在这个系统下办公，所以选择这个系统下开发。
2、安装了python，因为我们使用的语言就是python。
3、安装两个 python 中用于处理剪贴板和键盘/鼠标事件的Python库 ：
'pip install pyperclip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple'

二、idea中运行python代码

三、软件生成
1、安装pyinstaller库 :  'pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple'
2、在cmd 中 cd 到对代码应目录下，执行 ： 'pyinstaller --onefile auto_copy.py'

生成的可执行文件将位于 dist 目录中，可以直接双击运行。


灵感来源：
在使用Mobaxterm时，我注意到其软件中具备选中即自动复制和右键直接粘贴的功能。但是，这种选中自动复制的功能仅在软件内部有效。
由于这一功能极为便捷，我经常在软件外不自觉地尝试进行选中即复制的操作，然后意识到选中自动复制的功能仅在软件内部有效。
因此，我萌生了开发一个工具软件的想法，使整个系统都能实现选中即复制和右键即粘贴的功能。











It has been tested successfully with windows 11, other windows should be fine, but I haven't tested it yet because my electricity is only windows 11 version.
