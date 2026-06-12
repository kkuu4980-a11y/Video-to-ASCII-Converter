import os
import time
import cv2

ASCII_CHARS = [" ", ".", "'", "`", "^", '"', ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "*", "q", "h", "a", "o", "b", "d", "k", "$", "M", "W", "#"]

def frame_to_ascii(frame, new_width=60):
    height, width, _ = frame.shape
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55) 
    resized_frame = cv2.resize(frame, (new_width, new_height))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    ascii_str = ""
    for row in gray_frame:
        for pixel in row:
            index = int((pixel / 255) * (len(ASCII_CHARS) - 1))
            ascii_str += ASCII_CHARS[index]
        ascii_str += "\n"
    return ascii_str

print("[0] 繁體中文 (Traditional Chinese)")
print("[1] English")
try:
    lang_choice = int(input("Select Language / 選擇語言: "))
except ValueError:
    lang_choice = 1

is_zh = (lang_choice == 0)

files = [f for f in os.listdir('.') if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]

if not files:
    if is_zh:
        print("錯誤：當前資料夾內找不到任何影片檔案。")
    else:
        print("Error: No video files found in the current directory.")
    exit()

if is_zh:
    print("可用的影片列表：")
else:
    print("Available videos:")

for i, file_name in enumerate(files):
    print(f"[{i}] {file_name}")

try:
    if is_zh:
        choice = int(input("請選擇影片編號: "))
    else:
        choice = int(input("Select video index: "))
    selected_video = files[choice]
except (ValueError, IndexError):
    if is_zh:
        print("無效的選擇。")
    else:
        print("Invalid selection.")
    exit()

if is_zh:
    print("\n請選擇輸出格式：")
    print("[0] .lua (Roblox ModuleScript 專用)")
    print("[1] .txt (通用文字檔，使用 |SPLIT| 分隔影格)")
    try:
        fmt_choice = int(input("請輸入格式編號: "))
    except ValueError:
        fmt_choice = 0
else:
    print("\nSelect Output Format:")
    print("[0] .lua (For Roblox ModuleScript)")
    print("[1] .txt (Plain text with |SPLIT| separator)")
    try:
        fmt_choice = int(input("Select format index: "))
    except ValueError:
        fmt_choice = 0

is_txt = (fmt_choice == 1)

cap = cv2.VideoCapture(selected_video)

if is_txt:
    output_text = ""
else:
    output_text = "local videoFrames = {\n"

if is_zh:
    print("影片處理中...")
else:
    print("Processing...")

frame_list = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    ascii_frame = frame_to_ascii(frame)
    frame_list.append(ascii_frame)

cap.release()

if is_txt:
    output_text = "|SPLIT|".join(frame_list)
    out_filename = "video_frames.txt"
else:
    for frame_data in frame_list:
        output_text += f'    [==[{frame_data}]==],\n'
    output_text += "}\nreturn videoFrames"
    out_filename = "video_frames.lua"

with open(out_filename, "w", encoding="utf-8") as f:
    f.write(output_text)

if is_zh:
    print(f"完成！已成功生成 {out_filename} 檔案。")
    print("\n是否要在終端機中直接預覽播放？")
    print("[0] 是 (Yes)")
    print("[1] 否 (No)")
    try:
        preview_choice = int(input("請輸入選擇編號: "))
    except ValueError:
        preview_choice = 1
else:
    print(f"Done! Successfully generated {out_filename}.")
    print("\nDo you want to preview the playback in the terminal?")
    print("[0] Yes")
    print("[1] No")
    try:
        preview_choice = int(input("Select choice index: "))
    except ValueError:
        preview_choice = 1

if preview_choice == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    for frame_data in frame_list:
        print("\033[H" + frame_data, end="")
        time.sleep(0.033)
    
    if is_zh:
        print("\n預覽結束！")
    else:
        print("\nPreview Finished!")