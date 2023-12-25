import csv
import openai
from azure.cosmos import CosmosClient
import time
import datetime

# Azure Cosmos DB 连接信息
url = "<Azure Cosmos DB URI >"
key = "<Azure Cosmos DB KEY"
database_name = "<Azure Cosmos DB Database Name>"
container_name = "<Azure Cosmos DB Container Name>"



openai.api_type = "azure"

# 从csv文件中读取API信息
with open('api_info.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        region = row['region']
        endpoint = row['endpoint']
        api_key = row['api_key']
        engine = row['engine']
        prompt = row['prompt']
        
        openai.api_base = endpoint
        openai.api_version = "2023-07-01-preview"
        openai.api_key = api_key

        message_text = [{"role":"system","content":"您是一个帮助人们找到信息的AI助手。"},{"role":"user","content": prompt}]

        start_time = datetime.datetime.now()
        print("地区:", region)
        print("开始时间:", start_time)

        completion = openai.ChatCompletion.create(
            engine=engine,
            messages = message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        end_time = datetime.datetime.now()
        execution_time = end_time - start_time

        result = completion.choices[0].message['content']
        result_details = completion

        print("API调用执行时间:", execution_time)

        # 连接到Azure Cosmos DB
       
        client = CosmosClient(url, credential=key)

        # 选择数据库和容器

        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        # 在容器中创建一个新的项，以时间戳作为ID
        timestamp = str(int(time.time()))
        item = {
            "id": timestamp,
            "region": region,
            "prompt": prompt,
            "start_time": start_time.strftime("%Y-%m-%d %H:00"),
            "end_time": end_time.isoformat(),
            "execution_time": execution_time.total_seconds(),
            "result": str(result),  # 将结果转换为字符串
            "result_details": str(result_details)  # 将结果详细信息转换为字符串
        }
        container.create_item(item)
        
        # 将项写入CSV文件
        csv_file = 'openaiperfdata.csv'
        fieldnames = item.keys()
        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(item)

        
        # 将项写入CSV文件
        print(result)
