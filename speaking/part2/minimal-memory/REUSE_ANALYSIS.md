# Zoe Part 2 · 文案复用率审计（V0.3）

[返回研究目录](README.md) · [现有完整稿和增量句](CREATIVE_VARIANTS.md) · [54 题候选矩阵](COVERAGE_MATRIX.md) · [Zoe 最终 24 题](../people/IELTS_Part2_Zoe.md)

> **结论：**目前可以证明的只是：P16 与 P01 两篇 201 / 191 词完整稿在有序词汇层面重合约 55%–58%，但**完全相同的完整句子数为 0**。因此应统一核心故事的英文措辞，再单独准备 Topic 专属句，而不是每道题改写同一经历的每一句。

## 1. 分析范围与统计方法

数据来自本目录 [CREATIVE_VARIANTS.md](CREATIVE_VARIANTS.md)：**P16**「擅长学语言」、**P01**「做成困难的事情」两个已经完整写出的三段式答案，以及下面六个 Topic 的差异句。分析只计算英文朗读正文，排除 Markdown 标题、中文解释、关键词、题卡和 1 分钟准备提示。

- **英文单词数：**统一转小写后用英文词正则（带撇号的缩略词视作 1 词）计数。
- **整句精确复用率：**按 `.` / `?` / `!` 切分句子，比较句子完整原文是否相同；不把“同义改写”视作完全复用。
- **有序词汇复用率（LCS）：**两篇文章在保持出现顺序前提下能匹配的最多词数 ÷ 每篇总词数。它允许词语不连续，也会匹配 the / I / to 等普通词，因此反映文本相似度的**上限式代理指标**，不能直接解释为“已经背会多少内容”。
- **增量模块：**计算已写出的六题差异句，**不是**六篇完整 Part 2 答案，不可与完整稿直接比较整体复用率。
- **候选覆盖率：**V0.2 的 4 个 S + 20 个 M = 24 / 54 ≈ 44.4% 为“可能串题方向”，**不是已验证的完整稿覆盖率**。

## 2. 已写完的两篇：实际文本重合

| 指标 | P16 擅长语言 | P01 困难成就 |
| --- | ---: | ---: |
| 英文词数 | **201** | **191** |
| 英文自然段数 | 7 | 7 |
| 英文句数 | 9 | 11 |
| 完整相同的句子数 | **0** | **0** |
| 两篇最长有序公共词序列 | 110 词 | 110 词 |
| **LCS / 本篇词数** | **54.7%** | **57.6%** |

**解读：**两篇的主题内容高度关联，但逐句写法已经变了：

- P16：`She tries to create an immersive English-speaking environment by watching English videos, speaking with foreigners and using English in her daily life.`
- P01：`Instead of giving up, she created an immersive English-speaking environment. She watched English videos, spoke English every day and kept practising even when she made mistakes.`

这两种表达含义相近，但训练者仍需背不同语序、时态和连接方式。如果目标是最少记忆，应挑**一套固定说法**同时用于两个主题。

## 3. 六道题的现有差异模块

| Topic | 已写新增句数 | 英文单词数 | 功能 |
| --- | ---: | ---: | --- |
| P03 有条理 | 2 | 21 | 计划与进度 |
| P08 教新技能 | 2 | 28 | 教学和实践 |
| P09 受欢迎 | 1 | 18 | 观众喜爱原因 |
| P05 年长者 | 1 | 17 | 年龄与欣赏 |
| E16 改变观点 | 2 | 31 | 旧观点与新观点 |
| O03 有趣视频 | 1 | 20 | 视频内容与兴趣 |
| **合计** | **9** | **135** | **平均每道题 22.5 词** |

注意，这 135 词是**已经写出的差异句总量**，并非写完这六篇的全部额外词量，也不等于只需再背 135 词就能应对六题。尚需将每题的固定母版、不同题卡要求、自然衔接和实际时长整合验证。

## 4. 建议的低记忆成本结构

把英语环境故事拆成 **公共 CORE + 三个可切换的开头/结尾**：

### CORE：每次一字不变的 6 个故事句（研究用稿，非原定稿）

> At first, she wasn't confident speaking English, especially when talking to foreigners.
>
> Instead of giving up, she decided to create an immersive English-speaking environment.
>
> She watched English videos, practised speaking every day and tried to use English whenever she could.
>
> After several months, she made significant progress and became much more confident.
>
> Later, she shared her learning experience in a travel video, which left a deep impression on me.
>
> At that time, I was considering quitting my job to go to the Philippines to study English, but I was afraid of losing my stable income.

**使用策略：**不同题目尽量保持这六句逐字不变，避免反复把 `tries to create` 改成 `created`，把 `speaking with foreigners` 改成 `talking to foreigners`。只调整标题之外的少量重点句：

| 题目 | WHAT 要强调 | WHY 要强调 |
| --- | --- | --- |
| P16 擅长语言 | 沉浸式学习的原理、交流进步 | 方法对我的帮助 |
| P01 困难成就 | 从害怕说英语到能交流 | 不放弃和努力 |
| P03 有条理 | 每天明确的时间表 | 有计划才能坚持 |
| P08 教技能 | Zoe 教我如何跟读/录音 | 我如何实践及进步 |
| P09 受欢迎 | 她向观众分享学习方法 | 内容让人有共鸣 |
| E16 改变观点 | 我的旧想法与新想法 | 为什么我重新考虑去菲律宾 |
| O03 有趣视频 | 视频内容和观看时间 | 为什么吸引并启发我 |

### 句子使用原则

1. **故事正文优先固定**，不要只固定 INTRO/WHY 的万能连接词。
2. 原始母版一旦确定，以后的变体只替换 **WHAT 主题句、1–3 个不可缺的题卡事实、WHY 结论**。
3. 新增模块尽量在 **15–35 英文词**内完成；这是建议的练习预算，不是测得的实际平均值。
4. 目标可以设为 **70% 以上连续可直接背诵的英文内容**，但只是下一版的设计目标，**当前两个完整稿未达到这个标准**；必须写完后重新实测。
5. 如果为强行达到复用比例而漏答题卡，则宁愿增加几句，也不要把失焦答案当成串题成功。

## 5. 优化优先级与下一次审计

1. 先以 P16 / P01 两篇为样本，选定统一 CORE 并生成 **完全一致**的故事正文。
2. 先补全 P03、P08、P09 三篇人物类全文，再计算每篇**逐字固定句占比**和 WORD LCS，相比只算有相似单词更接近记忆成本。
3. 再补 E16、O03 两篇跨类话题，防止把人物故事机械移植到第一人称决定 / 视频题。
4. 必须进行 90–120 秒模拟口述，分别核对 cue card 的全部要素；重复句不是越多越好。
5. 对其余 V0.2 候选项继续单独报告“完整写作状态、复用率、新增词数、扣题状态”，不要以 **24 / 54** 代替已经测出的文本复用率。

> **重要限定：**本研究允许为 IELTS 练习设计 Zoe 的经历；但「Zoe 学英语取得成功」等仍然是**创意素材设定**。本目录不修改用户已确认的正式 Zoe 24 题稿件。
