# MiniMax 官方 API：雅思 Part 2 中英双语 MP3

[返回最小记忆量研究](README.md) · [25 篇练习原稿](ZOE_PHILIPPINES_25_TOPICS.md) · [仓库首页](../../../README.md)

## 当前规则（2026-11-18）

- 开头先以普通话男声朗读中文主题，如“擅长学习语言的人。”，短暂停顿 0.65 秒，然后以英文男声朗读五段完整英文。
- 英文音色：English_Trustworthy_Man，模型 speech-2.8-hd，speed=0.85（上一版为 0.78）。
- 为改善机械感，不再在每个英文句号后额外插入 0.20 秒停顿，仅依靠标点自然停顿；五段之间额外停顿 0.50 秒（上一版 0.75 秒）。
- 中文主题使用 MiniMax 官方中文男声音色 male-qn-qingse，speed=1.0；使用 ffmpeg 将两段 MP3 及短静音拼成一个文件。
- 因中文和英文分别使用两个音色，每篇有 **2 次 MiniMax 按量计费调用**。预估费用按总输入字符计，不是原本单次调用。
- GitHub Actions Artifact 提供 ZIP 下载，默认保留 7 天；不会把音频提交到仓库。

## 命名规则

- 文件名为 分类_两位序号_中文主题.mp3。
- **明确指定 P16 为人物类第 01 篇**，因此 P16 的完整名称为 人物类_01_擅长学习语言的人.mp3。
- 其余人物题从人物类_02 起，按原 25 题 Markdown 出现顺序编号；事件类、物品类、地点类各从 01 开始。
- 中文题目大体沿用原 Markdown 的标题，P16 按指定用语由“擅长学语言的人”规范为“擅长学习语言的人”；只调整语音标题和文件名，不修改原文。

## 运行与秘钥

1. 在 GitHub 仓库的 Settings → Secrets and variables → Actions → Repository secrets 中保存 MINIMAX_API_KEY。
2. 国内版使用默认 https://api.minimaxi.com/v1；若 API Key 来自国际版，在 Repository variables 中保存 MINIMAX_API_BASE=https://api.minimax.io/v1。
3. 进入仓库 Actions → Generate IELTS Part 2 MP3 (MiniMax) → Run workflow，填 P16 试听或 all 生成全部。
4. 进入运行记录底部 Artifacts 下载 ielts-part2-mp3-P16，解压后得到对应的中文主题命名 MP3。
5. 本次工作流更新的 push 触发器会自动生成一份 P16 测试音频；若进一步关闭此自动触发，以后只能手动运行，避免无意再次付费。

## 无需付费的测试

```bash
python scripts/minimax_part2_tts.py --topic all --dry-run
```

该命令检查 25 题正文解析和中文 MP3 文件名，不需要 API Key，不发起 TTS 请求。

## 错误排查

- HTTP 401/403：检查 Key、国家地区、余额与模型授权。
- 中文标题朗读失败：核实 male-qn-qingse 音色与当前模型可用性；这时不会调用英文正文。
- 英文正文朗读失败：中文标题请求可能已经计费，但不会自动重试。
- ffmpeg 必须可用；预先验证其存在后才进行付费 API 请求。
- 0.85 仅为 MiniMax speed 参数，不保证固定 WPM 或完美口音与自然度；请以实际试听为准。

官方文档：https://platform.minimax.io/docs/api-reference/speech-t2a-http
