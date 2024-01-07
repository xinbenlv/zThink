---
title: "5 steps to perform code reviews at Google"
date: 2013-11-19
categories:
  - blog
tags:
  - Jekyll
  - update
---

By <span class="GINGER_SOFTWARE_mark" id="18c826de-f1bc-4226-9c97-cf28ed136b63">Zainan Victor Zhou</span> 2013-11-19

<strong>Step 1: pre-screen</strong>

<strong>Size</strong>: The first step of a code review is to glance at the change list and check if the change list is in a reasonable size. Typically, a change list of 300 lines of code is a reasonable size. Unless necessary, larger size of code should be strongly discouraged. A Large size CL should be broken down into smaller CLs, but logically complete part. Leave a quick comment to the CL author asking possibility of breaking down or reason for not breaking down. On the other hand, a small CL as small as only online. It is OK to review small CL as long as it is logically complete.

<strong>Right person</strong>: Also, ask yourself if you are the appropriate person to review this change list. If you are not familiar enough with the updated code, or you are not savvy enough to understand the overall language, environment, etc., try to think if there is someone better than you to review to code. In some rare cases, even if you are not familiar/savvy enough, there is no other developer than you to review it, prepare for quickly learning about the new language, environment, etc.

<strong>Step 2: understand</strong>

After pre-screening at the CL and make sure the size falls in a reasonable range, and you are the right person to review, you can start to understand the CL. In some other world, try to think in the same way the CL author thinks.

<strong>Purpose</strong>: start understanding the CL by asking yourself: "do I know the overall purpose of the CL?" The purpose of CL should be clearly stated in the CL's description. If not, ask for it. For complex CLs, later developers and maintainers rely on the description to understand the CL. Sometimes even the CL author him/herself will need to refer to descriptions to understand it. Even though sometimes the code is self-explanatory, the description should clearly identify the purpose of the CL.

<strong>Workflow</strong>

Then, ask yourself: "am I expecting this CL? Does it match what I am expecting?" In a lot of scenarios at Google, you are part of the project that the CL author is submitting this CL for. Based on Google's engineer standard of practice, a documentation of design and task-distribution process usually goes before implementation of the task. The reviewers usually have a basic big picture of what the expecting CL should do. If this CL is part of a project, and some other change needs to be done before this CL can function well, it should be mentioned in the description. Also if this CL is blocking other CL or updates, it would be good to mention it as well.

<strong>Design decisions</strong>

- <span class="GINGER_SOFTWARE_mark" id="7a425dd7-be13-4991-8a63-b7f40e69e456">check</span> the important design decisions, if any, are revealed in the code descriptions.

<strong>Step 3: verify</strong>

- Verify the code is doing what the description is doing.

- Verify the code has relevant tests to cover a) design decision, b) important default <span class="GINGER_SOFTWARE_mark" id="3efe545a-cf48-4968-9172-f76b9860c16d">valueu</span>, c) <span class="GINGER_SOFTWARE_mark" id="77f0997e-29a7-47a2-bc43-135eb3fa2598">complicate</span> logic, d) common edge cases like zero/null/default value, If statement edge, etc.

<strong>Step 4: optimize</strong>

- Is the logic optimizable

- Is the library that being used optimizable

<strong>Step 5: check</strong>

- Check the style

Acknowledge: this post is part of a self-reflection of my first year work at Google, thank my mentor Lexi Baugher and teammate Nicolas Glorioso, Paul Mantyala and many Googlers' help in helping me improving my coding skills and code review skills.