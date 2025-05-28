### dify-mermaid-flask-service
Dify实战: 手把手教你使用Dify搭建AI自动生成图表、流程图的应用

工具介绍：
<p align="center">
<img src="https://raw.githubusercontent.com/mermaid-js/mermaid/develop/docs/public/favicon.svg" height="150">
</p>
<h1 align="center">
Mermaid
</h1>
<p align="center">
Generate diagrams from markdown-like text.
<p>
<p align="center">
  <a href="https://www.npmjs.com/package/mermaid"><img src="https://img.shields.io/npm/v/mermaid?color=ff3670&label="></a>
<p>

<p align="center">
<a href="https://mermaid.live/"><b>Live Editor!</b></a>
</p>
<p align="center">
 <a href="https://mermaid.js.org">📖 Documentation</a> | <a href="https://mermaid.js.org/intro/">🚀 Getting Started</a> | <a href="https://www.jsdelivr.com/package/npm/mermaid">🌐 CDN</a> | <a href="https://discord.gg/sKeNQX4Wtj" title="Discord invite">🙌 Join Us</a>
</p>
<p align="center">
<a href="./README.zh-CN.md">简体中文</a>
</p>
<p align="center">
Try Live Editor previews of future releases: <a href="https://develop.git.mermaid.live/" title="Try the mermaid version from the develop branch.">Develop</a> | <a href="https://next.git.mermaid.live/" title="Try the mermaid version from the next branch.">Next</a>
</p>

#### 使用指南

1. 切换到mermaid-flask-service目录下
2. 构建docker镜像：docker build -t mermaid-flask-service：latest . 
3. 启动容器： docker run -d --name mermaid-flask-service -p 5002:5002 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default mermaid-flask-service:latest
            参数释义： --network 指定网络，这里必须一致因为dify是这两个网络，后续需要通信
4. 在dify中导入mermaid作图工具.yml和mermaid_agent.yml
   - 把mermaid作图工具创建出来的工作流发布为工具mermaid_service，并描述设置为"save mermain content and get svg url"
   - 在mermaid_agent中引用该工具mermaid_service

### dify-markmap-flask-service
Dify实战: 手把手教你使用Dify搭建AI自动生成思维导图的应用

#### 使用指南

1. 切换到markmap-flask-service目录下
2. 构建docker镜像：docker build -t markmap-flask-service：latest . 
3. 启动容器： docker run -d --name markmap-flask-service -p 5005:5005 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default markmap-flask-service:latest
4. 在dify中导入markmap思维导图工具.yml和markmap_agent.yml
   - 把markmap思维导图工具创建出来的工作流发布为工具save_markmap，并将工具描述改为"save markmap content and get url"
   - 在markmap_agent删除旧工具，并重新引用工具save_markmap

### dify-marp-flask-service
Dify实战: 手把手教你用 Dify 和 Marp 搭建AI自动生成 PPT 应用

#### 使用指南

1. 切换到marp-flask-service目录下
2. 构建docker镜像：docker build -t marp-flask-service：latest . 
3. 启动容器： docker run -d --name marp-flask-service -p 5005:5005 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default marp-flask-service:latest
4. 在dify中导入marp的PPT工具.yml和marp_agent.yml
   - 把marp的PPT工具创建出来的工作流发布为工具,名字设置为save_marp_content，工具描述为"保存marp ppt内容，并获得ppt链接"
   - 在marp_agent.yml创建出的agent里删除旧工具，重新添加引用save_marp_content工具

### dify-quiz-flask-service 

让AI给你出试卷-Dify实战：搭建自动生成试卷的Agent
1. 切换到quiz-flask-service目录下
2. 构建docker镜像：docker build -t quiz-flask-service：latest . 
3. 启动容器： docker run -d --name markmap-flask-service -p 5006:5006 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default quiz-flask-service:latest
4. 在dify中导入创建试卷工作流.yml和保存试卷agent.yml
   - 把创建试卷工作流.yml创建出来的工作流发布为工具,名字设置为save_quiz_and_get_url，工具描述为"保存试卷并获取试卷url"
   - 在保存试卷agent.yml创建出的agent里删除旧工具，重新添加引用save_quiz_and_get_url工具
""
