# Zoe Part 2 · HeyGen 24 题音频

[返回人物类目录](README.md) · [返回首页](../../../README.md)

**用途：** 从已经生成好的 HeyGen 在线 MP3 地址下载 24 道 IELTS Speaking Part 2 音频，并在 GitHub Actions 中校验和打包为 ZIP。**不会重新合成语音，不需要 HeyGen API Key。**

## 在 GitHub 上一键打包

1. 进入 [Actions — Download HeyGen IELTS Part 2 (24 MP3)](https://github.com/zane4j/ielts-learning/actions/workflows/download-heygen-part2-24.yml)。
2. 点击 **Run workflow**，分支选择 `main`，再次点击 **Run workflow**。
3. 等工作流成功结束，打开这次运行详情。
4. 在页面底部 **Artifacts** 下载 `IELTS-Part2-Zoe-24-MP3`。
5. GitHub 下载的 Artifact 自身是一个 ZIP；打开后，其中的 `IELTS_Part2_Zoe_24_MP3.zip` 才是包含 **24 个 MP3 文件**的离线压缩包。

## 文件说明

- [音频元数据（24 条）](heygen_audio_24.json)：编号、中文 MP3 文件名和 HeyGen 地址。
- [下载脚本](../../../scripts/download_heygen_part2.py)：同时下载最多四段，失败重试，校验 MP3，构建 ZIP 并检查 CRC。
- [Actions 工作流](../../../.github/workflows/download-heygen-part2-24.yml)：仅手动触发，成功后将 ZIP 保存为 Artifact **7 天**。
- [Zoe 24 题英文原稿](IELTS_Part2_Zoe.md)：每篇音频包含英文题目和完整英文答案，**不朗读中文题目**。

## 如果运行失败

- HTTP 403 / 404：HeyGen 在线链接可能失效或访问受限，需要更新链接清单，不能仅重复运行来解决。
- 网络超时、HTTP 429 / 5xx：脚本会自动重试临时错误，仍失败则显示失败题目。
- 不会上传不完整 ZIP；只有 24 个 MP3 全部验证成功后才会上传 Artifact。
- 仓库是**公开的**，因此清单中的音频直链也公开。若需要保持链接私密，应改为私有仓库或将清单移入 GitHub Secrets。

## 本地运行（可选）

```bash
python3 scripts/download_heygen_part2.py
```

本地生成：`dist/IELTS_Part2_Zoe_24_MP3.zip`。
