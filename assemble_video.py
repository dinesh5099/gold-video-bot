from moviepy.editor import *

def create_video(image_path, audio_path, output_path="gold_update.mp4"):
    audio = AudioFileClip(audio_path)
    duration = audio.duration
    
    image_clip = ImageClip(image_path).set_duration(duration)
    image_clip = image_clip.resize(height=1080)
    
    def zoom(t):
        return 1 + 0.02 * t
    
    image_clip = image_clip.resize(zoom)
    
    final = image_clip.set_audio(audio)
    final.write_videofile(
        output_path,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        preset='medium'
    )
    return output_path
