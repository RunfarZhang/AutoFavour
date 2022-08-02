# AutoFavour
知识星球圈子文章自动点赞

# README
power by RunfarZhang
* 初始代码源自B站UP：不高兴就喝水，视频地址：https://www.bilibili.com/video/BV1T34y1o73U?is_story_h5=false&p=1&share_from=ugc&share_medium=android&share_plat=android&share_session_id=1eefde79-c281-4c2a-a1d6-4266d9c60e4f&share_source=WEIXIN&share_tag=s_i&timestamp=1659406747&unique_k=C4gH42B
* 对其源码略作修改，完成了特定任务。
## 使用指南
* 举例：使用360极速浏览器，对标签栏-知识星球的指定圈子内问政进行自动点赞
### 0、重要目录及文件
1. autogui.py: 主程序入口
2. cmd1.xlsx：自动化任务流程表
3. into_starts: 自动化任务图标存放位置
### 1. 截取图标，完成匹配
* 1. 截取360极速浏览器图标（未点击状态）放入.\into_stars\
* 2. 截取浏览器标签栏知识星球图标放入.\into_stars\
* 3. 截取指定星球圈子图标（未点击状态）放入.\into_stars\
* 4. 截取未点赞图标放入.\into_stars\
### 2. 修改cmd1.xlsx，编写自动化流程
* 1. 匹配浏览器并点击
* 2. 匹配标签栏知识星球标签并点击
* 3. 匹配指定圈子并点击
* 4. 滚动并点击未点赞的图标（循环动作）
### 3. 运行
```
python autogui.py
```