---
title: "How to Prepare for Software Engineer System Design Interviews: The Resources"
excerpt: "A reading list for system design interviews: DDIA for the foundations, then architecture trade-offs, domain modeling, reliability, classic patterns, and Alex Xu's two volumes for practice. Each book is checked against its publisher's page."
date: 2026-10-30
lang: en
author: aileen-wright
categories: [engineering]
tags: [system-design, interview, books]
translationKey: system-design-interview-resources
published: true
cover_image:
  src: /assets/blogposts/2026-10-30-system-design-interview-resources/sdi-00-cover-en.jpg
  x: 520
  y: 0
  size: 630
og_image: /assets/blogposts/2026-10-30-system-design-interview-resources/sdi-00-cover-en.jpg
---

A system design interview has a simple format. The interviewer names a product, such as a news feed or a chat service. The candidate draws an architecture on the spot, and then the two of them discuss the trade-offs. The ByteByteGo course on this topic calls these questions [the most difficult of all the technical interviews](#ref-bbg-foreword-hardest), because the scope is large, the requirements are vague, and there is [no standard or correct answer](#ref-bbg-foreword-answer).

When no single answer exists, memorizing answers does not help much. The interviewer wants to see whether you understand how data is stored, how requests are routed, and what happens when a machine fails. The interviewer also wants to hear you say what each choice costs. That knowledge comes from reading. This article gives a reading list in six groups and ends with the reading order that I recommend.

On 30 October 2026, I checked the author, edition, and publication date of each book against the publisher's page or the author's own page. Several books on the list now have a new edition, so check the edition before you buy.

## The first group explains data systems and distributed systems

![A house foundation under construction, with a thick blue book set into the stone footing as the cornerstone](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-01-foundation.jpg)

### Designing Data-Intensive Applications is the foundation of the list

Martin Kleppmann's *Designing Data-Intensive Applications* is usually called DDIA. The table of contents of the second edition starts with data models, storage, and encoding. Then it moves to [replication, sharding, transactions, and the trouble with distributed systems](#ref-oreilly-ddia2-toc). Most of the trade-offs that interviewers ask about have their background in those chapters.

Two editions of DDIA exist. Kleppmann wrote the second edition with Chris Riccomini. The O'Reilly page gives the [publication date as February 2026](#ref-oreilly-ddia2), and the book list on Kleppmann's homepage says [March 2026](#ref-kleppmann-home). Kleppmann wrote the first edition alone, and O'Reilly published it in [March 2017](#ref-oreilly-ddia1). If you have a choice, read the second edition.

### Understanding Distributed Systems gives a fast overview

Roberto Vitillo's *Understanding Distributed Systems* is shorter than DDIA. The book's website says that the current version is the [2nd edition, with 33 chapters and 328 pages](#ref-uds-edition). The book has [five parts: communication, coordination, scalability, resiliency, and maintainability](#ref-uds-parts). You can [read the first two chapters for free](#ref-uds-free) on the website.

The author says that the book [focuses on breadth more than depth](#ref-uds-breadth). It covers the network stack, data consistency models, scalability and reliability patterns, and observability. If you have little backend experience at scale, read this book first and DDIA second.

### Database Internals goes deeper into storage engines

Alex Petrov's *Database Internals* was published by O'Reilly in [October 2019](#ref-oreilly-dbint). The book's website says that the book has [two parts, Storage Engines and Distributed Systems](#ref-databass-parts). The first part covers B-trees, LSM trees, and the write-ahead log. The second part covers failure detection, leader election, consistency models, and consensus.

Interviews seldom go this deep. But an interviewer can ask why a database writes fast, or why your storage choice fits the read/write ratio. A reader of this book can answer at the level of the data structures.

## The second group gives a framework for architecture trade-offs

![A brass balance scale on a drafting table, with a model of one large building on one pan and a cluster of small connected houses on the other, almost level](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-02-tradeoffs.jpg)

### Fundamentals of Software Architecture compares architecture styles

Mark Richards and Neal Ford published the second edition of *Fundamentals of Software Architecture* with O'Reilly in [March 2025](#ref-oreilly-fosa2). This edition has [five new chapters](#ref-oreilly-fosa2-new). The first chapters define architecture characteristics, which are requirements such as scalability and availability that are not features. Then the book discusses [microservices, modular monoliths, microkernels, layered architectures](#ref-oreilly-fosa2-styles), and other styles one by one. A frequent follow-up question in an interview is "why this design and not that one?" This book gives you the words and the steps to compare designs.

### Software Architecture: The Hard Parts is about problems with no best practice

*Software Architecture: The Hard Parts* has four authors: Neal Ford, Mark Richards, Pramod Sadalage, and Zhamak Dehghani. O'Reilly published it in [October 2021](#ref-oreilly-hardparts). The title of chapter 1 is ["What Happens When There Are No 'Best Practices'?"](#ref-oreilly-hardparts-ch1). The book discusses [service granularity, contracts between services, and distributed transactions](#ref-oreilly-hardparts-topics). Interviewers often ask about these topics too.

### Two books about code-level design are optional

The next two books are about design at the level of modules and code. They have little to do with distributed systems, so they are optional for interview preparation.

Robert C. Martin's *Clean Architecture* was published by Pearson in [September 2017](#ref-informit-cleanarch). Its table of contents has [three main parts: design principles, component principles, and architecture](#ref-informit-cleanarch-toc). One chapter is about how to draw boundaries.

John Ousterhout is a professor of computer science at Stanford. He [released the second edition](#ref-aposd-2nd) of *A Philosophy of Software Design* in July 2021. The second edition adds sections to two chapters that compare the book with Robert Martin's *Clean Code*. Ousterhout writes that the two authors have [significant differences of opinion](#ref-aposd-cleancode) about the length of methods and the role of comments. If you read both books side by side, you see the design trade-offs more clearly than if you read only one.

## The third group covers domain modeling and service boundaries

![A hand-drawn town map divided into districts by coloured-pencil boundary lines, with a small wooden house in each district](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-03-boundaries.jpg)

When an interview question asks how to split a system into services, you need the concepts of domain modeling.

Eric Evans's *Domain-Driven Design* was published by Addison-Wesley in [August 2003](#ref-informit-ddd). Domain Language, the training company where Evans teaches, calls it ["The Big Blue Book"](#ref-domainlanguage-ddd). Ubiquitous Language, Aggregates, and Bounded Context are concepts that you hear often in interviews, and [each one has its own section](#ref-informit-ddd-toc) in the book.

Vaughn Vernon's *Implementing Domain-Driven Design* was published by Addison-Wesley in [February 2013](#ref-informit-iddd). It shows how to apply Evans's concepts in a real project.

Sam Newman's *Building Microservices*, second edition, was published by O'Reilly in [August 2021](#ref-oreilly-bm2). Newman says that the second edition is a [complete rewrite](#ref-newman-bm2-rewrite) of the first. The [first chapter is free](#ref-newman-bm2-free) on his website.

## The fourth group covers reliability and operations

![A cutaway sailing ship whose hull is divided by bulkheads, so that water in the flooded compartments stays contained and the ship floats level, with a lighthouse in the distance](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-04-bulkheads.jpg)

### Google gives away three SRE books

O'Reilly published the first edition of Google's *Site Reliability Engineering* in [April 2016](#ref-oreilly-sre1). Google puts [the full text online for free](#ref-sre-book-toc) at sre.google. The companion book [*The Site Reliability Workbook*](#ref-sre-workbook-toc) and [*Building Secure & Reliable Systems*](#ref-sre-books-bsrs) are also free to read online. Service level objectives (SLOs), load balancing at the frontend and in the datacenter, and handling overload all have their own chapters.

Google has also released a [completely rewritten second edition](#ref-sre-books-2nd). On the sre.google books page, the second edition has only a link to buy it from Google Books, with no link to read online. The free book is still the first edition.

### Release It! explains how systems fail in production

Michael Nygard's *Release It!*, second edition, was published by the Pragmatic Bookshelf in [January 2018](#ref-pragprog-releaseit). The book has a chapter on [stability patterns](#ref-pragprog-releaseit-patterns), which include timeouts, circuit breakers, and bulkheads. When an interviewer asks what happens if a downstream service fails, you can answer with these patterns.

## The fifth group is classic pattern catalogs for reference

![A library card catalog with one drawer open and a few index cards on the desk, each showing a small diagram of boxes and arrows](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-05-catalog.jpg)

These three books are more than twenty years old, and their technology examples are dated. I use them as reference books: when I see a pattern name that I do not know, I look up that one chapter.

Martin Fowler's *Patterns of Enterprise Application Architecture* came out in [2002](#ref-fowler-poeaa). Fowler says that the first part is a tutorial of about 100 pages, and [the rest is a reference to forty or so patterns](#ref-fowler-poeaa-patterns). The topics include [how to layer an enterprise application, how to organize domain logic, and how to connect that logic to a relational database](#ref-fowler-poeaa-topics).

Gregor Hohpe and Bobby Woolf's *Enterprise Integration Patterns* was published by Addison-Wesley in [October 2003](#ref-informit-eip). It contains [65 integration patterns](#ref-eip-site) for systems that communicate with messages. The pattern list on the website includes the [Publish-Subscribe Channel, the Dead Letter Channel, and the Idempotent Receiver](#ref-eip-toc). You use these concepts when you design a message queue in an interview.

*Design Patterns*, by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, was published by Addison-Wesley in [October 1994](#ref-informit-gof). It is about patterns in object-oriented code, so it helps less with system design interviews.

## The sixth group is for practice

![An open sketchbook with the same bridge drawn many times, next to an hourglass](/assets/blogposts/2026-10-30-system-design-interview-resources/sdi-06-practice.jpg)

### Alex Xu's two volumes are the main practice books

Volume 1 of Alex Xu's *System Design Interview – An Insider's Guide* came out in [2020](#ref-openlibrary-sdi1). Alex Xu and Sahn Lam wrote volume 2, which came out in [2022](#ref-goettingen-sdi2). The description of volume 2 calls it a sequel with a different set of questions, and says that [reading volume 1 is helpful but not required](#ref-goettingen-sdi2-standalone). Each chapter of the two volumes works through one question. Use them for practice after you read the books on principles.

ByteByteGo has a course with the same name, and the foreword that I quote at the start of this article comes from that course. Chapter 4 of the course gives a four-step framework: [understand the problem and set the design scope, propose a high-level design and get buy-in, do a deep dive, and wrap up](#ref-bbg-framework). When you practice, use the four steps to time yourself.

### Free resources add practice questions and papers

Donne Martin maintains the [System Design Primer](#ref-primer) on GitHub. It is a free study guide for system design interviews, and it includes Anki flashcards.

MIT's distributed systems course 6.5840 ([formerly 6.824](#ref-mit-6824-2022)) puts its schedule, readings, and labs online. The Spring 2026 schedule asks students to read papers before class, for example [GFS (2003)](#ref-mit-schedule-gfs), [Raft (2014)](#ref-mit-schedule-raft), and [Spanner (2012)](#ref-mit-schedule-spanner). The labs ask students to build MapReduce and Raft. If you want to find the original paper behind an idea in DDIA, use this schedule as a reading list.

## I recommend this reading order

1. **Read DDIA first for the foundations.** If you have little experience, read *Understanding Distributed Systems* before DDIA.
2. **Read *Fundamentals of Software Architecture* next.** It gives you a method to compare designs, so you can explain why you chose one.
3. **Choose the books on domain-driven design, microservices, and SRE that fit your target role.** For product systems, read more of Evans, Vernon, and Newman. For infrastructure, read more of the SRE books, *Release It!*, and *Database Internals*.
4. **Practice with Alex Xu's two volumes in the last stage.** After each question, find the related chapter in a book on principles. Make sure that you understand the answer and did not only memorize it.

You do not need to read the pattern books in the fifth group from start to finish. Look up a pattern when you need it. If you have little time, read at least DDIA and Alex Xu's two volumes. If you have more time, read some of the papers on the MIT schedule. Then you can talk about replication and consensus with more confidence.

## References

Publisher pages and authors' own pages are primary sources. ByteByteGo is a course platform, so it is a commercial source, and I use it only for quotes from its course. I did not find a book page from Byte Code LLC, the publisher of Alex Xu's books, so library catalogs supply the publication data for those two volumes.

**System design interviews**

- <span id="ref-bbg-foreword-hardest"></span>ByteByteGo — [System Design Interview course, Foreword](https://bytebytego.com/courses/system-design-interview/foreword#:~:text=System%20design%20interview%20questions%20are%20the%20most%20difficult%20to%20tackle%20among%20all%20the%20technical%20interviews). Quote: “System design interview questions are the most difficult to tackle among all the technical interviews.” (commercial source) — fetched [2026-10-30](https://web.archive.org/web/20260413171600/https://bytebytego.com/courses/system-design-interview/foreword)
- <span id="ref-bbg-foreword-answer"></span>ByteByteGo — [System Design Interview course, Foreword, on answers](https://bytebytego.com/courses/system-design-interview/foreword#:~:text=without%20a%20standard%20or%20correct%20answer). Quote: “The processes are open-ended and unclear without a standard or correct answer.” (commercial source) — fetched [2026-10-30](https://web.archive.org/web/20260413171600/https://bytebytego.com/courses/system-design-interview/foreword)
- <span id="ref-bbg-framework"></span>ByteByteGo — [System Design Interview course, chapter 4, “A Framework For System Design Interviews”](https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews#:~:text=Step%201%20-%20Understand%20the%20problem%20and%20establish%20design%20scope). Steps: “Step 1 - Understand the problem and establish design scope”, “Step 2 - Propose high-level design and get buy-in”, “Step 3 - Design deep dive”, “Step 4 - Wrap up” (commercial source) — fetched [2026-10-30](https://web.archive.org/web/20260618014719/https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews)

**Data systems and distributed systems**

- <span id="ref-oreilly-ddia2"></span>O'Reilly — [Designing Data-Intensive Applications, 2nd Edition](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/). Listing: “by Martin Kleppmann, Chris Riccomini”, “February 2026”, 672 pages — fetched [2026-10-30](https://web.archive.org/web/20260616232347/https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
- <span id="ref-oreilly-ddia2-toc"></span>O'Reilly — [Designing Data-Intensive Applications, 2nd Edition, table of contents](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/). Chapters 3 to 9: “Data Models and Query Languages”, “Storage and Retrieval”, “Encoding and Evolution”, “Replication”, “Sharding”, “Transactions”, “The Trouble with Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20260616232347/https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
- <span id="ref-oreilly-ddia1"></span>O'Reilly — [Designing Data-Intensive Applications (first edition)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). Listing: “by Martin Kleppmann”, “March 2017”, 616 pages — fetched 2026-10-30 (no archive found)
- <span id="ref-kleppmann-home"></span>Martin Kleppmann — [homepage, list of books](https://martin.kleppmann.com/#:~:text=2nd%20edition%20co-authored%20with%20Chris%20Riccomini%20appeared%20in%202026). Quote: “Designing Data-Intensive Applications, 2nd Edition. O'Reilly Media, March 2026.” — fetched [2026-10-30](https://web.archive.org/web/20261019064754/https://martin.kleppmann.com/)
- <span id="ref-uds-edition"></span>Roberto Vitillo — [Understanding Distributed Systems website, edition](https://understandingdistributed.systems/#:~:text=2nd%20edition%20with%2033%20packed%20chapters%20and%20328%20pages). Quote: “2nd edition with 33 packed chapters and 328 pages in PDF and EPUB format” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-parts"></span>Roberto Vitillo — [Understanding Distributed Systems website, structure of the book](https://understandingdistributed.systems/#:~:text=The%20book%20is%20divided%20into%205%20parts). Quote: “The book is divided into 5 parts: communication, coordination, scalability, resiliency, and maintainability.” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-free"></span>Roberto Vitillo — [Understanding Distributed Systems website, free chapters](https://understandingdistributed.systems/#:~:text=Read%20the%20first%20two%20chapters%20for%20free). Quote: “Read the first two chapters for free” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-uds-breadth"></span>Roberto Vitillo — [Understanding Distributed Systems website, audience](https://understandingdistributed.systems/#:~:text=looking%20for%20depth%20rather%20than%20breadth). Quote: “As an expert, you are likely looking for depth rather than breadth, and this book focuses more on the latter”. Same page: “you need to be familiar with the network stack, data consistency models, scalability and reliability patterns, observability best practices, and much more” — fetched [2026-10-30](https://web.archive.org/web/20261004054220/https://understandingdistributed.systems/)
- <span id="ref-oreilly-dbint"></span>O'Reilly — [Database Internals](https://www.oreilly.com/library/view/database-internals/9781492040330/). Listing: “by Alex Petrov”, “October 2019”, 370 pages — fetched [2026-10-30](https://web.archive.org/web/20260601001713/https://www.oreilly.com/library/view/database-internals/9781492040330/)
- <span id="ref-databass-parts"></span>Alex Petrov — [Database Internals website, structure of the book](https://www.databass.dev/#:~:text=The%20book%20consists%20of%20two%20parts). Quote: “The book consists of two parts: Storage Engines and Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20261012194439/https://www.databass.dev/)

**Software architecture**

- <span id="ref-oreilly-fosa2"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/). Listing: “by Mark Richards, Neal Ford”, “March 2025”, 546 pages — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-fosa2-new"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition, overview](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/#:~:text=with%20five%20new%20chapters). Quote: “This updated edition provides a comprehensive overview of software architecture's many aspects, with five new chapters covering the latest insights from the field.” — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-fosa2-styles"></span>O'Reilly — [Fundamentals of Software Architecture, 2nd Edition, overview](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/#:~:text=Microservices%2C%20modular%20monoliths%2C%20microkernels%2C%20layered%20architectures). Quote: “Architecture styles and patterns: Microservices, modular monoliths, microkernels, layered architectures, and many more”. Table of contents, chapter 4: “Architectural Characteristics Defined” — fetched [2026-10-30](https://web.archive.org/web/20260603184746/https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/)
- <span id="ref-oreilly-hardparts"></span>O'Reilly — [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/). Listing: “by Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani”, “October 2021”, 462 pages — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-oreilly-hardparts-ch1"></span>O'Reilly — [Software Architecture: The Hard Parts, table of contents, chapter 1](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/#:~:text=What%20Happens%20When%20There%20Are%20No). Quote: “1. What Happens When There Are No ‘Best Practices’?” — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-oreilly-hardparts-topics"></span>O'Reilly — [Software Architecture: The Hard Parts, overview](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/#:~:text=how%20to%20determine%20service%20granularity). Quote: “they examine everything from how to determine service granularity, manage workflows and orchestration, manage and decouple contracts, and manage distributed transactions” — fetched [2026-10-30](https://web.archive.org/web/20260223014505/https://www.oreilly.com/library/view/software-architecture-the/9781492086888/)
- <span id="ref-informit-cleanarch"></span>InformIT (Pearson) — [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166#:~:text=Published%20Sep%2010%2C%202017). Listing: “By Robert C. Martin”, “Published Sep 10, 2017 by Pearson” — fetched [2026-10-30](https://web.archive.org/web/20261003133541/https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166)
- <span id="ref-informit-cleanarch-toc"></span>InformIT (Pearson) — [Clean Architecture, table of contents](https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166#:~:text=Part%20III%3A%20Design%20Principles). Parts: “Part III: Design Principles”, “Part IV: Component Principles”, “Part V: Architecture”, and the chapter “Boundaries: Drawing Lines” — fetched [2026-10-30](https://web.archive.org/web/20261003133541/https://www.informit.com/store/clean-architecture-a-craftsmans-guide-to-software-structure-9780134494166)
- <span id="ref-aposd-2nd"></span>John Ousterhout — [Software Design Book page](https://web.stanford.edu/~ouster/cgi-bin/book.php#:~:text=In%20July%20of%202021%20I%20released%20the%20Second%20Edition). Quote: “In July of 2021 I released the Second Edition of A Philosophy of Software Design.” Page header: “John Ousterhout, Professor, Department of Computer Science” — fetched [2026-10-30](https://web.archive.org/web/20260930000611/https://www.web.stanford.edu/~ouster/cgi-bin/book.php)
- <span id="ref-aposd-cleancode"></span>John Ousterhout — [Software Design Book page, comparison with Clean Code](https://web.stanford.edu/~ouster/cgi-bin/book.php#:~:text=we%20have%20significant%20differences%20of%20opinion). Quote: “we have significant differences of opinion on topics such as the length of methods and the role of comments” — fetched [2026-10-30](https://web.archive.org/web/20260930000611/https://www.web.stanford.edu/~ouster/cgi-bin/book.php)

**Domain modeling and service boundaries**

- <span id="ref-informit-ddd"></span>InformIT (Addison-Wesley) — [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217#:~:text=Published%20Aug%2020%2C%202003). Listing: “By Eric Evans”, “Published Aug 20, 2003 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20261018122420/https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217)
- <span id="ref-informit-ddd-toc"></span>InformIT (Addison-Wesley) — [Domain-Driven Design, table of contents](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217#:~:text=UBIQUITOUS%20LANGUAGE). Sections: “UBIQUITOUS LANGUAGE”, “AGGREGATES”, “BOUNDED CONTEXT” — fetched [2026-10-30](https://web.archive.org/web/20261018122420/https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217)
- <span id="ref-domainlanguage-ddd"></span>Domain Language — [DDD Resources](https://www.domainlanguage.com/ddd/#:~:text=The%20Big%20Blue%20Book). Quote: “The Big Blue Book. Domain-Driven Design, by Eric Evans, provides a broad framework for making design decisions”. Same page: “In addition to offering training, Eric Evans and the other instructors are active speakers and writers” — fetched [2026-10-30](https://web.archive.org/web/20261005171737/https://www.domainlanguage.com/ddd/)
- <span id="ref-informit-iddd"></span>InformIT (Addison-Wesley) — [Implementing Domain-Driven Design](https://www.informit.com/store/implementing-domain-driven-design-9780321834577#:~:text=Published%20Feb%206%2C%202013). Listing: “By Vaughn Vernon”, “Published Feb 6, 2013 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20260710111237/https://www.informit.com/store/implementing-domain-driven-design-9780321834577)
- <span id="ref-oreilly-bm2"></span>O'Reilly — [Building Microservices, 2nd Edition](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/). Listing: “by Sam Newman”, “August 2021”, 612 pages — fetched [2026-10-30](https://web.archive.org/web/20260628082224/https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/)
- <span id="ref-newman-bm2-rewrite"></span>Sam Newman — [Building Microservices, 2nd Edition page](https://samnewman.io/books/building_microservices_2nd_edition/#:~:text=The%202nd%20edition%20is%20a%20complete%20rewrite). Quote: “The 2nd edition is a complete rewrite of the previous best selling edition” — fetched [2026-10-30](https://web.archive.org/web/20260919013741/https://samnewman.io/books/building_microservices_2nd_edition/)
- <span id="ref-newman-bm2-free"></span>Sam Newman — [Building Microservices, 2nd Edition page, free chapter](https://samnewman.io/books/building_microservices_2nd_edition/#:~:text=The%20first%20chapter%20of%20the%20book%20is%20available%20for%20free). Quote: “The first chapter of the book is available for free.” — fetched [2026-10-30](https://web.archive.org/web/20260919013741/https://samnewman.io/books/building_microservices_2nd_edition/)

**Reliability and operations**

- <span id="ref-oreilly-sre1"></span>O'Reilly — [Site Reliability Engineering (first edition)](https://www.oreilly.com/library/view/site-reliability-engineering/9781491929117/). Listing: “by Niall Richard Murphy, Betsy Beyer, Chris Jones, Jennifer Petoff”, “April 2016” — fetched [2026-10-30](https://web.archive.org/web/20260706162528/https://www.oreilly.com/library/view/site-reliability-engineering/9781491929117/)
- <span id="ref-sre-book-toc"></span>Google — [Site Reliability Engineering, online table of contents](https://sre.google/sre-book/table-of-contents/). Chapters include 4 “Service Level Objectives”, 19 “Load Balancing at the Frontend”, 20 “Load Balancing in the Datacenter”, and 21 “Handling Overload” — fetched [2026-10-30](https://web.archive.org/web/20261023010553/https://sre.google/sre-book/table-of-contents/)
- <span id="ref-sre-workbook-toc"></span>Google — [The Site Reliability Workbook, online table of contents](https://sre.google/workbook/table-of-contents/). Chapter 2: “Implementing SLOs” — fetched [2026-10-30](https://web.archive.org/web/20261002021106/https://sre.google/workbook/table-of-contents/)
- <span id="ref-sre-books-bsrs"></span>Google — [sre.google books page, Building Secure & Reliable Systems](https://sre.google/books/#:~:text=Building%20Secure%20%26%20Reliable%20Systems). The entry has a “Read online” link — fetched [2026-10-30](https://web.archive.org/web/20261015174024/https://sre.google/books/)
- <span id="ref-sre-books-2nd"></span>Google — [sre.google books page, second edition](https://sre.google/books/#:~:text=In%20this%20completely%20rewritten%20edition). Quote: “In this completely rewritten edition, we explore current SRE practices and how they've evolved in the decade since the book's initial publication”. The entry has only a “Buy from Google Books” link — fetched [2026-10-30](https://web.archive.org/web/20261015174024/https://sre.google/books/)
- <span id="ref-pragprog-releaseit"></span>The Pragmatic Bookshelf — [Release It! Second Edition](https://pragprog.com/titles/mnee2/release-it-second-edition/). Listing: “by Michael Nygard”, Pages: 376, Published: January 2018 — fetched [2026-10-30](https://web.archive.org/web/20260919013804/https://pragprog.com/titles/mnee2/release-it-second-edition/)
- <span id="ref-pragprog-releaseit-patterns"></span>The Pragmatic Bookshelf — [Release It! Second Edition, table of contents](https://pragprog.com/titles/mnee2/release-it-second-edition/#:~:text=Stability%20Patterns). The chapter “Stability Patterns” lists “Timeouts”, “Circuit Breaker”, and “Bulkheads” — fetched [2026-10-30](https://web.archive.org/web/20260919013804/https://pragprog.com/titles/mnee2/release-it-second-edition/)

**Classic patterns**

- <span id="ref-fowler-poeaa"></span>Martin Fowler — [Patterns of Enterprise Application Architecture book page](https://martinfowler.com/books/eaa.html). Listing: “by Martin Fowler, with Dave Rice, Matthew Foemmel, Edward Hieatt, Robert Mee, and Randy Stafford”, “2002” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-fowler-poeaa-patterns"></span>Martin Fowler — [Patterns of Enterprise Application Architecture book page, structure](https://martinfowler.com/books/eaa.html#:~:text=the%20reference%20to%20forty%20or%20so%20patterns). Quote: “The first part is a short (100 page) tutorial on enterprise application architecture. The bulk of the book is the reference to forty or so patterns.” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-fowler-poeaa-topics"></span>Martin Fowler — [Patterns of Enterprise Application Architecture book page, topics](https://martinfowler.com/books/eaa.html#:~:text=how%20to%20layer%20an%20enterprise%20application). Quote: “The main topic areas are: how to layer an enterprise application, how to organize domain logic, how to tie that logic to a relational database” — fetched [2026-10-30](https://web.archive.org/web/20260928164951/https://martinfowler.com/books/eaa.html)
- <span id="ref-informit-eip"></span>InformIT (Addison-Wesley) — [Enterprise Integration Patterns](https://www.informit.com/store/enterprise-integration-patterns-designing-building-9780321200686#:~:text=Published%20Oct%2010%2C%202003). Listing: “By Gregor Hohpe, Bobby Woolf”, “Published Oct 10, 2003 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20260614033829/https://www.informit.com/store/enterprise-integration-patterns-designing-building-9780321200686)
- <span id="ref-eip-site"></span>Gregor Hohpe — [Enterprise Integration Patterns website](https://www.enterpriseintegrationpatterns.com/#:~:text=This%20pattern%20language%20consisting%20of%2065%20integration%20patterns). Quote: “This pattern language consisting of 65 integration patterns helps developers design and build distributed applications or integrate existing ones.” — fetched [2026-10-30](https://web.archive.org/web/20261005180019/https://www.enterpriseintegrationpatterns.com/)
- <span id="ref-eip-toc"></span>Gregor Hohpe — [Enterprise Integration Patterns, pattern catalog](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html). The catalog lists “Publish-Subscribe Channel”, “Dead Letter Channel”, and “Idempotent Receiver” — fetched [2026-10-30](https://web.archive.org/web/20261019172151/https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html)
- <span id="ref-informit-gof"></span>InformIT (Addison-Wesley) — [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610#:~:text=Published%20Oct%2031%2C%201994). Listing: “By Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides”, “Published Oct 31, 1994 by Addison-Wesley Professional” — fetched [2026-10-30](https://web.archive.org/web/20261010172538/https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610)

**Interview practice**

- <span id="ref-openlibrary-sdi1"></span>Open Library — [System Design Interview – An Insider's Guide, catalog record](https://openlibrary.org/books/OL30260884M). ISBN 9798664653403, author Alex Xu, published 2020 — fetched 2026-10-30 (no archive found)
- <span id="ref-goettingen-sdi2"></span>University of Göttingen, Computer Science Library — [System Design Interview – An Insider's Guide: Volume 2, catalog record](https://bib.informatik.uni-goettingen.de/book/1800028660). Authors Alex Xu and Sahn Lam, published 2022 — fetched 2026-10-30 (no archive found)
- <span id="ref-goettingen-sdi2-standalone"></span>University of Göttingen, Computer Science Library — [Volume 2 catalog record, description](https://bib.informatik.uni-goettingen.de/book/1800028660#:~:text=Although%20reading%20Volume%201%20is%20helpful%2C%20it%20is%20not%20required). Quote: “This book can be seen as a sequel to the book: System Design Interview - An Insider's Guide. … Although reading Volume 1 is helpful, it is not required.” — fetched 2026-10-30 (no archive found)
- <span id="ref-primer"></span>Donne Martin — [system-design-primer repository on GitHub](https://github.com/donnemartin/system-design-primer#:~:text=Prep%20for%20the%20system%20design%20interview). Description: “Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards.” — fetched [2026-10-30](https://web.archive.org/web/20261025031510/https://github.com/donnemartin/system-design-primer)
- <span id="ref-mit-6824-2022"></span>MIT — [6.824 course home page, Spring 2022](http://nil.csail.mit.edu/6.824/2022/). Page heading: “6.824: Distributed Systems” — fetched [2026-10-30](https://web.archive.org/web/20260208023554/http://nil.csail.mit.edu/6.824/2022/)
- <span id="ref-mit-schedule-gfs"></span>MIT 6.5840 — [Spring 2026 schedule, lecture 3](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20GFS%20%282003%29). Quote: “LEC 3 (fk): GFS. Preparation: Read GFS (2003)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)
- <span id="ref-mit-schedule-raft"></span>MIT 6.5840 — [Spring 2026 schedule, lecture 6](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20Raft%20%28extended%29%20%282014%29). Quote: “LEC 6 (fk): Fault Tolerance: Raft (1). Preparation: Read Raft (extended) (2014)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)
- <span id="ref-mit-schedule-spanner"></span>MIT 6.5840 — [Spring 2026 schedule, lecture 12](https://pdos.csail.mit.edu/6.824/schedule.html#:~:text=Read%20Spanner%20%282012%29). Quote: “LEC 12 (rtm): Spanner. Preparation: Read Spanner (2012)” — fetched [2026-10-30](https://web.archive.org/web/20261023180617/https://pdos.csail.mit.edu/6.824/schedule.html)
