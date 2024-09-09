---
title: "Startup Notes: Reflections on Accounting"
date: 2024-09-09
categories:
  - blog
tags:
  - Jekyll
  - update
  - startup-notes
  - en-US
---


Before I started my own business, accounting was always an area that felt confusing and mysterious to me. It's only recently that I've begun to understand the core logic of accounting. These are some of my learnings and understandings. If there are any misunderstandings or inaccuracies, please feel free to correct me. I'd be happy if this helps other entrepreneurs who also feel confused about this topic.

## The Essence of Accounting

The essence of accounting is actually very simple: "Counting clearly what matters"

First: Define well what "matters"
Second: Count accurately the quantity of these things.

Especially for the second point, since we live in the "real" world, when we count "the same thing" from different angles, the conclusions should be the same.

Based on these two points, we can start from the most core statements to understand the logic of accounting.

## Balance Sheet: How Much Do You Have Left?

What do people care about most? As an owner, when running a business, you often care most about "how much (assets) are left" in this business. Since humans invented borrowing, this question has become: how much money or items do I have now, which ones belong to me, and which ones do I need to return to others.

This is one of the most important statements in accounting: the balance sheet. It reflects how total assets are allocated between borrowers and shareholders at a certain point in time. This gives rise to the first famous accounting equation:

**Assets = Liabilities + Shareholders' Equity**

## Income Statement: How Much Did You Earn?

When running a business, the second question often focused on is: "How much money did we make?" This is the origin of another important statement: the income statement (or profit and loss statement).

The income statement solves the problem of: in a given time interval, how much is left after subtracting various expenses from all the income I received. It records the entire process from revenue to final profit.

## Cash Flow Statement: Do You Have Enough Cash?

In the process of operation, people found that cash is particularly important. Even if you have assets, it's difficult to actually operate without cash. Especially when it comes to intangible assets, cash needs to be distinguished from other assets.

Therefore, around 1950 to 1970, people proposed a method to calculate cash separately, which is the cash flow statement. It records the initial cash, changes during the period, and final cash, and analyzes the reasons for cash changes (whether caused by earnings or financing activities).

## The Physical Logic of Accounting Equations

From the first principles, the physical logic of accounting equations is: looking at the same thing from two different angles should yield the same result.

- Assets = Shareholders' Equity + Liabilities: This is because shareholders' equity itself is defined as assets minus liabilities.
- Income - Expenses = Change in Assets: This reflects the actual situation in the physical world, when you put something into a box, it belongs to that box.
- Cash flow follows the same logic: when you define something as cash and put it in a specific box, it's in that box.

The essence of these equations comes from physical reality.

## The Origin of Double-Entry Bookkeeping

To maintain and verify these equations, double-entry bookkeeping came into being. It requires that both sides of the equation are calculated each time a calculation is made, which means that each record needs to be shown on both sides.

## Mathematics and Physics Describing Statements: "Point in Time" and "Period", Currency Units

As a beginner like me, I often need to remind myself: all statements have their time relevance. In other words, statements have no meaning without the concept of time.
For example, if you want to count how much money is left, you need to make a cross-section of time, choose a point in time, and calculate how much money is left at that point. Therefore, the balance sheet is always for a specific point in time. When it comes to "how much money was earned", there needs to be a period. The vegetables sold in one day are certainly not as much as those sold in a week. Without a period, talking about how much money was earned has no meaning, so the income statement and cash flow statement must correspond to a period. Other various statements and accounts follow the same logic, and currency units are also necessary. This is like in physics where you can't talk about any physical quantity without time, space, or units - unless it's a constant. But there are no constants in finance, only equations.

## Breaking Down "The Essence of Accounting": Subjective and Objective

"Defining what matters" - this is a subjective question. This also leads to different statements listing and counting different contents, or different definitions for each entry. For example, if a company pays dividends, it is classified as "operating activities" or "financing activities" in International Accounting Standards, while in US Generally Accepted Accounting Principles (GAAP) it must be classified as "financing activities". In this sense, it's not that dividends differ in quantity, but that in the two accounting standards, the scope corresponding to "financing activities" is defined differently.

