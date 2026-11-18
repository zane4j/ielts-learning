# MiniMax 官方 TTS｜雅思 Part 2 音频生成固定规范

[返回最小记忆量研究](README.md) · [25 篇英文原稿](ZOE_PHILIPPINES_25_TOPICS.md) · [仓库首页](../../../README.md)

> 这是当前有效的用户语音生成要求。以后新增或批量生成 Part 2 时均以本文件为准；如果有更新，以用户最后一次明确要求为准。

## 1. 音频内容和顺序（必须遵守）

1. **只朗读英语，不要任何中文语音**。文件名仍然使用中文。
2. 开头先朗读每篇原文中 `**Topic:**` 后面的**完整英文题目**（例如 `Describe a person who is good at learning languages.`），然后读该篇英文完整正文。
3. 英文题目读完后，约 **0.70 秒停顿**，再进入正文。正文的五个自然段顺序保持不变。
4. **不读** `INTRO / WHAT / WHY / HOW` 等标题、`Cue Card`、五行考场关键词、中文说明、共用故事标记，也不读 Markdown 的格式符号。
5. 不随意增删或改写英文原文；只有朗读控制标签用于停顿，不视为正文。

## 2. 男声、速度、自然度

| 项目 | 当前固定设置 |
| --- | --- |
| 调用方式 | GitHub Actions → 用户自己的 MiniMax 官方 API Key（GitHub Secret） |
| 模型 | `speech-2.8-hd` |
| 英文男声 | `English_Trustworthy_Man`，目标为自然北美职场口音，实际是否符合标准美式需听音频确认 |
| 语速 | `speed=0.85`（以前 0.78 太慢） |
| 英文题目后停顿 | `<#0.70#>` |
| 正文五段之间 | `<#0.50#>` |
| 句间停顿 | **仅依靠自然标点，不要在每句后插入固定停顿** |
| 风格 | 自然口语、连贯的语调、清晰的重音与弱读，适合 IELTS Speaking Part 2 / B1–B2 跟读及 Shadowing |
| 音频 | MP3、32 kHz、128 kbps、mono |

注意：模型数值语速不等于精确每分钟单词数，语气、重音和停顿自然度需根据试听反馈迭代，不能承诺已经完全改善。

## 3. MP3 中文命名（强制）

- 格式：`分类_两位序号_中文主题.mp3`。
- 分类使用：`人物类` / `事件类` / `物品类` / `地点类`。
- 用户指定的 P16 必须叫做 **`人物类_01_擅长学习语言的人.mp3`**。
- 其余人物题按现有 Markdown 出现顺序从人物类 02 开始；事件、物品、地点分别从 01 开始。
- 除 P16 的明确规范化名称外，中文主题保持与 Markdown 题名一致，仅用于文件名元数据；**绝不朗读中文题名**。
- 一篇对应一个独立 MP3，便于导入 iPhone 和逐篇跟读。

## 4. 执行、费用与安全

- 脚本：`scripts/minimax_part2_tts.py`；工作流：`.github/workflows/generate-ielts-audio.yml`。
- **每篇仅调用 MiniMax 一次**，输入是英文题目 + 原文五段英文正文，按原始字符计费。
- GitHub Secret `MINIMAX_API_KEY` 读取密钥；不写入源码、不打印 API Key 或全文。
- 国内 API Base 默认为 `https://api.minimaxi.com/v1`；国际版可在 Repository variables 中设置 `MINIMAX_API_BASE=https://api.minimax.io/v1`。
- Actions **只支持手动 `workflow_dispatch`**，不会因为 push 自动生成或扣费。
- `topic=P16` 用于单篇试听；`topic=all` 生成全部 25 篇（25 次付费调用）。
- 所有 MP3 打包为 GitHub Actions Artifact 下载（保留 7 天）；不会提交到公开 GitHub 仓库。
- 失败不自动重试，避免重复收费。下一次正式调用前，应先确认语速和听感。

## 5. 免费本地验证

```bash
python scripts/minimax_part2_tts.py --topic all --dry-run
```

`--dry-run` 检查 25 篇是否都能提取英文题目、5 段英文及对应中文文件名，不读取密钥、不请求 MiniMax、不收费。

## 6. 如何生成和下载

1. 进入仓库 [GitHub Actions 工作流](../../../.github/workflows/generate-ielts-audio.yml)。
2. 选择 **Run workflow**，输入 `P16` 或 `all`。
3. 运行结束，打开该次 Actions 运行记录，在 **Artifacts** 中下载 ZIP，解压获得中文命名的 MP3。

官方接口文档：https://platform.minimax.io/docs/api-reference/speech-t2a-http
