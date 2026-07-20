from fetch_data import get_gold_price_data, get_historical_prices
from generate_chart import create_price_chart
from generate_script import generate_script
from generate_audio import create_audio
from assemble_video import create_video

def run_pipeline():
    print("1. Fetching data...")
    current_price = get_gold_price_data()
    history = get_historical_prices()
    change_pct = ((history[-1] - history[-2]) / history[-2]) * 100
    
    print("2. Creating chart...")
    chart_path = create_price_chart(history)
    
    print("3. Generating script...")
    script = generate_script(current_price, history, change_pct)
    print(f"Script:\n{script}\n")
    
    print("4. Generating audio...")
    audio_path = create_audio(script)
    
    print("5. Assembling video...")
    video_path = create_video(chart_path, audio_path)
    
    print(f"Done! Video saved to {video_path}")
    return video_path

if __name__ == "__main__":
    run_pipeline()
