"""
Function to plot in matplotlib stock candlestick from numpy array
the numpy array can contain 4 or 5 values [(time), open, high, low, close]

GitHub: ChlouisPy
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# BASE CONFIGURATION
# base color RGBA
RED: str = "#ED1C24FF"
GREEN: str = "#22B14CFF"
BLACK: str = "#000000FF"
WHITE: str = "#FFFFFFFF"
TRANSPARENT: str = "none"

# base alpha information
BASE_ALPHA: float = 1.0

# base size
BORDER_WIDTH: float = 1
CANDLE_WIDTH: float = 0.5
WICK_WIDTH: float = 0.00025

# plot option
PLOT_PADDING_RATE = 1

# pre created configuration
"""
red: the color of the candle when it decrease (hexadecimal color RGBA or RGB as str)
green: the color of the candle when it increase (hexadecimal color RGBA or RGB as str)
border_i: the color of the boarder when candle increase (hexadecimal color RGBA or RGB as str)
border_d: the color of the boarder when candle decrease (hexadecimal color RGBA or RGB as str)
wick_i: the color of the wick when candle increase (hexadecimal color RGBA or RGB as str)
wick_d: the color of the wick when candle decrease (hexadecimal color RGBA or RGB as str)
alpha: transparency of the candle (float)
border_w: the width of the boarder (float)
candle_w: the width of the candle (float)
wick_w: the with of the wick (float)
"""
CANDLE_CONFIG: dict = {}

CANDLE_CONFIG["base"]: dict = {"red": RED,
                               "green": GREEN,
                               "border_i": BLACK,
                               "border_d": BLACK,
                               "wick_i": BLACK,
                               "wick_d": BLACK,
                               "alpha": BASE_ALPHA,
                               "border_w": BORDER_WIDTH,
                               "candle_w": CANDLE_WIDTH,
                               "wick_w": WICK_WIDTH,
                               }

CANDLE_CONFIG["hollow"]: dict = {"red": TRANSPARENT,
                                 "green": TRANSPARENT,
                                 "border_i": GREEN,
                                 "border_d": RED,
                                 "wick_i": GREEN,
                                 "wick_d": RED,
                                 "alpha": BASE_ALPHA,
                                 "border_w": BORDER_WIDTH,
                                 "candle_w": CANDLE_WIDTH,
                                 "wick_w": WICK_WIDTH
                                 }

CANDLE_CONFIG["simple"]: dict = {"red": RED,
                                 "green": GREEN,
                                 "border_i": TRANSPARENT,
                                 "border_d": TRANSPARENT,
                                 "wick_i": GREEN,
                                 "wick_d": RED,
                                 "alpha": BASE_ALPHA,
                                 "border_w": BORDER_WIDTH,
                                 "candle_w": CANDLE_WIDTH,
                                 "wick_w": WICK_WIDTH
                                 }

CANDLE_CONFIG["black"]: dict = {"red": TRANSPARENT,
                                "green": TRANSPARENT,
                                "border_i": BLACK,
                                "border_d": BLACK,
                                "wick_i": BLACK,
                                "wick_d": BLACK,
                                "alpha": BASE_ALPHA,
                                "border_w": BORDER_WIDTH,
                                "candle_w": CANDLE_WIDTH,
                                "wick_w": WICK_WIDTH
                                }


def create_color_config(
        name: str,
        red: str = RED,
        green: str = GREEN,
        border_increase: str = BLACK,
        border_decrease: str = BLACK,
        wick_increase: str = BLACK,
        wick_decrease: str = BLACK,
        alpha: float = BASE_ALPHA,
        border_width: float = BORDER_WIDTH,
        candle_width: float = CANDLE_WIDTH,
        wick_width: float = WICK_WIDTH) -> None:
    """
    This function add a new configuration to the CANDLE_CONFIG dictionary
    warning : You can't add a new candle configuration with the same name as another

    :param name: the name of your new configuration
    :param red: the color of the candle when it decrease (hexadecimal color RGBA or RGB as str)
    :param green: the color of the candle when it increase (hexadecimal color RGBA or RGB as str)
    :param border_increase: the color of the boarder when candle increase (hexadecimal color RGBA or RGB as str)
    :param border_decrease: the color of the boarder when candle decrease (hexadecimal color RGBA or RGB as str)
    :param wick_increase: the color of the wick when candle increase (hexadecimal color RGBA or RGB as str)
    :param wick_decrease: the color of the wick when candle decrease (hexadecimal color RGBA or RGB as str)
    :param alpha: transparency of the candle (float)
    :param border_width: the width of the boarder (float)
    :param candle_width: the width of the candle (float)
    :param wick_width: the with of the wick (float)
    :return: None
    """
    global CANDLE_CONFIG

    # check if the name is already used
    name_list = list(CANDLE_CONFIG.keys())

    if name in name_list:
        print("The name of your configuration is already used")
        return None

    # add the new configuration
    CANDLE_CONFIG[name]: dict = {"red": red,
                                 "green": green,
                                 "border_i": border_increase,
                                 "border_d": border_decrease,
                                 "wick_i": wick_increase,
                                 "wick_d": wick_decrease,
                                 "alpha": alpha,
                                 "border_w": border_width,
                                 "candle_w": candle_width,
                                 "wick_w": wick_width
                                 }

    print("New configuration successfully added")


def plot_candle(
        ax,
        stock_data: np.array,
        config_name: str = "base",
        axis=0):
    """
    This function will plot all candles from the numpy array

    stock_data configuration :
    There is two way to create the stock_data array:
     - the first way is only with important data like, open ; high ; low ; close. If you do that the array should
       look's like :

        ########## axis=0 ##########

       stock_data = np.array([
                              [open0, high0, low0, close0],
                              [open1, high1, low1, close1],
                              [open2, high2, low2, close2],
                              ...
                              [openX, highX, lowX, closeX]
                            ])
        with this method the row of the data correspond to the horizontal axis value on the plot

    - the second way is with five information, time ; open ; high ; low ; close If you do that the array should
       look's like :

       stock_data = np.array([
                              [0, open0, high0, low0, close0],
                              [1, open1, high1, low1, close1],
                              [2, open2, high2, low2, close2],
                              ...
                              [X, openX, highX, lowX, closeX]
                            ])
       with this method the vale in the first index of a raw correspond to the horizontal axis value on the plot

       ########## axis=1 ##########

       stock_data = np.array([
                              [open0, open1, open2, ... openX],
                              [high0, high1, high2, ... highX],
                              [low0, low1, low2, ... lowX],
                              [close0, close1, close2, ... closeX],
                              [0, 1, 2, ... X],
                            ])

        or

        stock_data = np.array([
                              [open0, open1, open2, ... openX],
                              [high0, high1, high2, ... highX],
                              [low0, low1, low2, ... lowX],
                              [close0, close1, close2, ... closeX],
                            ])

    Warning : for X value in second type of array, you should use int > 1 between two value, because your candle can
              collide, if you want use smallest value between two candle you should crete your own CANDLE_CONFIG with
              the create_color_config() function and change the border_width, candle_width and wick_width parameter

    :param ax: a matplotlib ax where you want plot yours candles
    :param stock_data: np.array of shape (n, 4) or (n, 5) with float or int
    :param config_name: the name of the graphical configuration for the plotting
    :param axis: how your data are organised
    :return: None
    """

    candle_config: dict = {}

    # check if the config name exist
    if config_name not in list(CANDLE_CONFIG.keys()):
        print("The name of your configuration do not exist")
        candle_config = CANDLE_CONFIG["base"]

    else:
        candle_config = CANDLE_CONFIG[config_name]

    if axis == 0:
        R = range(len(stock_data))

        if len(stock_data[0]) == 4:
            # mode without index
            P = 0

        else:
            # mode with index
            P = 1

            # first plot a invisible line to force plot size
            ax.plot(
                np.array([0 / PLOT_PADDING_RATE, len(stock_data) * PLOT_PADDING_RATE]),
                np.array([max(stock_data[:, P:].flatten().tolist()) * PLOT_PADDING_RATE,
                          min(stock_data[:, P:].flatten().tolist()) / PLOT_PADDING_RATE]),
                c=TRANSPARENT
            )

    else:
        R = range(len(stock_data[0]))

        if len(stock_data) == 4:
            # mode without index
            P = 0

        else:
            # mode with index
            P = 1

        # first plot a invisible line to force plot size
        ax.plot(
            np.array([0 / PLOT_PADDING_RATE, len(stock_data) * PLOT_PADDING_RATE]),
            np.array([max(stock_data[P:, :].flatten().tolist()) * PLOT_PADDING_RATE,
                      min(stock_data[P:, :].flatten().tolist()) / PLOT_PADDING_RATE]),
            c=TRANSPARENT
        )

    # for each lines in stock data
    for i in range(len(stock_data[0])):

        # get every data
        if axis == 0:
            _open = stock_data[i][0 + P]
            high = stock_data[i][1 + P]
            low = stock_data[i][2 + P]
            close = stock_data[i][3 + P]

            # coordinate where to plot the candle
            if P == 1:
                x_c = stock_data[i][0]
            else:
                x_c = i

        else:
            _open = stock_data[0 + P][i]
            high = stock_data[1 + P][i]
            low = stock_data[2 + P][i]
            close = stock_data[3 + P][i]

            # coordinate where to plot
            if P == 1:
                x_c = stock_data[0][i]
            else:
                x_c = i

        # if the stock increase
        if _open <= close:

            # plot wick on bottom of the candle
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["wick_w"], low),  # set coordinate of the lowest point
                    candle_config["wick_w"] * 2,  # set the full width of the wick
                    _open - low,  # set the highest point
                    color=candle_config["wick_i"],
                    alpha=candle_config["alpha"]
                )
            )

            # plot wick on top of the candle
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["wick_w"], close),  # set coordinate of the lowest point
                    candle_config["wick_w"] * 2,  # set the full width of the wick
                    high - close,  # set the highest point
                    color=candle_config["wick_i"],
                    alpha=candle_config["alpha"]
                )
            )

            # plot color
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["candle_w"] / 2, _open),  # set starting point
                    candle_config["candle_w"],
                    close - _open,
                    color=candle_config["green"],
                    alpha=candle_config["alpha"],
                    ec=candle_config["border_i"],
                    lw=candle_config["border_w"]

                )
            )

        # if the stock decease
        else:
            # plot wick on bottom of the candle
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["wick_w"], low),  # set coordinate of the lowest point
                    candle_config["wick_w"] * 2,  # set the full width of the wick
                    close - low,  # set the highest point
                    color=candle_config["wick_d"],
                    alpha=candle_config["alpha"]
                )
            )

            # plot wick on top of the candle
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["wick_w"], _open),  # set coordinate of the lowest point
                    candle_config["wick_w"] * 2,  # set the full width of the wick
                    high - _open,  # set the highest point
                    color=candle_config["wick_d"],
                    alpha=candle_config["alpha"]
                )
            )

            # plot color
            ax.add_patch(
                Rectangle(
                    (x_c - candle_config["candle_w"] / 2, _open),  # set starting point
                    candle_config["candle_w"],
                    close - _open,
                    color=candle_config["red"],
                    alpha=candle_config["alpha"],
                    ec=candle_config["border_d"],
                    lw=candle_config["border_w"]

                )
            )

    return ax
