# Recovery index shards

Các file trong thư mục này lưu bản dịch theo **chỉ số 1-based trong thứ tự key của `[CP] Seven Deadly Sins/i18n/default.json` phiên bản 3.13.4**.

Cách phục hồi:
1. Đọc `default.json` 3.13.4 và giữ nguyên thứ tự key.
2. Với mỗi cặp `index -> translation`, lấy key ở vị trí `index - 1`.
3. Gán bản dịch vào key đó trong `vi.json`.
4. Sau khi ghép phải chạy QA token/Hán tự như `HANDOFF.md` quy định.

Các file recovery là dữ liệu cứu hộ từ phiên ChatGPT đã QA trước đó. Sau khi materialize thành shard key-based trong `translations/cp`, cập nhật `CHECKPOINT.json`.
