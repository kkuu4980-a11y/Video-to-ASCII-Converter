# Video to ASCII Converter



一個使用 Python 編寫的工具，能將任何影片檔案轉換為 ASCII 字元畫字串模組。高流暢度、並針對黑底白字進行了視覺優化，轉換完成後可透過選單選擇是否直接在終端機中進行即時預覽。
請在 https://github.com/kkuu4980-a11y/Video-to-ASCII-Converter/releases 下載.exe版。

---

## 專案特點

* **雙語互動介面**: 支援繁體中文與英文互動式命令列選單。
* **智慧影片偵測**: 自動掃描當前資料夾下的影片檔案（`.mp4`、`.mkv`、`.avi`、`.mov`）並提供編號供用戶選擇。
* **終端機即時預覽**: 轉換完成後可透過選單選擇是否直接在終端機以 30 FPS 高流暢度預覽播放，無需載入遊戲即可確認效果。
* **多功能輸出格式**: 自由選擇匯出 `.lua`（Roblox 陣列格式）或 `.txt`（帶有 `|SPLIT|` 分隔符號的通用文字檔）。
* **黑底優化渲染**: 採用專為「黑底白字」優化的反轉字元密度表，完美還原剪影細節。

---

## Prerequisites / 系統需求

* Python 3.x
* OpenCV Python (`opencv-python`)

### Installation / 安裝依賴

```bash
pip install opencv-python
```
