# Pool Fractals Drawer

This is a simple program that calculate then draws pool fractals. It is written in Python.
Pool Fractals are done by considering a ball bouncing at 90° on a pool table each time an edge is encountered. 
The pool table is divided in a grid (the input of the program and) and only half of the path is drawn.
The ball always starts in a corner and end in another:

<p style="text-align: center;"><img src="https://user-images.githubusercontent.com/35769613/222894221-e2d6b09c-9fc1-4b0d-9484-abe984068733.png" width="300"></p>

## How to use

This program requires python 3 to be installed. Dependencies can be installed using pip:
```bash
pip install -r requirements.txt
python main.py
```
You are then asked to enter the size of the grid (the number of squares on each side).
The program will then calculate the fractal and draw it in a window.

## Examples

Different sizes of grid result in different patterns. Here are some examples:

<p style="text-align: center;">
<img src="https://user-images.githubusercontent.com/35769613/222895332-ba3aa61b-82bd-4358-8b8a-3356a42aac18.png" height="200">
<img src="https://user-images.githubusercontent.com/35769613/222895354-08897310-db1f-44b9-aa8e-f4ae505e41e5.png" height="200">
</p>

Those 2 are generated using two consecutive number of the fibonacci sequence as the grid size (21, 13) and (144, 89).
Both image result in the same pattern and the ratio between the two dimensions of the grid is an approximation of the golden ratio (1.61803398875) : 21/13 = 1,61538462 and 144/89 = 1,61797753.

<p style="text-align: center;">
<img src="https://user-images.githubusercontent.com/35769613/222895524-0bd66e71-f5e5-4c15-9e71-2b3b5c4b06ff.png" height="200">
</p>
When observing this pattern, it is possible to estimate pi using the dimension of the grid: 223/71 = 3,14084507 ~ pi

More patterns can be obtained. Feel free to try out!

## References

More information about pool fractals can be found here: http://xcont.com/