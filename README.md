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
    * stock_data (*required*): *np.array*: an array of shape (n, 4) or (n, 5)
    * config_name: str: the name of the candlestick style
    
- ### How to use plot_candle()

    This function has to input possibles for *stock_data*:
    
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