As a science and engineering student, I felt quite uneasy about this seemingly groundless homonymy, because I didn't know where this difference came from and how it was derived. But when I understood that this was a "subjective" definition, I understood and it gave me a lot of security.
- If I'm making statements, understanding that I'm counting things according to someone else's definition (accounting standards), then I'll just follow their definition and not worry too much about why they define it that way - because it's subjective. For example, tax forms that need to be shown to the government, or financial statements for the SEC and investors, must be counted according to rules defined by others (accounting standard-setting bodies).
- At the same time: it gives me a fulcrum to apply first principles, I can also define things I care about in statements that are only for our own viewing, and then count them clearly. Managerial Accounting is probably this type.

"Counting things clearly", after defining "things", is an objective question. The double-entry bookkeeping method we commonly use is a common method to ensure things are counted correctly, counting the same thing from different angles on both sides and checking for equality to reduce errors.

### Subjectivity of Price and Value

Of course, there's another kind of subjectivity: sometimes our estimation of the price and value of something also carries a certain subjectivity. Different people may value the same asset very differently, so in financial reports, this subjectivity may lead to inaccurate records. This subjectivity often becomes a means of falsifying accounts. Therefore, everyone who looks at financial statements will be concerned about the calculation methods for the value of some items in the accounting standards and financial statement footnotes.

## Reflection: What Will Change and What Won't in the Future of Accounting?

Using "first principles" to think is to judge what is intrinsic, constant, unchanging; and what changes with external factors.

1. We divide a fund pool into shareholders' money and creditors' money because humans started to have borrowing behavior. If there were no borrowing, there might not be the equation "Assets = Shareholders' Equity + Liabilities", but only "Assets = Assets".
2. The logic of accounting is constant, but these statements may change according to specific situations. If new categories other than liabilities appear in the future, or if certain values become variable, this equation may need to be modified.
	1. If the government starts to levy proportional taxes on assets, it may be necessary to add "government equity" as an item.
	2. Non-profit organizations have issues they care about more than "money", so perhaps they should have another type of statement, such as "number of people". Analogous to the balance sheet, it might become a statement of "Contributors = Volunteers + Employees". And the income statement would become "User conversion = Contributor increment"
	3. Blockchain might change the "Cash Flow" statement. If we often face different currencies or units of calculation, or if the conversion between assets becomes very frequent, the cash flow statement may no longer have its original meaning.

### Some Potential Changes in Accounting Brought by Blockchain

- If the error rate of accounts becomes extremely low, the possibility of tampering becomes extremely small, and the computational cost, storage cost, and labor cost of bookkeeping and reconciliation become almost negligible, what will accounting become? Let me make some guesses

	- In traditional understanding, loan financing behavior is not frequent, it's intermittent. Each loan financing will calculate the total financing amount. However, in the context of blockchain, loan behavior may be continuous. In this case, perhaps the way of bookkeeping needs to change
	- Not only financing, but if there are continuously delivered products or services, or continuously generated obligations, it's difficult to fully show this behavior that is relatively continuous over time on financial statements. This has also led to two accounting methods - cash basis and accrual basis - which to some extent try to solve this problem, but are not perfect.
	- Today, convertible notes or other equity financing tools such as SAFE that automatically convert into debt or equity or different proportions of equity according to various conditions are already complex enough. There are no good financial statements that can easily describe this situation, so special cap tables need to be developed to model various potential situations. In the case of blockchain, what if investment can also be automatically and continuously input to a large extent according to certain time and external conditions, or automatically and continuously distribute dividends? Today's accounting books are probably unable to adapt to this complex situation, so a new bookkeeping system and accounting system need to be born.

## Conclusion

Back to the essence, the logic of accounting is to calculate clearly what people care about. Combined with human current business activities based on buying and selling, accounting needs to calculate clearly how much goods we have now, who these goods belong to, and how these goods come in and out. This forms the three major statements of accounting.

I hope these thoughts can help you better understand the core logic of accounting and provide some inspiration for your entrepreneurial journey. Of course, this is just my personal understanding, if there are any shortcomings, please feel free to point them out.