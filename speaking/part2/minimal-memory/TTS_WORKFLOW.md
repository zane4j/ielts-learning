# MiniMax 官方 API：雅思 Part 2 MP3

[返回最小记忆量研究](README.md) · [25 篇练习原稿](ZOE_PHILIPPINES_25_TOPICS.md) · [仓库首页](../../../README.md)

## P16 试听

- [GitHub Actions 工作流](../../../.github/workflows/generate-ielts-audio.yml)：在仓库顶部 Actions → Generate IELTS Part 2 MP3 (MiniMax) 中使用。
- 工作流第一次提交时会自动触发一次 P16 Demo，产生一次 MiniMax API 按量收费；此后可点击 Run workflow 手动生成。
- topic 默认 P16，也可输入其他题号，如 L08；输入 all 将生成全部 25 篇，产生 25 次单独计费请求。
- 运行结束后进入当前 Actions 运行页面，底部 Artifacts 下载 ielts-part2-mp3-P16 ZIP，里面是 P16.mp3，保留 7 天。
- 音频只上传 Actions Artifact，绝不提交 MP3 到代码仓库。25 篇原始 Markdown 不修改。

## API Key 设置

1. 仓库 Settings → Secrets and variables → Actions → Repository secrets 中创建 MINIMAX_API_KEY。
2. 国内版默认 API Base 为 https://api.minimaxi.com/v1。
3. 国际版 Key 在 Repository variables 中创建 MINIMAX_API_BASE，值为 https://api.minimax.io/v1。
4. GitHub Secret 只在生成步骤注入，控制台不打印密钥，也不打印正文。

## 默认语音参数

| 参数 | 值 |
| --- | --- |
| 模型 | speech-2.8-hd |
| 语音 | English_Trustworthy_Man，英语男声（美式口音待试听确认） |
| 语速 | 0.78 倍 |
| 句间停顿 | 0.20 秒 |
| 段落停顿 | 0.75 秒 |
| 音频格式 | MP3 / 32 kHz / 128 kbps |
| 输入 | 只提取五段英文正文，忽略标签、题卡与关键词 |

## 检查和排错

- 不花钱验证提取：python scripts/minimax_part2_tts.py --topic P16 --dry-run
- 如果缺少 MINIMAX_API_KEY，检查仓库 Secret 拼写。
- HTTP 401/403：检查账户地区、密钥权限和余额；在国际版账户设置对应的 MINIMAX_API_BASE。
- 出现 MiniMax API error code：查看具体的状态码，可能涉及音色或请求参数。
- 不自动重试失败调用，避免重复扣费；如需再次尝试，在 Actions 中手动重新运行。
- speed=0.78 是模型语速参数，不保证精确 110–125 WPM，需实际试听核验。

官方文档：https://platform.minimax.io/docs/api-reference/speech-t2a-http
