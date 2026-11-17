# S01｜生产故障排查：共用故事与 5 题适配

[返回首页](../../../README.md) · [事件类题卡](../topics/events/README.md) · [人物类题卡](../topics/people/README.md)

> 本页仅包含故事母版、替换句和替换后的故事，不包含完整回答的开头介绍或总结。Alex 是可替换的练习姓名；分工、对话及过程属于待你确认的练习设定，可按真实经历修改。

## 固定事实

同事 Alex 负责服务并主导 SQL 修复；你协助检查日志、定位慢请求；另一位同事准备测试。五题都保留这一分工：你帮助他定位，他完成关键修复，团队共同验证。人物题讲 Alex，不换成 Zoe。

## 故事母版

One evening, an application at work became unusually slow, and users started reporting problems. My colleague Alex was responsible for the service, so he asked me to help him investigate. The difficult part was finding the cause quickly while keeping the service running. Alex made a short checklist and divided the work: I checked the logs, he examined the database, and another colleague prepared the tests. I noticed that one request was taking much longer than usual and shared the details with him. Using that information, Alex found a database query that was reading far more data than necessary. He improved the query, and we tested the change together before releasing it. After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. We were all relieved that we had solved the problem without causing another one.

## 句子编号：便于只记修改处

**S1** One evening, an application at work became unusually slow, and users started reporting problems.

**S2** My colleague Alex was responsible for the service, so he asked me to help him investigate.

**S3** The difficult part was finding the cause quickly while keeping the service running.

**S4** Alex made a short checklist and divided the work: I checked the logs, he examined the database, and another colleague prepared the tests.

**S5** I noticed that one request was taking much longer than usual and shared the details with him.

**S6** Using that information, Alex found a database query that was reading far more data than necessary.

**S7** He improved the query, and we tested the change together before releasing it.

**S8** After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable.

**S9** We were all relieved that we had solved the problem without causing another one.

## 适配总览

| Topic | 故事重点 | 修改句子 |
| --- | --- | --- |
| E14 遇到的技术难题 | 难在哪里，以及如何定位原因 | S3、S6 |
| E12 团队合作经历 | 分工与合作带来的作用 | S4、S9 |
| E09 帮助别人的一次经历 | 同事需要帮助，你提供了什么帮助 | S2、S5 |
| P01 做成困难事情的人 | Alex 面对困难并成功完成修复 | S3、S7 |
| P03 有条理的人 | Alex 用清单、分工和检查顺序管理工作 | S4、S7 |

每题只替换两句，其余七句保持原样。下方完整故事中的**粗体**是替换句，方便对照；不是需要额外朗读的标记。

## E14｜遇到的技术难题

### 只改这两句

**S3 →** The difficult part was that several parts of the system could have caused the delay, so we had to check them one by one.

**S6 →** Using that information, Alex found a database query that was reading far more data than necessary, which explained the delay.

### 替换后的故事

One evening, an application at work became unusually slow, and users started reporting problems. My colleague Alex was responsible for the service, so he asked me to help him investigate. **The difficult part was that several parts of the system could have caused the delay, so we had to check them one by one.** Alex made a short checklist and divided the work: I checked the logs, he examined the database, and another colleague prepared the tests. I noticed that one request was taking much longer than usual and shared the details with him. **Using that information, Alex found a database query that was reading far more data than necessary, which explained the delay.** He improved the query, and we tested the change together before releasing it. After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. We were all relieved that we had solved the problem without causing another one.

## E12｜团队合作经历

### 只改这两句

**S4 →** Alex divided the work according to our strengths: I checked the logs, he examined the database, and another colleague prepared the tests.

**S9 →** Working together saved us time because we could investigate different parts of the problem at the same time.

### 替换后的故事

One evening, an application at work became unusually slow, and users started reporting problems. My colleague Alex was responsible for the service, so he asked me to help him investigate. The difficult part was finding the cause quickly while keeping the service running. **Alex divided the work according to our strengths: I checked the logs, he examined the database, and another colleague prepared the tests.** I noticed that one request was taking much longer than usual and shared the details with him. Using that information, Alex found a database query that was reading far more data than necessary. He improved the query, and we tested the change together before releasing it. After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. **Working together saved us time because we could investigate different parts of the problem at the same time.**

## E09｜帮助别人的一次经历

### 只改这两句

**S2 →** My colleague Alex was responsible for the service, but he was struggling to find the cause, so I offered to help.

**S5 →** I checked the logs, picked out the slow request, and explained what I had found so he could narrow down his search.

### 替换后的故事

One evening, an application at work became unusually slow, and users started reporting problems. **My colleague Alex was responsible for the service, but he was struggling to find the cause, so I offered to help.** The difficult part was finding the cause quickly while keeping the service running. Alex made a short checklist and divided the work: I checked the logs, he examined the database, and another colleague prepared the tests. **I checked the logs, picked out the slow request, and explained what I had found so he could narrow down his search.** Using that information, Alex found a database query that was reading far more data than necessary. He improved the query, and we tested the change together before releasing it. After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. We were all relieved that we had solved the problem without causing another one.

## P01｜做成困难事情的人

### 只改这两句

**S3 →** Alex was under a lot of pressure because he had to find the cause quickly while keeping the service running.

**S7 →** Despite the pressure, he stayed calm, improved the query, and made sure we tested the change carefully before releasing it.

### 替换后的故事

One evening, an application at work became unusually slow, and users started reporting problems. My colleague Alex was responsible for the service, so he asked me to help him investigate. **Alex was under a lot of pressure because he had to find the cause quickly while keeping the service running.** Alex made a short checklist and divided the work: I checked the logs, he examined the database, and another colleague prepared the tests. I noticed that one request was taking much longer than usual and shared the details with him. Using that information, Alex found a database query that was reading far more data than necessary. **Despite the pressure, he stayed calm, improved the query, and made sure we tested the change carefully before releasing it.** After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. We were all relieved that we had solved the problem without causing another one.

## P03｜有条理的人

### 只改这两句

**S4 →** Alex made a clear checklist, gave each of us a task, and kept track of what we had checked: I handled the logs, he examined the database, and another colleague prepared the tests.

**S7 →** He improved the query and followed his checklist, making sure we completed the tests before releasing the change.

### 替换后的故事

One evening, an application at work became unusually slow, and users started reporting problems. My colleague Alex was responsible for the service, so he asked me to help him investigate. The difficult part was finding the cause quickly while keeping the service running. **Alex made a clear checklist, gave each of us a task, and kept track of what we had checked: I handled the logs, he examined the database, and another colleague prepared the tests.** I noticed that one request was taking much longer than usual and shared the details with him. Using that information, Alex found a database query that was reading far more data than necessary. **He improved the query and followed his checklist, making sure we completed the tests before releasing the change.** After the update, the application responded much faster, and we continued monitoring it to make sure it stayed stable. We were all relieved that we had solved the problem without causing another one.

