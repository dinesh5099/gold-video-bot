def generate_script(current_price, prices, change_pct):
    direction = "up" if change_pct > 0 else "down"
    
    script = f"""
    Here's today's gold price update.
    Gold is currently trading at {current_price} dollars per ounce.
    That's {direction} {abs(change_pct):.1f} percent compared to yesterday.
    
    Over the past week, gold has ranged between {min(prices)} and {max(prices)} dollars.
    
    Investors continue to watch inflation data and Federal Reserve signals 
    for the next major move in precious metals.
    
    That's your gold market update. Stay tuned for tomorrow's report.
    """
    return script.strip()
