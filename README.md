# CryptocurrencyAssistant
## 加密货币助手：行情分析，价格预警，量化交易

本系统用于快速搭建加密货币数据分析平台，只要有一点编程基础，就可以快速入手。提供常见的**加密货币分析策略**案例，包括ahr999指数，Pi周期逃顶指数等。后续还将实现价格预警，量化交易等功能。
本系统灵感来源：[Cryptocurrency-Analysis-Python](https://github.com/triestpa/Cryptocurrency-Analysis-Python)

**量价图**

btc每日量价图

![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/PriceVolume.png)

**ahr999指数实现**
ahr999指数是微博用户ahr999提出的比特币囤币指数。当指数低于1.2时，表示币价回归正常值，可以开始定投，当指数低于0.45时，表示币价严重低估。
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/ahr999.png)
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/ahr999x.png)

**Pi逃顶指数**
Pi逃顶指数是[Philip Swift](https://twitter.com/PositiveCrypto)提出的逃顶指数。他回测发现，过去3次牛市，币价最高点都发生在MA111超过MA350\*2时，因此该指数可以用于指导是否可以逃顶。（但也正因为回测点太少，可能存在过拟合的情况）
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/PiTop.png)





### 功能清单

|  | 项目 |
| ------- | --------- |
| &check; | ahr999指数 |
| &check; | ahr999x指数 |
| &check; | PI 逃顶指数 |
| &cross; | 数据筛选 |
| &cross; | 价格预警 |
| &cross; | 量化交易 |
| &cross; | 其它币种 |

### 使用流程

#### 1. 搭建环境

*此部分参照[博客](https://blog.patricktriest.com/analyzing-cryptocurrencies-python/)，英语好的同学可以移步。*

**1.1 安装Anaconda**
Anconda是一个非常强大的开源Python发行版本，包含了conda、Python以及一大堆科学包。在[Anaconda官网](https://www.anaconda.com/products/individual)下载文件，并安装。

**1.2 创建Anaconda项目环境**
Python的版本有很多，每个项目的Python版本和依赖包都可能不一样，所以我们要先用Anaconda创建一个本项目的Python环境。
打开Anaconda Promote，在弹出的命令框中输入指令：

```
conda create --name cryptocurrency-assistant python=3
```
此时，我们已经创建好了一个名为*cryptocurrency-assistant*的环境。我们可以通过以下命令，查看目前系统中已有的环境：
```
conda env list
```
通过以下命令，将当前环境切换到刚才新创建的cryptocurrency-assistant
```
activate cryptocurrency-assistant
```
通过以下命令，安装我们所需要的依赖包：
```
conda install numpy pandas nb_conda jupyter plotly
```
**1.3 开启Jupyter notebook**

>Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——[Jupyter Notebook官方介绍](https://jupyter.org/)

简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。
在命令框中输入以下命令，将可以通过http://localhost:8888 使用Jupyter notebook。
```
jupyter notebook
```
**1.4 数据源准备**
将文件data/20130428-20210725.tsv拷贝到C盘根目录下
#### 2. 运行代码
把项目中main.py的代码，每个 **# In[]** cell中的内容，依次复制到新建的 Jupyter notebook的每一个cell中，点击运行代码，就可以看到代码正常运行，并生成相应的趋势图。
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/sample-analyzer.png)









### 免责声明
此系统只是用于分享加密货币的常见分析策略及量化交易方案，不构成任何投资建议，任何盈亏及法律风险与作者无关。

