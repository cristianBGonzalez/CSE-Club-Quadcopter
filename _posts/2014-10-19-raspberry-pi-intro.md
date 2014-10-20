---
layout: post
title: "Raspberry Pi Intro"
description: ""
category: 
tags: ["PI"]
---
{% include JB/setup %}

##Raspberry PI and PWM Intro

Hello everyone this is an intro to get everyone of those who are not used to Raspberry PI up to speed on how things will be done. First of all the objective at this phase of the project is to enable control of the motors. To control anything we will need to control the GPIO (or general purpose input output) pins, which shall be done using the Wiring PI library using Python programming language. Additionally, pulse width modulation and a PID controller will be necessary to control the motors. Now to prepare for the project I suggest the following:

<ul>
	<li>Codeacademy to learn <a href="http://www.codeacademy.com">Python</a> make an account and start learning the syntax</li>
	<li>For learning the WiringPython library there is the official <a href="http://wiringpi.com/reference/">website reference</a>. Please note that while this is for C or C++ version we can use these function by adding "wiringpi2." in front of the function for the python version.</li>
	<li>An intro to <a href="http://www.embedded.com/electronics-blogs/beginner-s-corner/4023833/Introduction-to-Pulse-Width-Modulation">PWM</a></li>
	<li>An intro to <a href="http://www.ni.com/white-paper/3782/en/">PID Controllers</a></li>
	<li>Finally, a paper on using <a href="http://www.academia.edu/5091119/Design_of_Quadrotor_Hovering_System_Based_on_Inertial_Measurement_Unit_Sensor">PID on a quadcopter</a>. This one is of particular use since it talks about four PID controllers all being used to control pitch, yaw, roll, and altitude and how each contributes to the overal output to each motor.</li>
</ul>

I know this is a lot to absorb, but remember this is a serious engineering project. Thus this will be a great learning experience for all of us so long as we put the work needed into this project.