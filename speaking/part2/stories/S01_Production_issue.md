# S01｜生产故障排查：口语精简版

[返回首页](../../../README.md) · [事件类题卡](../topics/events/README.md) · [人物类题卡](../topics/people/README.md)

> 仅故事部分，不是完整 Part 2 回答。Alex 为练习姓名，角色与过程可按真实经历调整。统一分工：你查日志、提供线索；Alex 定位并修复数据库查询；你们共同测试。此精简版省略第三位同事的次要细节。

## 先记这条线索

**慢 → 帮 → 分 → 找 → 改 → 测 → 好**

系统变慢 → 帮助同事 → 分工排查 → 找到线索 → 修改查询 → 测试发布 → 恢复正常。

英文关键词：**slow → help → plan → spot → change → test → normal**。

## 故事母版

One evening, our app suddenly became really slow. My colleague Alex was in charge, so I helped him look into it. He made a quick plan: I checked the logs, and he checked the database. I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. The app was back to normal, and we all felt relieved.

## 一句对应一个画面

| 线索 | 句子 |
| --- | --- |
| S1 · 慢 | One evening, our app suddenly became really slow. |
| S2 · 帮 | My colleague Alex was in charge, so I helped him look into it. |
| S3 · 分 | He made a quick plan: I checked the logs, and he checked the database. |
| S4 · 找 | I spotted a slow request, which helped him find the problem. |
| S5 · 改 | A database query was doing too much work, so he changed it. |
| S6 · 测 | We tested the fix together and then released it. |
| S7 · 好 | The app was back to normal, and we all felt relieved. |

## 5 个 Topic：每题只替换一句

其余六句不变。先熟悉母版，再记各题重点：**难题＝查原因；团队＝分工有效；帮助＝主动帮忙；成功的人＝顶住压力；有条理＝清单分工**。

### E14｜遇到的技术难题

**只替换 S2：** We didn't know what was causing the delay, so Alex and I checked things step by step.

One evening, our app suddenly became really slow. **We didn't know what was causing the delay, so Alex and I checked things step by step.** He made a quick plan: I checked the logs, and he checked the database. I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. The app was back to normal, and we all felt relieved.

---

### E12｜团队合作经历

**只替换 S7：** The app was back to normal, and sharing the work had helped us solve the problem faster.

One evening, our app suddenly became really slow. My colleague Alex was in charge, so I helped him look into it. He made a quick plan: I checked the logs, and he checked the database. I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. **The app was back to normal, and sharing the work had helped us solve the problem faster.**

---

### E09｜帮助别人的一次经历

**只替换 S2：** Alex was stuck and looked worried, so I offered to check the logs for him.

One evening, our app suddenly became really slow. **Alex was stuck and looked worried, so I offered to check the logs for him.** He made a quick plan: I checked the logs, and he checked the database. I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. The app was back to normal, and we all felt relieved.

---

### P01｜做成困难事情的人

**只替换 S2：** Alex was under pressure to fix it quickly, but he stayed calm and asked me to help.

One evening, our app suddenly became really slow. **Alex was under pressure to fix it quickly, but he stayed calm and asked me to help.** He made a quick plan: I checked the logs, and he checked the database. I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. The app was back to normal, and we all felt relieved.

---

### P03｜有条理的人

**只替换 S3：** Alex made a checklist and gave us clear tasks: I checked the logs, and he checked the database.

One evening, our app suddenly became really slow. My colleague Alex was in charge, so I helped him look into it. **Alex made a checklist and gave us clear tasks: I checked the logs, and he checked the database.** I spotted a slow request, which helped him find the problem. A database query was doing too much work, so he changed it. We tested the fix together and then released it. The app was back to normal, and we all felt relieved.

## 怎么背更轻松

1. 先只看“慢、帮、分、找、改、测、好”，用中文复述整个过程。
2. 再用英文关键词讲，每个关键词带出一句，不要求每次逐字相同。
3. 母版熟悉后，每次抽一个 Topic，只换对应的一句。

保留自然短语：**look into it**（查一查原因）、**spotted a slow request**（发现一个慢请求）、**back to normal**（恢复正常）、**felt relieved**（松了口气）。不必进一步解释 SQL 或数据库内部原理。

本版缩短的是故事主体。完整回答仍需结合具体题卡补充人物／时间／地点和题目要求的原因、感受，不能把这段短故事直接当作整篇两分钟回答。
