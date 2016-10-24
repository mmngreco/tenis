import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
from IPython.display import set_matplotlib_formats
# formato de los gráficos
plt.style.use(['seaborn-white', 'seaborn-paper'])
set_matplotlib_formats('svg', 'png')
plt.rcParams['savefig.dpi'] = 75

plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 10, 6
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14

# plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "Times New Roman"
plt.rcParams['font.serif'] = "cm"
# plt.rcParams['text.latex.preamble'] = u"\\usepackage{subdepth}, \\usepackage{type1cm}"

path = '/Users/mmngreco/Documents/apuestas/code'

data = pd.read_excel("../data/rto_por_torneo.xlsx")
data.describe()
data.columns = "tournament games yield lay win pg rate ratelay".split()


sns.pairplot(data=data, hue="win")
sns.pairplot(data=data, hue="win")
