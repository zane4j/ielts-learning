# Markdown 学习仓库维护规范

> 自 2026-11-18 起，仓库统一采用 **GitHub 原生 Markdown**。HTML / GitHub Pages 样式系统已弃用，旧版本仍可在 Git 历史中查看。

## 目录结构

- `README.md`：唯一顶层学习导航
- `speaking/README.md`：口语目录
- `speaking/part2/people/README.md`：Zoe 人物类 24 题入口与逐题定位
- `speaking/part2/people/IELTS_Part2_Zoe.md`：人物类最终定稿，不根据旧版 16 题或五段式自动改写
- `speaking/part2/places/README.md`：地点类 9 题与框架
- `speaking/part2/topics/README.md`：原有 54 题基线 Cue Card，和最终 Zoe 24 题不同
- `writing/README.md`、`writing/task1/README.md`：写作目录与批改资料

## 排版和跳转

1. 使用 Markdown 标题（`#`、`##`、`###`）、表格、列表、加粗和引用。**不创建 HTML 页面。**
2. 同一自然段内部不添加无意义硬换行；不同框架部分及视频例子需要分段时必须换行。
3. 每个专题的 `README.md` 必须链接到父目录/首页，并为本目录全部当前资料提供实际可用的相对路径链接。
4. 如果用户希望直接跳到某一道 Zoe 题，则使用当前文件内固定的 `zoe-topic-XX` 定位标识，不更改 24 道题的正文内容。
5. 维护英语学习资料时，尊重加粗含义。例如 Zoe 最终稿中的粗体是“本 Topic 新增或变化内容”，不能擅自解释为固定模板。
6. Writing 原稿和参考稿需要明确区分；原文缺失时不能编造。HTML 中的视觉色彩在 MD 不具有相同语义，要用文本说明和 Markdown 强调表达。

## 提交前

运行 `node scripts/check-markdown.mjs`；检查 Markdown 相对链接、Zoe 24 题稳定定位，以及是否误引入新的 HTML 页面。GitHub Actions 会执行相同验证。
