# 利用scrapy框架爬取糗事百科并将其存为json
## scrapy基本框架介绍和项目建立
* Scrapy Engine：引擎核心，接受所有信号并发送信号
* Item Pipeline：处理数据、储存
* Schedule（调度器）：处理url队列，接收引擎发送的请求，并排列整理，入队
* Downloader（下载器）：下载服务器端数据
* middleware：设置代理ip，请求头等

爬取顺序

1.spider发送请求  
2.请求发送至Schedule  
3.url存入队列，引擎取出url，传至downloader  
4.数据返回至引擎，传入spider，提取需要数据  
5.提取的url返给Schedule，提取数据传给item pipeline存储  

### 安装
pip install scrapy  
windows下还需安装：  
pip install pypiwin32  

### 创建项目
1.python环境cmd命令：  
scrapy startproject [项目名称]  
2.使用命令在 [项目名称] 文件夹内创建一个爬虫  
**爬虫名不能和项目名称相同**  
scrapy genspider [爬虫名] "xxx.com"  
**爬取网页限制在 xxx.com 域名下**  

### 修改setting文件
* ROBOSTXT_OBEY——修改为False
* DEAFAULT_REQUEAT_HEADERS——添加 User-Agent

## scrapy爬取糗事百科
* name：标识爬虫名字，多个爬虫时每个爬虫名字必须唯一
* allowed_domains：允许爬取范围
* start_urls：开始url，一般写一个就行  
此处start_urls = ['https://www.qiushibaike.com/text/page/1/']  
### 编写parse函数
解析网页发现，笑话信息均在xpath：//div[@id="content-left"]的每个div下  
而对应的下一页链接在xpath：//ul[@class="pagination"]/li[last()]/a/@href 中  
以此循环获取作者和文本，并存于json中  
详情见python文件注释

