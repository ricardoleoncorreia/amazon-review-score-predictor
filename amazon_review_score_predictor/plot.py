from typing import Literal, Optional, TypedDict
import matplotlib.pyplot as plt
import seaborn as sns

class PlotParams(TypedDict):
  x: any
  title: str
  xlabel: str
  ylabel: str
  labelrotation: int
  y: Optional[any]
  hue: Optional[str]

class PlotUtils:
  @staticmethod
  def create_plot(
    type: Literal["bar", "line"],
    x: str,
    hue: str,
    title: str,
    xlabel: str,
    ylabel: str,
    data = None,
    y: str | None = None,
    fontsize: int = 16,
    order: list | None = None,
    palette: str = "deep",
    xtick_rotation: int = 0,
    ytick_rotation: int = 0,
    figsize: tuple[int, int] = (20, 5),
    legend: bool = False,
    standalone: bool = True,
  ) -> None:
    if standalone:
      plt.figure(figsize=figsize)

    if type == "bar":
      g = sns.barplot(x=x, y=y, hue=hue, data=data, palette=palette, legend=legend, order=order)
    elif type == "count":
      g = sns.countplot(x=x, hue=hue, data=data, palette=palette, legend=legend, order=order)
    elif type == "line":
      g = sns.lineplot(x=x, y=y, hue=hue, data=data, palette=palette, legend=legend)
    else:
      raise ValueError("Type must be either 'bar' or 'line'")

    g.set_title(title, fontsize=2 * fontsize)
    g.set_xlabel(xlabel, fontsize=fontsize)
    g.set_ylabel(ylabel, fontsize=fontsize)
    g.tick_params(axis='x', labelsize=fontsize, labelrotation=xtick_rotation)
    g.tick_params(axis='y', labelsize=fontsize, labelrotation=ytick_rotation)

    if standalone:
      plt.show()

  @staticmethod
  def create_comparison_plot(
    title: str,
    params: list[PlotParams],
    fontsize: int = 16,
    palette: str = "deep",
    figsize: tuple[int, int] = (15, 8),
  ) -> None:
    fig, axes = plt.subplots(1, len(params), figsize=figsize)
    fig.suptitle(title, fontsize=2 * fontsize)

    for ax, param in zip(axes, params):
      PlotUtils.create_plot(
        type="bar",
        x=param.get("x"),
        y=param.get("y"),
        hue=param.get("hue"),
        title=param["title"],
        xlabel=param["xlabel"],
        ylabel=param["ylabel"],
        fontsize=fontsize,
        palette=palette,
        xtick_rotation=param["labelrotation"],
        legend=False,
        standalone=False,
      )
      plt.sca(ax)

    plt.show()
