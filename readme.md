# 测试GPT-4 Turbo 在Azure 不同Region的性能


本Repo中的两个python程序，可以分别调用多个Azure Region的Azure Openai和openai.com。

 - [azure-openai-gpt4turbo.py](azure-openai-gpt4turbo.py) 调用Azure Openai GPT-4 turbo API，使用openaiperfdata.csv文件保存性能数据

 - [openai-dotcom-gpt4turbo.py](openai-dotcom-gpt4turbo.py) 调用Openai.com的GPT-4 turbo API，使用openaiperfdata.csv文件保存性能数据


## 安装

### 首先，你需要安装 Python 和 Python的openai库：


```bash
pip install openai 

```

### 然后，你需要将azure openai API连接和prompt信息写入到[ `api_info.csv`](api_info.csv) 的 CSV 文件，其中包含以下列，可以输入多个region上的API信息：

- region
- endpoint
- api_key
- engine
- prompt
  

例子： AustraliaEast,https://ai-australiaeast.openai.azure.com/,<你的azure openai api_key >,gpt-4-turbo-australiaeast,用300个左右的汉字描述什么是微软Azure?

### 接着你需要将openai.com API连接和prompt信息写入到 [`api_info_openai.csv`](api_info_openai.csv) 的 CSV 文件，其中包含以下列，可以输入多条openai.com上的api_key的API信息：

- region(设置成openai)
- api_key
- engine
- prompt

例子： 
openai,https://api.openai.com/,sk-<your own openai api_key>,gpt-4-1106-preview,用300个左右的汉字描述什么是微软Azure?
## 运行

### 初始测试一次性运行程序
初始测试阶段，你可以使用以下命令一次性运行程序，然后观测结果：

```bash 将结果保存到同目录的CSV文件openaiperfdata.csv中
python azure-openai-gpt4turbo.py 

python openai-dotcom-gpt4turbo.py
```
### 长时间在Linux测试机（Openai API客户端）定时运行

在 Linux 中，你可以使用 cron 来定时执行程序。以下是如何设置每小时执行一次 Python 程序的步骤：

打开终端。

输入 crontab -e 命令来编辑你的 cron 任务。

在打开的编辑器中，添加以下两行：

```bash
0 * * * * /usr/bin/python3 /path/to/your/azure-openai-gpt4turbo.py 
0 * * * * /usr/bin/python3 /path/to/your/openai-dotcom-gpt4turbo.py
```


这行命令的意思是，每小时的第 0 分钟，执行这两个Python程序。/usr/bin/python3 是 Python 解释器的路径，你需要根据你的系统来修改这个路径。/path/to/your/azure-openai-gpt4turbo.py 是你的 Python 程序的路径，你需要替换为你的程序的实际路径。

保存并关闭编辑器。
现在，你的 Python 程序应该会每小时执行一次。你可以使用 crontab -l 命令来查看你的 cron 任务。

请注意，cron 使用的是系统时间，你需要确保你的系统时间是正确的。此外，你的 Python 程序应该能在没有交互的情况下运行，因为 cron 任务是在后台运行的。
## 测试结果

将openaiperfdata.csv中的测试结果导入到Excel或各种数据可视化工具进行分析各个Azure Region及openai.com的模型性能。