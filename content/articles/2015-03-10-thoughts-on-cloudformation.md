Title: Thoughts on CloudFormation
Date: 2015-03-10 08:10:10 -0400
Category: AWS
Tags: AWS, CloudFormation, Deployment

I've spent the last 10 months working with AWS' CloudFormation service. I felt it would be useful to put my thoughts together on how I found the service to be for a small startup.

## Pros

CloudFormation is great if you don't want to deal with the orchestration of your deployments. It runs over your configuration files and figures out what the delta changes are, applies them taking dependencies into account, and will also rollback if a failure occurs.

Overall, CloudFormation works well for offloading the execution of deployments.

## Cons

There are a few places where CloudFormation begins to fall short for me.

The first is complexity. I'm not saying the service can't handle the complexity, but humans can't handle the complexity of the JSON that CloudFormation uses for configuration. Even a moderately complex environment can begin to clock in at thousands of lines of JSON. At that point, it starts to feel like the XML days of yore.

That means you have to lean on a tool like [troposphere](https://github.com/cloudtools/troposphere) can do some heavy lifting. Troposphere is a great library and I would not even try to approach CloudFormation without it or something equivalent.

The second downside is when your stacks fail to rollback. This happens most often when you're making a complicated change (e.g. refactoring nested CloudFormation templates) and the only way to get resolution on it is to contact AWS support. Support on the forums is slow and you're not always guaranteed to get attention either so if you end up using CloudFormation you better have [premium support](https://aws.amazon.com/premiumsupport/). Your best bet is to makes a series of smaller, incremental changes, rather than sweeping refactoring.

The third downside is that you're limited to 20 stacks per region by default. You can request an increase to this limit, but there's always a limit. Limits like this are in place so that AWS can ensure a performant service for all their customers. This ends up steering you towards monolithic stacks, which can be even more painful. This also makes it much more difficult to run an arbitrary number of ad-hoc production-like environments for your developers.

## Alternatives

#### Roll Your Own with Boto

If you're using Python to generate CloudFormation configuration, it's not a huge leap to just use [boto](http://boto.readthedocs.org/) directly. The [AWS CLI](http://aws.amazon.com/cli/) runs on boto so the one thing you can count on is really solid service coverage. Boto will give you much more control and a better ability to recover from failed deployments, whereas a failure in CloudFormation (failed rollbacks are notoriously painful and always require intervention of AWS support to resolve) can possibly hold your service hostage while you engage AWS support to fix the failed stack. You'll have to handle rollback yourself, but you have much control over how exactly that works.

#### Terraform

Hashicorp's [Terraform](https://www.terraform.io/) is one project to keep an eye on. The main roadblock to adoption for me would be the limited scope of [AWS coverage](https://github.com/hashicorp/terraform/issues/28). It's a pretty cool tool so far though and once it achieves a higher coverage of AWS services it will probably be my go-to tool.

## Final Thoughts

CloudFormation can really help you get going on AWS if you don't want to deal with some of the deployment logistics, but the complexity of configuring it will quickly catch up with you for non-trivial deployments. AWS is continuing to improve the service though so some of the pitfalls I point out here may improve of time (particularly the rollback failures as I know it's a sore point).
