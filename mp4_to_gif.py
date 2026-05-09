from moviepy import VideoFileClip

def convert_and_compress_to_gif(input_path, output_path):
    # ==========================================
    # ▼ 設定エリア（適用したい処理を True にする）
    # ==========================================
    
    # 1. トリミング（時間の切り出し）
    ENABLE_TRIM = False      # 実行する場合は True に変更
    start_time = 0.0        # 開始時間（秒）
    end_time = 10.0         # 終了時間（秒）

    # 2. クロップ（画面の切り抜き）
    ENABLE_CROP = False     # 実行する場合は True に変更
    crop_x1 = 0
    crop_y1 = 50
    crop_y2_margin = 150    # 下から削るピクセル数

    # 3. リサイズ（縮小）
    resize_scale = 0.6      # 縦横サイズの倍率指定
    fps = 10                # GIFのフレームレート

    # ==========================================
    # ▼ 処理エリア
    # ==========================================
    
    clip = VideoFileClip(input_path) # 動画ファイルを読み込む
    
    # トリミングを実行
    if ENABLE_TRIM:
        clip = clip.subclipped(start_time, end_time)
        
    # クロップを実行
    if ENABLE_CROP:
        clip = clip.cropped(x1=crop_x1, y1=crop_y1, x2=clip.w, y2=clip.h - crop_y2_margin)
        
    # リサイズを実行
    if resize_scale:
        clip = clip.resized(resize_scale)
        
    # GIF書き出し
    clip.write_gif(output_path, fps=fps)
    
    # メモリ解放
    clip.close()

# 実行
convert_and_compress_to_gif("input_video.mp4", "output.gif")