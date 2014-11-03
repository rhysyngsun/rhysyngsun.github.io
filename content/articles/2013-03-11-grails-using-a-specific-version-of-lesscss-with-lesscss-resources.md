Title: Grails - Using a specific version of LessCSS with lesscss-resources
Date: 2013-03-11 09:30:00 -0400
Tags: Grails, Grails Plugin, Less

A few days ago I was trying to integrate the [twitter-bootstrap](http://grails.org/plugin/twitter-bootstrap) Grails plugin into an app but was
    having difficulty getting the less sources to play nice with the [lesscss-resources](http://grails.org/plugin/lesscss-resources) plugin.

[It turned out](https://github.com/paulfairless/grails-lesscss-resources/issues/45) that the most recent
    version of bootstrap used LessCSS syntax that is only available in the 1.3.3 version of the lesscss compiler. The
    lesscss-resources depends on version 1.3.1, so to work around that issue you can update your BuildConfig.groovy settings to the following to force a specific version of the lesscss compiler:


    :::groovy
    grails.project.dependency.resolution = {
        dependencies {
            runtime ('org.lesscss:lesscss:1.3.3')
        }
        plugins {
            compile(":lesscss-resources:1.3.1") {
                excludes "lesscss"
            }
        }
    }
