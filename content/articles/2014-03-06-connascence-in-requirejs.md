Title: Connascence in RequireJS
Date: 2014-03-06 17:50:15 -0500
Category: Software Engineering
Tags: Javascript, RequireJS, Software Engineering

I'm a huge fan of keeping code complexity to a minimum. Note that I'm distinguishing code complexity from system complexity. I believe you can have a complex system built on simple code. In fact, that's what you want because such code is highly testable.

We've all run across examples of complex code: a class with too many concerns, a function that's doing too many operations, or an abstraction in a place where it's unnecessary.

A few days after his passing, I watched a video of [Jim Weirich](http://en.wikipedia.org/wiki/Jim_Weirich) of Rake fame [giving a presentation](http://youtu.be/NLT7Qcn_PmI) on the concept of [connascence](http://en.wikipedia.org/wiki/Connascence_(computer_programming)). I highly recommend you watch it if you're unfamiliar with the topic.

This topic really hit on one of those things that I'd previously vaguely categorized as a "code smell." Code that's highly coupled makes for painful points when you have to change a behavior in the overall system. It's nice to have a quality metric for that now.

A few days later it struck me that this concept explains very well why I've always had trouble with this style of [RequireJS](http://requirejs.org/) (this example lifted from their docs [here](http://requirejs.org/docs/api.html#defdep):

    :::javascript
    //my/shirt.js now has some dependencies, a cart and inventory
    //module in the same directory as shirt.js
    define(["./cart", "./inventory"], function(cart, inventory) {
        //return an object to define the "my/shirt" module.
        return {
            color: "blue",
            size: "large",
            addToCart: function() {
                inventory.decrement(this);
                cart.add(this);
            }
        }
    });

In this example, there's an increasing Connascence of Order between the array of dependencies and the argument list as the number of dependencies for your module increase. Ideally, you should be keeping your dependency count as low as possible, but very often it slips over two or three, which is the point at which I'd say this type of connascence starts to become troublesome.

I'm also one of those folks who is very anal with making sure dependencies/imports are logically ordered and (if necessary) logically grouped. That means I'm occasionally inserting a dependency into list, rather than appending it.

Note that there's also a Connascence of Name between a dependency's name in the list and the filename of that module. There's no way to get away from that, but you can completely remove the Connascence of Order by changing to a CommonJS-ish style:

    :::javscript
    define(function(require) {
        //my/shirt.js now has some dependencies, a cart and inventory
        //module in the same directory as shirt.js
        var cart = require("./cart"),
            inventory = require("./inventory");

        //return an object to define the "my/shirt" module.
        return {
            color: "blue",
            size: "large",
            addToCart: function() {
                inventory.decrement(this);
                cart.add(this);
            }
        }
    });

The CommonJS style eliminates a whole class of programmer error. Sure you might have a few extra lines of code, but you've removed the need for the mental overhead of making sure the order is right in both places.
