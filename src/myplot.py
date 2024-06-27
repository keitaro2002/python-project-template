import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from cycler import cycler


# https://qiita.com/aurueps/items/d04a3bb127e2d6e6c21b
plt.rcParams["figure.dpi"] = 150            # dpi
plt.rcParams["font.size"] = 14              # 基本となるフォントの大きさ

plt.rcParams["xtick.direction"] = "out"      # 目盛り線の向き、内側"out"か外側"out"かその両方"inout"か
plt.rcParams["ytick.direction"] = "out"      # 目盛り線の向き、内側"in"か外側"out"かその両方"inout"か
plt.rcParams["xtick.top"] = False            # 上部に目盛り線を描くかどうか
plt.rcParams["xtick.bottom"] = False         # 下部に目盛り線を描くかどうか
plt.rcParams["ytick.left"] = False           # 左部に目盛り線を描くかどうか
plt.rcParams["ytick.right"] = False          # 右部に目盛り線を描くかどうか
plt.rcParams["xtick.major.size"] = 6.0      # x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 6.0      # y軸主目盛り線の長さ
plt.rcParams["xtick.major.width"] = 1.0     # x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 1.0     # y軸主目盛り線の線幅
plt.rcParams["xtick.minor.visible"] = False # x軸副目盛り線を描くかどうか
plt.rcParams["ytick.minor.visible"] = False # y軸副目盛り線を描くかどうか
plt.rcParams["xtick.minor.size"] = 4.0      # x軸副目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 4.0      # y軸副目盛り線の長さ
plt.rcParams["xtick.minor.width"] = 0.6     # x軸副目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 0.6     # y軸副目盛り線の線幅
plt.rcParams["xtick.labelsize"] = 14        # 目盛りのフォントサイズ
plt.rcParams["ytick.labelsize"] = 14        # 目盛りのフォントサイズ

plt.rcParams["axes.linewidth"] = 1.0        # グラフ囲う線の太さ

plt.rcParams["legend.loc"] = "best"         # 凡例の位置、"best"でいい感じのところ
plt.rcParams["legend.frameon"] = True       # 凡例を囲うかどうか、Trueで囲う、Falseで囲わない
plt.rcParams["legend.framealpha"] = 0.8     # 透過度、0.0から1.0の値を入れる
plt.rcParams["legend.facecolor"] = "white"  # 背景色
plt.rcParams["legend.edgecolor"] = "black"  # 囲いの色
plt.rcParams["legend.fancybox"] = False     # Trueにすると囲いの四隅が丸くなる
plt.rcParams["lines.linewidth"] = 1.0      # グラフの線の太さ

apple_colors = [
    '#007aff',
    '#ff9500',
    '#34c759',
    '#ff3b30',
    '#af52de',
    '#a2845e',
    '#ffcc00',
    '#00c7be',
]

plt.rcParams['axes.prop_cycle'] = cycler(color=apple_colors)


def save(fig: Figure, path: str, *args, **kwargs):
    fig.savefig(path, bbox_inches='tight', pad_inches=0.05, *args, **kwargs)