---
name: seedance-prompt
description: "将剧本、小说或分镜脚本转化为即梦Seedance 2.0视频提示词。当用户需要：(1) 将剧本/小说/分镜脚本转为AI视频提示词 (2) 生成Seedance 2.0可用的镜头描述 (3) 切分视频片段并生成prompt时触发。"
---

# 即梦Seedance 2.0 视频提示词生成器

将剧本、小说或分镜脚本转化为结构化脚本片段和Seedance 2.0可用提示词。

## 核心概念

- **片段（Segment）**：AI输出的基本单位，包含1个或多个镜头，总时长不超过15秒
- **镜头（Shot）**：单个镜头画面，1-8秒
- **资产引用**：在画面描述中自然引用，使用 @资产名 格式，每个引用后加空格
- **场景转换**：必须切换到新的片段

## 输入处理

接收用户输入的剧本内容，自动执行以下分析：

1. **全局视觉风格提炼**
   - 美术风格：古风写实/赛博朋克/现代都市/奇幻/东方科幻等
   - 摄影调性：暗调/高调/低饱和度/高饱和度等
   - 光源设定：月光/霓虹灯/自然光/暖光/冷光等
   - 情绪氛围：悬疑/温情/紧张/速度感/科技感等

2. **脚本片段切分规则**
   - 单个镜头：1-8秒
   - 每个片段最长15秒（尽量安排接近15秒）
   - 台词时长计算：中文约150字/分钟
   - 智能切分原则：
     1. **场景切换必须分段**（第一优先级）
     2. 情绪转折点可分段
     3. 保持叙事完整性
     4. 单片段多镜头时合理分配时长（不平均分配，根据内容需要）

## 输出格式（无空行）

```
视觉风格 [风格关键词，逗号分隔]

片段X [总时间段] 包含N个镜头
[镜头1: 时间段] 中文画面描述，@资产1 @资产2 自然分布在描述中，资产引用后加空格
[镜头2: 时间段] 中文画面描述，@资产3 自然分布在描述中

片段Y [总时间段] 包含N个镜头
[镜头1: 时间段] 中文画面描述，@资产4 @资产5 自然分布在描述中
```

## Seedance Prompt 结构规范

按以下顺序组织提示词，用逗号分隔，不分段：

1. **镜头语言**：景别 + 镜头运动
2. **主体描述**：角色外貌（必须全局一致）+ 当前动作 + 表情
3. **场景环境**：地点特征 + 背景细节 + 光源（具体描述）
4. **视觉风格**：美术风格 + 摄影调性 + 色调
5. **氛围关键词**：情绪词 + 电影参考（可选）
6. **技术参数**：cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading

## 景别术语

Extreme Wide Shot (EWS) / 大远景, Wide Shot (WS) / 远景, Full Shot (FS) / 全景, Medium Shot (MS) / 中景, Medium Close-Up (MCU) / 中近景, Close-Up (CU) / 特写, Extreme Close-Up (ECU) / 大特写

## 镜头运动术语

static shot（固定）, push in / dolly in（推）, pull out / dolly out（拉）, pan left/right（摇）, follow shot / tracking shot（跟）, crane up / elevating shot（升）, crane down / descending shot（降）, orbit / circling around（环绕）

## 竖屏构图要求

9:16比例时强调：vertical composition, centered or lower third composition, background layers

## 技术参数固定标签

每个prompt末尾添加：cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading

## 示例

**输入：**
```
夕阳下，一个穿黑色风衣的男人走进老旧的咖啡馆。他点了杯咖啡，望向窗外的雨景。
```

**输出：**
```
视觉风格 赛博朋克, 暗调, 低饱和度, 冷光, 悬疑

片段1 [0-8s] 包含2个镜头
[镜头1: 0-4s] MCU, push in, 一个穿黑色风衣的男人走在湿漉漉的街道上，@男人 面部冷峻，眼神警惕，油灯暖光从右侧打来，赛博朋克风格，暗调摄影，霓虹色调，cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading
[镜头2: 4-8s] WS, static shot, @男人 推开咖啡馆的木门，@咖啡馆 内烟雾缭绕，复古装潢与霓虹灯交织，冷色调光源，赛博朋克氛围，cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading

片段2 [8-15s] 包含2个镜头
[镜头1: 8-11s] MCU, follow shot, @男人 坐在吧台前，@咖啡师 递来一杯咖啡，@男人 手指轻敲吧台，表情沉思，台灯暖光从左侧打来，cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading
[镜头2: 11-15s] MCU, pull out, @男人 转头望向窗外，@雨景 细雨蒙蒙，霓虹灯光在玻璃上折射，冷色调主导，忧郁悬疑氛围，cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading
```

## 注意事项

- 角色外貌描述必须在每个镜头prompt中完整重复，确保一致性
- 不要在prompt中写对白文字，对白通过后期字幕处理
- 光源描述要具体（如：warm oil lamp glow from右侧），不要用模糊词
- 避免复杂多人互动，单镜头人物不超过2人（根据剧情最多9人）
- 每条EN Prompt控制在120词以内
- 资产引用格式：@资产名，**仅在首次出现时引用**，后续自然衔接不重复引用
- **禁止使用你我他/她/它等人称代词**，必须使用 @资产 格式指定
- **场景转换必须切换新的片段**
