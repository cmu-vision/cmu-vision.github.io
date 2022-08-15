## cmu-vision-web

### Homepage item

Add a `contentItem` div block to `index.html` within `content` div block.
```html
<div class="contentItem">

    <!-- news title -->
    <div class="leftWrap">
        <span id="post2117"></span>
        <h2 class="title">CMU Vision Papers at CVPR 2022</h2>
        <span class="date">19 June 2022</span>
    </div>

    <!-- news body -->
    <div class="newsItemWrapperLeft">
        <table class="newsItem">
            <tr>
                <td><span class="image"><img alt="News" src="./assets/vibration.png" width="500.5"
                            height="324" /></span></td>
                <td>
                    <div class="newsText"><a
                            href="http://graphics.cs.cmu.edu/wp/wp-content/uploads/2020/09/single_source_logmap.jpg"></a><span
                            class="hspace"></span>
                        CMU Vision will be at CVPR 2022!<span class="hspace"></span>
                        <ul><span class="hspace"></span>
                            <li><a href="https://imaging.cs.cmu.edu/vibration/">Dual-Shutter Optical
                                    Vibration Sensing</a><br>Mark Sheinin, Dorian Chan, Matthew O'Toole,
                                Srinivas Narasimhan</li><span class="hspace"></span>
                            <li><a href="https://shubhtuls.github.io/ss3d/">Pre-train, Self-train,
                                    Distill: A simple recipe for Supersizing 3D
                                    Reconstruction</a><br>Kalyan
                                Vasudev Alwala, Abhinav Gupta, Shubham Tulsiani</li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table> <!-- newsItem -->
    </div> <!-- newsItemWrapper -->
    
</div>
<hr>
```

### People item
Add a `personTable`block under the appropriate header category. 
```html
<table class="personTable">
    <!-- photo -->
    <tr>
        <td>
            <a href="./people.html">
                <div class="imButtonWrapper">
                    <img alt="Prof. X" src="assets/incognito.jpeg" />
                </div>
            </a>
        </td>
    </tr>
    
    <!--  name -->
    <tr>
        <td>
            <a href="./people.html">
                Prof. X</a>
        </td>
    </tr>
</table> <!-- personTable -->
```

### Course item
Add a `courselistItem` div block within `contentItem` div. This adds one course item with space for one more course item in the same row. To add a course in the same row, fill the two empty table data (`td`) elements with the same structure as the first two elements.
```html
<div class="courselistItem">

    <div class="buttonWrapper">
        <table class="course">
            <tr>
                <!-- course 1 -->
                <td>
                    <div class="cropTeaser" style="background-image: url('assets/thumbnail.png');">
                    </div>
                </td>
                <td class="courseDescription">
                    <h2 class="courseTitle">
                        16-385 / Computer Vision </h2>
                    This course provides a comprehensive introduction to computer vision. Major topics
                    include image processing, detection
                    and recognition, geometry-based and physics-based vision and video analysis.
                    Students will learn basic concepts of
                    computer vision as well as hands on experience to solve real-life vision problems.
                    <p class="offeringList"><a href="./index.html">Course website</a></p>
                </td>
                <!-- course 2 -->
                <td></td>
                <td></td>
            </tr>
        </table> <!-- course x 2-->
    </div>
</div> <!-- contentItem -->
```
