import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    # Load and clean the data
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    lower_limit = df['value'].quantile(0.025)
    upper_limit = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

    # Draw line plot
    plt.figure(figsize=(12, 6))
    plt.plot(df_clean.index, df_clean['value'], color='r', label='Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.legend()
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    # Load and clean the data
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    lower_limit = df['value'].quantile(0.025)
    upper_limit = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

    # Prepare data for bar plot
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.month
    df_grouped = df_clean.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    df_grouped.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    # Load and clean the data
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    lower_limit = df['value'].quantile(0.025)
    upper_limit = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]

    # Prepare data for box plot
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.month

    # Draw year-wise box plot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='value', data=df_clean)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('box_plot_year.png')
    plt.show()

    # Draw month-wise box plot
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='month', y='value', data=df_clean)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('box_plot_month.png')
    plt.show()
