import pandas as pd
import matplotlib.pyplot as plt


def visualize_monthly_avg_sleep(sleep: pd.Series, title=''):
    sleep = sleep.replace(0, sleep.mean())
    sleep = sleep.resample('M').mean()

    sleep.index = [sleep.index.strftime('%m-%d'), sleep.index.year]
    sleep = sleep.unstack()

    sleep.index = pd.to_datetime(sleep.index, format='%m-%d').month_name()

    fig, ax = plt.subplots(figsize=(12, 4))

    sleep.plot(kind='bar', ax=ax, legend=False)

    fig.legend(loc='lower center', ncol=3)

    min = sleep.min().min()
    max = sleep.max().max()
    mean = sleep.mean()

    ax.set_ylim([min * 0.9, max*1.1])
    ax.set_title(title)

    min_index = sleep[sleep == min].dropna(
        axis=1, how='all').dropna(axis=0).index
    max_index = sleep[sleep == max].dropna(
        axis=1, how='all').dropna(axis=0).index

    ax.annotate(f'min: {round(min,2)}',
                xy=(sleep.index.get_loc(min_index[0]), min),
                )

    ax.annotate(f'max: {round(max,2)}',
                xy=(sleep.index.get_loc(max_index[0]), max),
                )
    cmap = plt.get_cmap("tab10")

    c = 0
    for i, v in mean.items():
        ax.axhline(v, c=cmap(c))
        ax.annotate(f'{round(v,2)}',
                    xy=(11, v),
                    )
        c = c+1

    fig.tight_layout()

    plt.show()


def visualize_weekly_avg_sleep(sleep: pd.Series):
    sleep = sleep.replace(0, sleep.mean())
    sleep = sleep.resample('W').mean()

    sleep.index = [sleep.index.isocalendar().week, sleep.index.year]
    sleep = sleep.unstack()

    # sleep.index = sleep.index.isocalendar().week

    fig, ax = plt.subplots(figsize=(12, 4))

    sleep.plot(kind='bar', ax=ax, legend=False)

    fig.legend(loc='lower center', ncol=3)

    min = sleep.min().min() * 0.9
    max = sleep.max().max() * 1.1

    ax.set_ylim([min, max])

    ax.set_title('Weekly Average Night Sleeping Time')

    fig.tight_layout()
    plt.show()
