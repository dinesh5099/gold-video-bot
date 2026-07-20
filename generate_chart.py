import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def create_price_chart(prices, output_path="gold_chart.png"):
    days = [datetime.now() - timedelta(days=x) for x in range(len(prices)-1, -1, -1)]
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    
    ax.plot(days, prices, color='#FFD700', linewidth=3, marker='o', markersize=8)
    ax.fill_between(days, prices, min(prices)-10, alpha=0.2, color='#FFD700')
    
    ax.set_title('Gold Price - Last 7 Days', fontsize=28, color='white', pad=20)
    ax.set_ylabel('Price (USD/oz)', fontsize=18, color='white')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, facecolor='#1a1a1a', bbox_inches='tight')
    plt.close()
    return output_path
