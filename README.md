# Using [Open CV](https://opencv.org/about/) 
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/100px-OpenCV_Logo_with_text_svg_version.svg.png)  
### Projects:

1. _Face Recognition on pictures._
2. _Face recognition in real time._
3. _Car recognition._
4. _Car & pedestrian recognition._
5. _Smile recognition._


**What's _Open CV_?**

**Open** Source **C**omputer **V**ision is a computer vision and machine learning software library.
It has more than 2500 optimized algorithms, including _classic & state-of-the-art computer vision_ and _machine learning_. 

It has C++, Python, Java and Matlab interfaces and supports Windows, Linux, Android, and MacOS. 

Some uses of this algorithms are face recognition, identificate objects, classify human actions, tracking movements and more. For these projects I'll be using 4 of these algorithms which are:

- Project 1, 2 & 5: [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xmlhttps://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- Project 3:
- Project 4: [haarcascade_fullbody.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml)
- Project 5: [haarcascade_smile.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml)

[Here](https://github.com/opencv/opencv) you can find all the algorithms and more files from **OpenCV**. In order to review every project just select on the branches section the one of your interest, but before let's explain how the code is 
structured.

Even though we have 3 different projects, they share the same structure of code:

1. At the beginning we import **OpenCV** library and save in a variable the _haarcascade algorithm_ that we will use. Furthermore we type the source to be analysed (from photo,video or webcam).  

