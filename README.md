English | [中文](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/docs/README-CN.md)

## Cryptocurrency Assistant: Market Analysis, Price Alerts, and Quantitative Trading

This system is designed for quickly building a cryptocurrency data analysis platform. With basic programming knowledge, you can get started quickly. It provides common **cryptocurrency analysis strategies** examples, including the ahr999 index, Pi cycle top indicator, and more. Future implementations will include price alerts and quantitative trading features.
This system is inspired by: [Cryptocurrency-Analysis-Python](https://github.com/triestpa/Cryptocurrency-Analysis-Python)

**Price-Volume Chart**

BTC Daily Price-Volume Chart

![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/PriceVolume.png)

**Ahr999 Index Implementation**
The ahr999 index is a Bitcoin accumulation index proposed by Weibo user ahr999. When the index is below 1.2, it indicates that the coin price has returned to normal values and you can start dollar-cost averaging. When the index is below 0.45, it indicates that the coin price is severely undervalued.
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/ahr999.png)
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/ahr999x.png)

**Pi Top Indicator**
The Pi top indicator is a top indicator proposed by [Philip Swift](https://twitter.com/PositiveCrypto). Through backtesting, he found that in the past three bull markets, the highest price points all occurred when MA111 exceeded MA350*2. Therefore, this indicator can be used to guide whether it's time to exit the market. (However, due to the small number of backtesting points, there may be overfitting issues)
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/PiTop.png)

### Feature List

|  | Item |
| ------- | --------- |
| &check; | ahr999 index |
| &check; | ahr999x index |
| &check; | PI top indicator |
| &cross; | Data filtering |
| &cross; | Price alerts |
| &cross; | Quantitative trading |
| &cross; | Other cryptocurrencies |

### Usage Process

#### 1. Environment Setup

*This section references the [blog](https://blog.patricktriest.com/analyzing-cryptocurrencies-python/). English readers can refer to it directly.*

**1.1 Install Anaconda**
Anaconda is a powerful open-source Python distribution that includes conda, Python, and numerous scientific packages. Download and install from the [Anaconda website](https://www.anaconda.com/products/individual).

**1.2 Create Anaconda Project Environment**
There are many Python versions, and each project may require different Python versions and dependencies. Therefore, we need to create a Python environment for this project using Anaconda.
Open Anaconda Prompt and enter the following command:

```
conda create --name cryptocurrency-assistant python=3
```
At this point, we have created an environment named *cryptocurrency-assistant*. We can view all existing environments in the system using:
```
conda env list
```
Use the following command to switch to the newly created cryptocurrency-assistant environment:
```
activate cryptocurrency-assistant
```
Install the required dependencies using:
```
conda install numpy pandas nb_conda jupyter plotly
```
**1.3 Start Jupyter notebook**

>Jupyter Notebook is a web-based interactive computing application. It can be used for the entire computing process: development, documentation, code execution, and result presentation.—[Jupyter Notebook Official Introduction](https://jupyter.org/)

In simple terms, Jupyter Notebook opens in a web browser where you can directly write and run code, with results displayed directly below the code blocks. If you need to write documentation during programming, you can do so on the same page, making it convenient for immediate explanation and clarification.
Enter the following command to access Jupyter notebook at http://localhost:8888:
```
jupyter notebook
```
**1.4 Data Source Preparation**
Copy the file data/20130428-20210725.tsv to the C drive root directory

#### 2. Run the Code
Copy the code from main.py, each **# In[]** cell's content, into separate cells in a new Jupyter notebook. Click run to execute the code and generate the corresponding trend charts.
![image](https://github.com/JunqiaoDuan/CryptocurrencyAssistant/blob/main/images/sample-analyzer.png)

### Disclaimer
This system is only for sharing common cryptocurrency analysis strategies and quantitative trading solutions. It does not constitute any investment advice. Any profits, losses, or legal risks are not the responsibility of the author.

