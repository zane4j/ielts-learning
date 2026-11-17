# S01｜生产故障排查：口语母版与 5 题适配

[返回首页](../../../README.md) · [事件类题卡](../topics/events/README.md) · [人物类题卡](../topics/people/README.md)

> 仅故事部分。Alex 为可替换的练习姓名；角色和细节请按真实经历调整。分工保持一致：你查日志并找到线索，Alex 优化查询，两人共同测试。

## 记忆线索：五个画面

**变慢 → 分工 → 定位 → 优化上线 → 恢复正常**

英文关键词：**slow → logs / database → slow request / query → optimize / test / deploy → normal**。

## 故事母版

One evening, our app suddenly became really slow, and users started reporting problems.  
My colleague Alex was responsible for the service, so I helped him **look into it**.  
At first, we were not sure what was wrong, and we had to keep the app running.  
Alex made a quick plan: I **checked the logs** while he looked at the database.  
I found a slow request, and that helped us **troubleshoot the problem**.  
**It turned out that** one query was reading far more data than it needed.  
Alex **optimized the query**, and we **tested the fix** together before **deploying it**.  
After that, the **response time dropped**, and everything was back to normal.

## 分块记忆

| 画面 | 句子 | 记忆重点 |
| --- | --- | --- |
| 变慢 | S1–S3 | 用户反馈问题，我帮 Alex；排查时服务必须继续运行 |
| 分工 | S4 | 我查日志，他查数据库 |
| 定位 | S5–S6 | 慢请求 → 查询读取过多数据 |
| 优化上线 | S7 | optimize → test → deploy |
| 恢复正常 | S8 | 响应变快，恢复正常 |

**S1** One evening, our app suddenly became really slow, and users started reporting problems.

**S2** My colleague Alex was responsible for the service, so I helped him look into it.

**S3** At first, we were not sure what was wrong, and we had to keep the app running.

**S4** Alex made a quick plan: I checked the logs while he looked at the database.

**S5** I found a slow request, and that helped us troubleshoot the problem.

**S6** It turned out that one query was reading far more data than it needed.

**S7** Alex optimized the query, and we tested the fix together before deploying it.

**S8** After that, the response time dropped, and everything was back to normal.

## 5 个 Topic：每题只替换一句

其余七句保持不变。下方粗体为替换句。

### E14｜遇到的技术难题

**替换 S3：** The tricky part was finding the root cause without taking the service offline.

One evening, our app suddenly became really slow, and users started reporting problems. My colleague Alex was responsible for the service, so I helped him look into it. **The tricky part was finding the root cause without taking the service offline.** Alex made a quick plan: I checked the logs while he looked at the database. I found a slow request, and that helped us troubleshoot the problem. It turned out that one query was reading far more data than it needed. Alex optimized the query, and we tested the fix together before deploying it. After that, the response time dropped, and everything was back to normal.

---

### E12｜团队合作经历

**替换 S4：** We split the work to save time: I checked the logs while Alex looked at the database.

One evening, our app suddenly became really slow, and users started reporting problems. My colleague Alex was responsible for the service, so I helped him look into it. At first, we were not sure what was wrong, and we had to keep the app running. **We split the work to save time: I checked the logs while Alex looked at the database.** I found a slow request, and that helped us troubleshoot the problem. It turned out that one query was reading far more data than it needed. Alex optimized the query, and we tested the fix together before deploying it. After that, the response time dropped, and everything was back to normal.

---

### E09｜帮助别人的一次经历

**替换 S2：** My colleague Alex was struggling to find the cause, so I offered to help him check the logs.

One evening, our app suddenly became really slow, and users started reporting problems. **My colleague Alex was struggling to find the cause, so I offered to help him check the logs.** At first, we were not sure what was wrong, and we had to keep the app running. Alex made a quick plan: I checked the logs while he looked at the database. I found a slow request, and that helped us troubleshoot the problem. It turned out that one query was reading far more data than it needed. Alex optimized the query, and we tested the fix together before deploying it. After that, the response time dropped, and everything was back to normal.

---

### P01｜做成困难事情的人

**替换 S7：** Even under pressure, Alex stayed calm, optimized the query, and made sure we tested the fix before deploying it.

One evening, our app suddenly became really slow, and users started reporting problems. My colleague Alex was responsible for the service, so I helped him look into it. At first, we were not sure what was wrong, and we had to keep the app running. Alex made a quick plan: I checked the logs while he looked at the database. I found a slow request, and that helped us troubleshoot the problem. It turned out that one query was reading far more data than it needed. **Even under pressure, Alex stayed calm, optimized the query, and made sure we tested the fix before deploying it.** After that, the response time dropped, and everything was back to normal.

---

### P03｜有条理的人

**替换 S4：** Alex made a checklist and gave us clear tasks: I checked the logs while he looked at the database.

One evening, our app suddenly became really slow, and users started reporting problems. My colleague Alex was responsible for the service, so I helped him look into it. At first, we were not sure what was wrong, and we had to keep the app running. **Alex made a checklist and gave us clear tasks: I checked the logs while he looked at the database.** I found a slow request, and that helped us troubleshoot the problem. It turned out that one query was reading far more data than it needed. Alex optimized the query, and we tested the fix together before deploying it. After that, the response time dropped, and everything was back to normal.

## 工作表达：按短语记忆

| 表达 | 含义 |
| --- | --- |
| look into it | 排查一下 |
| check the logs | 查看日志 |
| troubleshoot the problem | 排查问题 |
| It turned out that… | 后来发现…… |
| optimize the query | 优化查询 |
| test the fix | 测试修复方案 |
| deploy the fix | 部署修复 |
| response time | 响应时间 |
| root cause | 根本原因 |
| take the service offline | 将服务下线 |

**背诵方法：** 先只看五个画面复述，再补每块的一两句。尤其把“查日志 → 找慢请求 → 定位查询”当成因果链记，不用逐词死背。optimize 在过去的故事中用 **optimized**。

本版保留完整工作过程，用口语连接句和常用技术词表达。它仍然只是故事主体；完整回答需结合题卡补充必要背景、原因和感受。
