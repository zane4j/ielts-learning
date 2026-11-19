# IELTS Speaking Part 1 · 40 Topics

[返回口语目录](../README.md) · [返回首页](../../README.md)

根据 `IELTS_SPEAKING_Zane.xlsx` 的 `Part1` 工作表整理：

- **40 个 Topic / 197 组完整 Question–Answer**，每个 Topic 一个 MP3。
- 使用此前**已经生成**的 HeyGen 音频链接，不重新生成音频，也不需要 API Key。
- 朗读顺序：**Topic 标题 → 较长停顿 → Question → 停顿 → Answer**，依次读完每个 Topic 的所有问答。
- 美式英语男声，按 Excel 原文朗读；原文未进行语法批改。
- [40 个 MP3 音频链接及题量清单](heygen_audio_40.csv)。

## 使用 GitHub Actions 一键下载与打包

1. 进入 **[Download HeyGen IELTS Part 1 (40 MP3)](https://github.com/zane4j/ielts-learning/actions/workflows/download-heygen-part1.yml)**。
2. 点击 **Run workflow**，分支选 `main`，然后运行；也会在首次提交工作流时自动触发。
3. 等待执行结果为绿色 **Success**。
4. 打开对应运行记录，找到页面底部的 **Artifacts**，下载 **`ielts-part1-40-mp3`**。
5. 下载的是 GitHub Actions 的外层 ZIP，解压后得到 **`IELTS_Part1_40_Topics_MP3.zip`**；再次解压可得到 40 个 MP3（按 `01_Work.mp3` ... `40_Science.mp3` 排序）。

> GitHub 的 Workflow Artifacts 通常需要登录才能下载；下载链接会受 Artifacts 保留期限限制。本工作流设为 **14 天**。

## 技术实现

- [下载、校验和 ZIP 打包 Python 脚本](../../scripts/download_heygen_part1.py)
- [GitHub Actions 工作流](../../.github/workflows/download-heygen-part1.yml)
- 标准库实现，最多 4 路并发下载；支持 HTTP 错误重试与超时。
- 校验全部 40 个文件的 MP3 文件头、大小及（安装 ffprobe 时）音频时长，并检查 ZIP 完整性。
- **任一 Topic 下载失败即执行失败，不生成不完整压缩包。**
- 音频由 HeyGen 托管，若原地址过期或访问受限，须更新清单中的对应音频链接。

本地验证（不下载）：

```bash
python3 scripts/download_heygen_part1.py --dry-run
```

本地下载和打包：

```bash
python3 scripts/download_heygen_part1.py
```

输出：`dist/IELTS_Part1_40_Topics_MP3.zip`。
