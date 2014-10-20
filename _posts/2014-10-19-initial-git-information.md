---
layout: post
title: "Initial Git Information"
description: ""
category: 
tags: ["general"]
---
{% include JB/setup %}

##Welcome to the project everybody!

Hello this is an introduction to what each contributor needs to do for the project I shall cover some of the basics for helping out with this project. Before you begin though make sure that you have a github account and have it setup on your computer.

So the repository page of the project is: https://github.com/egonzalezjr555/CSE-Club-Quadcopter. When you get there you will need to focus on making own copy of the repository which you shall do by clicking on the button that says fork. After that you will need to copy that repository to your computer using git. To do this you must first go to the the directory in which you want to be in either through the cmd or some other terminal program. After that you will need  to get the SSH clone url (from your account) and copy it. Type the following command in your terminal.

{% highlight bash %}
git clone "paste  SSH url here"
{% endhighlight %}

To keep our project organized we have decided to split the project into different branches as of this moment we have the master, IMU, Raspberry-PI, and gh-pages branches. The master will be the main branch and where all the code and documentation will end up in. For now all you need to know is that you will be working on your branch and will need to switch to your branch by typing command.

{% highlight bash %}
git checkout "name of branch"
{% endhighlight %}

or as  a more specific example.

{% highlight bash %}
git checkout IMU
{% endhighlight %}

I should note that right now we are pretty much starting from scratch so there is no need to synchronize your repository, but eventually we will need to, so I will post more info on doing that later.

Moving forward after you make changes that you need to make you need to push those changes to your repository and these can be done by typing the following commands:

{% highlight ruby %}
git add -A
git commit -m "Type a message about your push here"
git push origin "Name of branch"
{% endhighlight %}

Finally, go back to the main repository and issue a pull request from your branch to the branch in the main repository. This is done by going to https://github.com/egonzalezjr555/CSE-Club-Quadcopter and clicking on the button to create pull requests located to the left and directly on top of where the files are listed. Before initiating the pull request, make sure that you switch to the correct branch. After initiating a pull request it will initiate a review of it in which the request shall be merged or denied.