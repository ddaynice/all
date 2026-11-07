# -*- coding: utf-8 -*-
"""工具注册表：平台首页展示的工具列表。

加新工具的三步：
1. 在 platform/static/ 下新建工具页面目录
2. 在这里注册一条（id/name/desc/icon/url）
3. server.py 里挂载对应静态目录或后端路由
"""

TOOLS = [
    {
        "id": "quiz",
        "name": "面试刷题",
        "desc": "间隔重复刷题自测，支持分类浏览、搜索与掌握度统计",
        "icon": "📝",
        "url": "/quiz/",
    },
    {
        "id": "chat",
        "name": "AI 面试陪练",
        "desc": "和 AI 面试官模拟面试、答题点评、自由技术提问",
        "icon": "🤖",
        "url": "/chat/",
    },
    {
        "id": "sync",
        "name": "资料同步",
        "desc": "从飞书拉取最新文档，转换入库并重建 AI 检索索引",
        "icon": "📡",
        "url": "/sync/",
    },
]
