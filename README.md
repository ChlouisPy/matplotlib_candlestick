# matplotlib_candlestick
This script allow you to create custom Matplotlib candlestick graph

## How to use:

- First you must import candlestick.py
````python
import candlestick
````

### There is two function in this program:

- #### create_color_config():
    This function allow you to create your custom candlestick.
    There are multiples arguments on this function 
    * name (*required*): *str*: The name of your candlestick style
    * red: *str*: the color of the candle when it decreases (hexadecimal color RGBA or RGB as str)
    * green: *str*: the color of the candle when it increases (hexadecimal color RGBA or RGB as str)
    * border_increase: *str*: the color of the boarder when candle increase (hexadecimal color RGBA or RGB as str)
    * border_decrease: *str*: the color of the boarder when candle decrease (hexadecimal color RGBA or RGB as str)
    * wick_increase: *str*: the color of the wick when candle increase (hexadecimal color RGBA or RGB as str)
    * wick_decrease: *str*: the color of the wick when candle decrease (hexadecimal color RGBA or RGB as str)
      
    * alpha: *float*: transparency of the candle
    * border_width: *float*: the width of the boarder
    * candle_width: *float*: the width of the candle 
    * wick_width: *float*: the with of the wick

- #### plot_candle():
    This function get you Matplotlib plot and add all candles.
    There are multiples arguments on this function
    * ax (*required*):  Your matplotlib ax
    * stock_data (*required*): *np.array*: an array of shape (n, 4) or (n, 5) for axis=0 and (4, n) or (5, n) for axis=1
    * config_name: str: the name of the candlestick style
    * axis: int: the type on array you use 1 or 0 (base is 0)
    
- ### How to use plot_candle()

    This function has two input possibles for *stock_data* and to type on axis:
    
    #### axis=0
    
    - Input of shape (n, 4):
        ```python
        stock_data = np.array([
                              [open0, high0, low0, close0],
                              [open1, high1, low1, close1],
                              [open2, high2, low2, close2],
                              ...
                              [openX, highX, lowX, closeX]
                              ])
        ```
      In this case the index in n correspond to the horizontal axis value on the plot
      <br>
      <br>
    - Input os shape (n, 5):
        ```python
        stock_data = np.array([
                              [0, open0, high0, low0, close0],
                              [1, open1, high1, low1, close1],
                              [2, open2, high2, low2, close2],
                              ...
                              [X, openX, highX, lowX, closeX]
                              ])

        ```
      In this case the value X will correspond to the horizontal axis value on the plot
      <br>
      <br>
      
      #### axis=1
      ```python
      stock_data = np.array([
                              [open0, open1, open2, ... openX],
                              [high0, high1, high2, ... highX],
                              [low0, low1, low2, ... lowX],
                              [close0, close1, close2, ... closeX],
                              [0, 1, 2, ... X],
                            ])
        ```
        or
        ```python
        stock_data = np.array([
                              [open0, open1, open2, ... openX],
                              [high0, high1, high2, ... highX],
                              [low0, low1, low2, ... lowX],
                              [close0, close1, close2, ... closeX],
                            ])
        ```
- ### Style already in candlestick.py:
    
- #### base
![alt text](https://github.com/ChlouisPy/matplotlib_candlestick/blob/main/images/base.png?raw=true)
- #### Hollow
![alt text](https://github.com/ChlouisPy/matplotlib_candlestick/blob/main/images/hollow.png?raw=true)
- #### Simple
![alt text](https://github.com/ChlouisPy/matplotlib_candlestick/blob/main/images/simple.png?raw=true)
- #### Black
![alt text](https://github.com/ChlouisPy/matplotlib_candlestick/blob/main/images/black.png?raw=true)


- ## Requirement:
- library     (*version that i use*)
- Matplotlib  (*3.3.3*)
- Numpy       (*1.18.0*)

- ## Credit:
- [ChlouisPy](https://github.com/ChlouisPy/)
