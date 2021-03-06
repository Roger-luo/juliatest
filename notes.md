# Problem E

## 水资源缺乏的原因

- 物理上的缺乏：某些地方本身水资源就少
- 经济上的缺乏：某些地方因为管理不善和缺乏基础设施而导致水资源缺乏

- 个人消费的增长
- 工业消费的增长
- 对清洁水的污染的增长

## 是否有可能为所有人提供干净的水？

- 物理上的可行性：
    + 自然水资源
    + 技术进步：脱盐工厂和雨水收集技术
- 理解水资源的补充是一个综合的问题
    + 环境的制约
    + 社会因素造成的水资源分布
    + 人类历史上是如何解决水资源匮乏的？
    + 地理(位置)，地志(地形)，生态
    + 如何精确预测未来水资源的储量
    + 新水源的可能性(脱盐工厂，雨水收集...)
    + 人口统计学和健康相关问题和水的关系

这些问题随着气候变化和人口增长而变得严重起来。

## Problem statement
- 建立一个模型能够评价某个地区满足其人口的供水能力，需要考虑：
    + 自然水资源的流动性对供给和需求的双重影响
- 使用UN的[水地图](http://www.unep.org/dewa/vitalwater/jpg/0222-
waterstress-overuse-EN.jpg)选一个水资源重度或中度超过负荷的国家或地区。
    + 解释为什么这个区域缺乏水资源。
    + 要确保考虑了由物理上和经济上所影响的社会和环境因素
- 在你所选的地区，应用你的模型来评价出未来15年内的水资源供给形势
    + 这个形势对所在地区的居民的影响是怎样的？
    + 确保模型中考虑到了环境驱动的影响
- 在你所选的区域，设计一个考虑所有水资源消耗的因素的介入方案。
    + 每个介入方案需要不可避免地影响到周边地区，甚至整个水生态系统。
    + 讨论这个影响，和介入方案的好处和坏处
    + 你的方案是如何减轻水资源匮乏的？
- 将你设计的介入方案应用后，该地区将来是否对水资源匮乏更不容易受到影响
    + 水资源是否会在将来某一个时间出现匮乏？如果会，请评估发生的时间
- 请写一个20页的报告，总结页不包括在内来解释你的模型，所选地区的水资源匮乏情况



The hydrologic cycle is simulated in a Python program. The cycle components are available water and unavailable water resident water cost industrial water cost and agricultural water cost.

The available water decreased when there are requests of water supply from industry, agriculture and residence.The unavailable water increases in the mean time.

There are some parameters that effects the three kinds of water costs.