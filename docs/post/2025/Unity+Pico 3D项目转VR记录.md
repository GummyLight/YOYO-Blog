---
aliases: []
title: Unity+Pico 3D项目转VR记录
sidebar:
date: 2025-09-11
category:
  - 技术
tags: []
status:
  - published
description: ""
---
---
# Unity+Pico 3D项目转VR记录

1. 环境配置 [1. 创建开发者帐号、组织和应用 | PICO 开发者平台](https://developer-cn.picoxr.com/document/unity/create-a-developer-account-organization-and-app/) 参见入门教程，完成1-4
2. XR origin 的坐标为Player的坐标复制而来，两个的Main Camera采用同样的坐标，这样可以把头显视角移动到3D的用户视角位置。
3. 以上两步可以实现 全景显示和手柄识别，接下来实现交互
4. 手柄交互（一）：移动旋转 [XR Interaction Toolkit教程⭐二、实现移动、传送和人物的碰撞 - 技术专栏 - Unity官方开发者社区](https://developer.unity.cn/projects/65769b7fedbc2a0026540015)
5. 手柄交互（二）：物体选择 [XR Interaction Toolkit教程⭐三、实现抓取和交互功能 - 技术专栏 - Unity官方开发者社区](https://developer.unity.cn/projects/65769b7bedbc2a0026540012) 参考这里的抓取，这时候只能实现把物体抓到手上，要修改交互逻辑为，抓到手上之后，让其消失并触发增加玩家清理计数、播放音效、销毁垃圾对象等行为，可以为“垃圾”对象添加一个如下脚本：(将这个脚本放在GrabInteractor的selectExit 回调函数里，参考[Unity+Pico（五）：物体响应射线事件 - zero_to_infinity - 博客园](https://www.cnblogs.com/zerotoinfinity/p/17040306.html))
6. 现在实现的是一个可以走动和交互物品的系统，接下来要改变Canvas，变成可交互的，参考[XR Interaction Toolkit教程⭐四、实现与UI交互 - 技术专栏 - Unity官方开发者社区](https://developer.unity.cn/projects/65769b95edbc2a4da3d3edd3)
7. 首先更改场景1的设定：[Unity VR 开发教程 OpenXR+XR Interaction Toolkit (五) UI【旧版】unityvr开发教程-CSDN博客](https://blog.csdn.net/qq_46044366/article/details/127431250)  screen space-Camera的用处是，无论镜头如何变化，UI始终固定在和镜头相同的一个相对位置上。Plane Distance 默认为100，这时UI会被场景中的其他model遮盖，只需要将distance减小（>0）
8. 8. 注意修改完canvas之后，要修改player脚本对应的变量。
9. 游戏已经可以运行，但是头显的显示不是全景，且整体偏暗，来解决一下这里的问题
	1. 变暗: [关于Unity在游戏运行过程中切换场景导致场景变暗的问题_unity切换场景后变暗-CSDN博客](https://blog.csdn.net/weixin_61754136/article/details/133745394#:~:text=%E8%BF%99%E5%85%B6%E5%AE%9E%E6%98%AF%20Unity%20%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E7%9A%84%E5%8E%9F%E5%9B%A0%EF%BC%8C%E6%89%80%E4%BB%A5%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%E6%98%AF%E6%89%BE%E5%88%B0Window--Rendering--Lighting%E3%80%82%20%E4%BD%A0%E4%BC%9A%E7%9C%8B%E5%88%B0%E9%9D%A2%E6%9D%BF%E9%87%8C%E9%9D%A2%E6%9C%89%E4%B8%80%E4%B8%AAAuto%20Generate%E7%9A%84%E5%8B%BE%E9%80%89%E6%A1%86%EF%BC%8C%E5%A6%82%E6%9E%9C%E8%A2%AB%E5%8B%BE%E9%80%89%E5%88%99%E5%8F%96%E6%B6%88%E5%8B%BE%E9%80%89%EF%BC%8C%E6%9C%AA%E8%A2%AB%E5%8B%BE%E9%80%89%E5%B0%B1%E4%B8%8D%E7%94%A8%E7%90%86%E4%BC%9A%EF%BC%8C%E7%84%B6%E5%90%8E%E7%82%B9%E5%87%BB%E5%90%8E%E9%9D%A2%E7%9A%84Generate,Lighting%20%E6%8C%89%E9%92%AE%E3%80%82%20%E4%BD%A0%E4%BC%9A%E5%8F%91%E7%8E%B0%E5%9C%A8%E4%BD%A0%E7%9A%84%E5%9C%BA%E6%99%AF%20%E6%96%87%E4%BB%B6%E5%A4%B9%20%E9%87%8C%E9%9D%A2%E4%BC%9A%E7%94%9F%E6%88%90%E4%B8%80%E4%B8%AA%E6%96%87%E4%BB%B6%E5%A4%B9%EF%BC%8C%E6%96%87%E4%BB%B6%E5%A4%B9%E5%90%8D%E7%A7%B0%E5%B0%B1%E6%98%AF%E4%BD%A0%E5%BD%93%E5%89%8D%E5%9C%BA%E6%99%AF%E7%9A%84%E5%90%8D%E7%A7%B0%EF%BC%8C%E8%BF%99%E6%97%B6%E5%80%99%E5%B0%B1%E7%94%9F%E6%95%88%E4%BA%86%E3%80%82)
	2. 变暗+卡顿：[从零开始的PICO教程（2）--实时预览应用场景_pico unity integration sdk 开发-CSDN博客](https://blog.csdn.net/qq_51116518/article/details/131618613)
	3. 非全景：有待商讨
10. 接下来是打包，报错：you are missing the recommended jdk  [Unity防坑指南之Android路径缺失jdk、sdk和ndk+ndk版本问题（手动安装组件） - yansirfuture - 博客园](https://www.cnblogs.com/anderson0/p/16104174.html)
	- JDK：
	- SDK：[Android Studio安装详细教程（从下载到安装，保姆级教程）_android studio 国内下载-CSDN博客](https://blog.csdn.net/weixin_45143788/article/details/127498365)配合使用：[Unity 找不到 Android SDK 及编译失败的终极解决方案 | Iifa Tree](https://blog.iifatree.com/2021/01/10/unity-android-sdk/)
	- 打包：[6. 打包并运行场景 | PICO 开发者平台](https://developer-cn.picoxr.com/document/unity/build-and-run-the-scene/)
	最终这里的报错是把DNS设置成了114.114.114.114 然后直接在Hub重装了Unity
11.  **PlayerSettings->Active Input Handling is set to Both**：[创建Unity项目、Android打包和打包踩坑_playersettings->active input handling is set to bo-CSDN博客](https://blog.csdn.net/m0_71827731/article/details/144628266)
12. 加音乐最好把音频转换成ogg，避免因为音频文件存在一些作者属性信息而import失败