

```markdown
# 测试GPT-4 Turbo 在Azure 不同Region的性能

本Repo中的两个python文件可以连接多个Azure Region的Azure Openai。

 - azure-openai-gpt4turbo.py 用于小数据量测试，使用CSV文件保存性能数据即可，建议初始部署使用azure-openai-gpt4turbo.py 即可。
 - azure-openai-gpt4turbo-with-cosmosdb.py将性能数据及相关详细的数据写入Cosmos DB SQL API并同时写入CSV，用于近一步分享。
## 安装

首先，你需要安装 Python 和以下 Python 库：

- openai
- azure-cosmos（如果使用Azure Cosmos DB作为结果数据存储）

你可以使用以下命令安装这些库（）：

```bash
pip install openai 
pip install azure-cosmos
```

然后，你需要将azure openai API连接和prompt信息写入到 `api_info.csv` 的 CSV 文件，其中包含以下列：

- region
- endpoint
- api_key
- engine
- prompt

例子： AustraliaEast,https://ai-australiaeast.openai.azure.com/,<你的azure openai api_key >,gpt-4-turbo-australiaeast,用300个左右的汉字描述什么是微软Azure?


## 运行

你可以使用以下命令运行程序：

```bash 将结果保存到同目录的CSV文件openaiperfdata.csv中
python azure-openai-gpt4turbo.py 
```


如果使用了cosmos DB，请先创建Azure Cosmos DB（SQL API），并修改azure-openai-gpt4turbo-with-cosmosdb.py中的入cosmos DB的连接信息，然后运行如下命令：

```bash 将结果保存到cosmos DB和同目录的CSV文件openaiperfdata.csv中
python azure-openai-gpt4turbo-with-cosmosdb.py
```

## 测试结果

将openaiperfdata.csv中的测试结果导入到Excel或各种数据可视化工具进行分析各个Azure Region的openai性能。