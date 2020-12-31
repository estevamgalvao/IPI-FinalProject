# Final Project: Toonify Filter

Implementation of an image processing algorithm inspired by [Kevin Dade Toonify Paper](https://github.com/estevamgalvao/IPI-FinalProject/blob/master/Dade_Toonify.pdf).
The main proposal of the project is to achieve a friendly photo filter that transform every photo to a similar cartoon picture up to 5 seconds using Python.

### Main Functions
- cv2.medianBlur
- cv2.Canny
- cv2.bilateralFilter
- cv2.kmeans

### Conclusion
The algorithm does not satisfy every kind of photo - e.g. selfies - but in the most cases had a great result, mainly in the stronger colours cases.
> Average Speed of Filtering: 4.06 seconds/HD image


### References
- [Kevin Dade Toonify Paper](https://github.com/estevamgalvao/IPI-FinalProject/blob/master/Dade_Toonify.pdf)
- [Bilateral Filtering for Gray and Color Images](http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html)
- [In Depth: k-means Clustering](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)
- [Docs OpenCV](https://docs.opencv.org/3.1.0/index.html)
- [Images Database](https://wallpaperscraft.com/)
