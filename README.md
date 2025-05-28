### dify-mermaid-flask-service
Dify实战: 手把手教你使用Dify搭建AI自动生成图表、流程图的应用

##工具介绍：

mermaid官网：https://mermaid.js.org/ 

GitHub代码仓库：https://github.com/mermaid-js/mermaid


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

## About

<!-- <Main description>   -->

Mermaid is a JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams. The main purpose of Mermaid is to help documentation catch up with development.

> Doc-Rot is a Catch-22 that Mermaid helps to solve.

Diagramming and documentation costs precious developer time and gets outdated quickly.
But not having diagrams or docs ruins productivity and hurts organizational learning.<br/>
Mermaid addresses this problem by enabling users to create easily modifiable diagrams. It can also be made part of production scripts (and other pieces of code).<br/>
<br/>

Mermaid allows even non-programmers to easily create detailed diagrams through the [Mermaid Live Editor](https://mermaid.live/).<br/>
For video tutorials, visit our [Tutorials](https://mermaid.js.org/ecosystem/tutorials.html) page.
Use Mermaid with your favorite applications, check out the list of [Integrations and Usages of Mermaid](https://mermaid.js.org/ecosystem/integrations-community.html).

You can also use Mermaid within [GitHub](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/) as well many of your other favorite applications—check out the list of [Integrations and Usages of Mermaid](https://mermaid.js.org/ecosystem/integrations-community.html).

For a more detailed introduction to Mermaid and some of its more basic uses, look to the [Beginner's Guide](https://mermaid.js.org/intro/getting-started.html), [Usage](https://mermaid.js.org/config/usage.html) and [Tutorials](https://mermaid.js.org/ecosystem/tutorials.html).

Our PR Visual Regression Testing is powered by [Argos](https://argos-ci.com/?utm_source=mermaid&utm_campaign=oss) with their generous Open Source plan. It makes the process of reviewing PRs with visual changes a breeze.
#### mermaid使用指南

1. 切换到mermaid-flask-service目录下
2. 构建docker镜像：docker build -t mermaid-flask-service：latest . 
3. 启动容器： docker run -d --name mermaid-flask-service -p 5002:5002 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default mermaid-flask-service:latest
            参数释义： --network 指定网络，这里必须一致因为dify是这两个网络，后续需要通信
4. 在dify中导入mermaid作图工具.yml和mermaid_agent.yml
   - 把mermaid作图工具创建出来的工作流发布为工具mermaid_service，并描述设置为"save mermain content and get svg url"
   - 在mermaid_agent中引用该工具mermaid_service

### dify-markmap-flask-service
Dify实战: 手把手教你使用Dify搭建AI自动生成思维导图的应用

##工具介绍：

markmap官网：https://markmap.js.org/

GitHub代码仓库：https://github.com/markmap/markmap/tree/master

<div align="center">
  <p>
    <img src="marp.png#gh-light-mode-only" alt="Marp" width="450" />
    <img src="marp-dark.png#gh-dark-mode-only" alt="Marp" width="450" />
  </p>
  <p>
    <strong>Marp</strong>: Markdown Presentation Ecosystem
  </p>
</div>

**Marp** is the ecosystem to write your presentation with plain Markdown.

<div align="center">

### [🌐 Website ▶︎](https://marp.app)&emsp;|&emsp;[💬 Discussion forum ▶︎](https://github.com/marp-team/marp/discussions)&emsp;|&emsp;[😎 Awesome list ▶︎](https://github.com/marp-team/awesome-marp)

</div>

## Marp family

Our project is spread over many repos in order to focus on a limited scope per repository.

This repo (**[marp-team/marp][marp]**) is an entrance to the Marp family, and places [our website](https://marp.app/) in `/website`.

### Framework / Core

|                       Name | Description                                                                                 | Release                                                   |
| -------------------------: | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------- |
|               **[Marpit]** | The skinny framework for creating slide deck from Markdown. ([marpit.marp.app])             | [![@marp-team/marpit][badge-marpit]][marpit-npm]          |
| **[Marp Core][marp-core]** | The core of Marp converter with practical features and [built-in themes][marp-core-themes]. | [![@marp-team/marp-core][badge-marp-core]][marp-core-npm] |

### Apps

|                     Name | Description                                                                                      | Release                                                |
| -----------------------: | :----------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **[Marp CLI][marp-cli]** | [Marp Core][marp-core] / [Marpit]'s CLI interface to convert into HTML, PDF, PPTX, and image(s). | [![@marp-team/marp-cli][badge-marp-cli]][marp-cli-npm] |

### Integrations

|                                Name | Description                                                                       | Release                                                     |
| ----------------------------------: | :-------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| **[Marp for VS Code][marp-vscode]** | A [VS Code][vscode] extension to preview the slide deck written in Marp Markdown. | [![VS Marketplace][badge-marp-vscode]][marp-vscode-release] |

<details>
<summary>See outdated/inactive projects...</summary><br />

|                     Name | Description                                                      | Release                                                      |
| -----------------------: | :--------------------------------------------------------------- | :----------------------------------------------------------- |
|     [Marp Web][marp-web] | The Web interface of Marp based on [PWA] and [Preact] framework. | [![tech demo][badge-marp-web]][marp-web-site]                |
| [Marp React][marp-react] | Marp renderer component for [React].                             | [![@marp-team/marp-react][badge-marp-react]][marp-react-npm] |
|     [Marp Vue][marp-vue] | Marp renderer component for [Vue].                               | [![@marp-team/marp-vue][badge-marp-vue]][marp-vue-npm]       |

And there is a gravesite of classic Marp app in https://github.com/yhatt/marp. :ghost:

[marp-web]: https://github.com/marp-team/marp-web
[marp-react]: https://github.com/marp-team/marp-react
[marp-vue]: https://github.com/marp-team/marp-vue
[pwa]: https://en.wikipedia.org/wiki/Progressive_Web_Apps
[preact]: https://preactjs.com/
[react]: https://reactjs.org/
[vue]: https://vuejs.org/
[marp-web-site]: https://web.marp.app/
[marp-react-npm]: https://www.npmjs.com/package/@marp-team/marp-react
[marp-vue-npm]: https://www.npmjs.com/package/@marp-team/marp-vue
[badge-marp-web]: https://img.shields.io/badge/%E2%80%8B-tech%20demo-%230288d1.svg?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAUUlEQVQokWNgGD6AqePif3Sx9B2PMcQwNKFrTN/x+D9ejTBNyBphmnBqRNYE04isCatGdE1MHRf/o2vC0IhNE1PaXPwacWnCqxGfJoI2Dn4AAN0ZrMM1VUFvAAAAAElFTkSuQmCC
[badge-marp-react]: https://img.shields.io/npm/v/@marp-team/marp-react.svg?style=flat-square&logo=npm
[badge-marp-vue]: https://img.shields.io/npm/v/@marp-team/marp-vue.svg?style=flat-square&logo=npm

</details>

[yhatt/marp]: https://github.com/yhatt/marp
[marp]: https://github.com/marp-team/marp
[marpit]: https://github.com/marp-team/marpit
[marp-core]: https://github.com/marp-team/marp-core
[marp-core-themes]: https://github.com/marp-team/marp-core/tree/main/themes
[marp-cli]: https://github.com/marp-team/marp-cli
[marp-vscode]: https://github.com/marp-team/marp-vscode
[vscode]: https://code.visualstudio.com/
[marpit.marp.app]: https://marpit.marp.app/
[marpit-npm]: https://www.npmjs.com/package/@marp-team/marpit
[marp-core-npm]: https://www.npmjs.com/package/@marp-team/marp-core
[marp-cli-npm]: https://www.npmjs.com/package/@marp-team/marp-cli
[marp-vscode-release]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode
[badge-marpit]: https://img.shields.io/npm/v/@marp-team/marpit.svg?style=flat-square&logo=npm
[badge-marp-core]: https://img.shields.io/npm/v/@marp-team/marp-core.svg?style=flat-square&logo=npm
[badge-marp-cli]: https://img.shields.io/npm/v/@marp-team/marp-cli.svg?style=flat-square&logo=npm
[badge-marp-vscode]: https://img.shields.io/visual-studio-marketplace/v/marp-team.marp-vscode.svg?style=flat-square&logo=visual-studio-code&label=Marketplace

## Ecosystem

Marp ecosystem has a lot of cool stuffs for making awesome presentation. Check out **[the awesome list of Marp](https://github

# markmap

[![Join the chat at https://gitter.im/gera2ld/markmap](https://badges.gitter.im/gera2ld/markmap.svg)](https://gitter.im/gera2ld/markmap?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Visualize your Markdown as mindmaps.

This project is heavily inspired by [dundalek's markmap](https://github.com/dundalek/markmap).

👉 [Try it out](https://markmap.js.org/repl).

## Related Projects

Markmap is also available in:

- [VSCode](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode) and [Open VSX](https://open-vsx.org/extension/gera2ld/markmap-vscode)
- Vim / Neovim:
  - [coc-markmap](https://github.com/gera2ld/coc-markmap) ![NPM](https://img.shields.io/npm/v/coc-markmap.svg) - powered by [coc.nvim](https://github.com/neoclide/coc.nvim)
  - [markmap.vim](https://github.com/Zeioth/markmap.nvim): for using without [coc.nvim](https://github.com/neoclide/coc.nvim)
- Emacs: [eaf-markmap](https://github.com/emacs-eaf/eaf-markmap) -- powered by [EAF](https://github.com/emacs-eaf/emacs-application-framework)
- MCP Server: [markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) [![NPM Version](https://img.shields.io/npm/v/@jinzcdev/markmap-mcp-server.svg)](https://www.npmjs.com/package/@jinzcdev/markmap-mcp-server) - powered by [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## Usage

👉 [Read the documentation](https://markmap.js.org/doc


#### markmap使用指南

1. 切换到markmap-flask-service目录下
2. 构建docker镜像：docker build -t markmap-flask-service：latest . 
3. 启动容器： docker run -d --name markmap-flask-service -p 5005:5005 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default markmap-flask-service:latest
4. 在dify中导入markmap思维导图工具.yml和markmap_agent.yml
   - 把markmap思维导图工具创建出来的工作流发布为工具save_markmap，并将工具描述改为"save markmap content and get url"
   - 在markmap_agent删除旧工具，并重新引用工具save_markmap

### dify-marp-flask-service
Dify实战: 手把手教你用 Dify 和 Marp 搭建AI自动生成 PPT 应用

#### marp使用指南

1. 切换到marp-flask-service目录下
2. 构建docker镜像：docker build -t marp-flask-service：latest . 
3. 启动容器： docker run -d --name marp-flask-service -p 5005:5005 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default marp-flask-service:latest
4. 在dify中导入marp的PPT工具.yml和marp_agent.yml
   - 把marp的PPT工具创建出来的工作流发布为工具,名字设置为save_marp_content，工具描述为"保存marp ppt内容，并获得ppt链接"
   - 在marp_agent.yml创建出的agent里删除旧工具，重新添加引用save_marp_content工具

### dify-quiz-flask-service 
DIfy实战：让AI给你出试卷-Dify实战：搭建自动生成试卷的Agent

### agent智能出卷使用指南

1. 切换到quiz-flask-service目录下
2. 构建docker镜像：docker build -t quiz-flask-service：latest . 
3. 启动容器： docker run -d --name markmap-flask-service -p 5006:5006 -v $(pwd)/data:/app/data  --network docker_ssrf_proxy_network --network docker_default quiz-flask-service:latest
4. 在dify中导入创建试卷工作流.yml和保存试卷agent.yml
   - 把创建试卷工作流.yml创建出来的工作流发布为工具,名字设置为save_quiz_and_get_url，工具描述为"保存试卷并获取试卷url"
   - 在保存试卷agent.yml创建出的agent里删除旧工具，重新添加引用save_quiz_and_get_url工具
""
