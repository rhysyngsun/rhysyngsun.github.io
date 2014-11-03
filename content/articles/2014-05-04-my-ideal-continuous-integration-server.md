Title: My Ideal Continuous Integration Server
Date: 2014-11-04 20:02:10 -0400
Category: Continuous Integration
Tags: Continuous Integration, Continuous Delivery

I've spent the last week looking at various CI solutions. My main criteria were:

- create a flexible [Continuous Delivery](http://martinfowler.com/bliki/ContinuousDelivery.html) [deployment pipeline](http://martinfowler.com/bliki/DeploymentPipeline.html)
- ability to promote builds to various environments (QA, prod, etc)
- alerting to our team

It started with an attempt at wrangling the defacto tool, [Jenkins](http://jenkins-ci.org) into a usable system but that quickly proved to be an uphill battle.
Overly complication configuration aside, the final straw with Jenkins was being unable to configure
[GitHub Web Hooks](https://help.github.com/articles/creating-webhooks), however
that capability was dependent on having GitHub configured as _the_ authentication method for users.

That's a pretty flawed design that speaks to a poor separation of concerns;
authentication strategy should not be tangled with an unrelated feature of the product.
Overall, I think the legacy of Jenkins' plugin architecture is weighing it (and its users) down.

I also took a look at numerous open source competitors to Jenkins as well as SaaS-based solutions.
Pretty much all of these fell short on Goal #2, which lead to me a conclusion that everyone out there either:

- is deploying code straight into production via automation (Continuous Deployment)
- poured weeks of developer time into Jenkins
- gave up on Jenkins and rolled a custom solution

I wasn't ready to commit to any of these at the immediate moment, so the situation was looking pretty bleak.
I [threw out a tweet](https://twitter.com/rhysyngsun/status/461276722382790656) to vent my frustration at the state of CI/CD solutions.
[Chad Wathington](https://twitter.com/twchad) replied that [ThoughtWorks](http://www.thoughtworks.com/) had recently open sourced their Continuous Delivery solution [named Go](https://github.com/gocd/gocd/) (not to be confused with Golang, an issue they're [acutely aware of](https://github.com/gocd/gocd/issues/128)).

So far, I'm pretty impressed. As far as open source self-hostable CI solutions go, it's not nearing an complicated and limiting as Jenkins.
It does seem a _tad_ more complicated than I need, but it's likely because my initial pass at getting a pipeline is intended to be a simple one.

I still feel like Go is needs a lot of work and hope to contribute to it myself at some point (although I wish it wasn't written in Java).

I've also got feeling that I should take a stab at my own solution (to be done on my own time, not my employer's).
There's a lot to still be done in this space and I have a gut feeling that it needs a fresh approach that incorporates all these learnings.
The fresh start is needed because an ideal solution for CI needs back pressure against complexity.
