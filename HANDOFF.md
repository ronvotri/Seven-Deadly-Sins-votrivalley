# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên làm việc sau. Đọc file này trước khi tiếp tục.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Mod nguồn

- Mod: Seven Deadly Sins 1.6
- Version đang Việt hóa: **3.13.4**
- File nguồn: `Seven Deadly Sins 1.6-3.13.4 15100 3.13.4 2026-08-14T08-26Z oD4nNsEqK.zip`
- CP default: **24,827 key**
- DLL default: **2,419 key**

## Quy tắc dịch đã chốt

1. Văn phong tiếng Việt tự nhiên, giống hội thoại game, không dịch máy cứng.
2. Giữ cá tính riêng từng NPC, không dùng một bộ xưng hô chung.
3. Chuẩn hóa tên nhân vật sang tên Latin mà mod dùng, tránh lẫn chữ Hán trong câu Việt.
4. Không tự thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^` và các Content Patcher token khác.
5. Sau mỗi cụm phải QA token + kiểm Hán tự.
6. Nội dung 3.13.4 là nguồn cấu trúc cuối cùng. Bản Anh 3.12.2 chỉ dùng đối chiếu/ngữ cảnh.

## Giọng nhân vật

- Lane: ngọt, láu cá, bán hàng, ve vãn.
- Rane: sắc hơn Lane, trêu chọc, thao túng nhẹ, hơi chiếm hữu.
- Sariel: lịch sự/kiêu, ngọt nhưng có gai.
- Uriel: nghiêm, kiêu, trang trọng, đôi khi độc miệng.
- Moore: lạnh, độc, hoa mỹ, không bình dân hóa quá mức.
- Hovsep: rụt rè, mềm, đáng yêu, dễ hoảng.
- Lucas: ngọt nhưng nguy hiểm, thông minh, hay trêu.
- Teresa: giữ tự xưng `Nunu` khi nguồn dùng đặc điểm này.
- Shirai: dị thường, rùng rợn, thân mật theo kiểu bất an.
- Cupid: lắm lời, dễ thương, tự tin, mê trà/hóng chuyện tình cảm.
- Pelette: cộc, nóng, mang nhiều vết thương cũ; mềm dần theo tim và đặc biệt ấm hơn rõ rệt trong marriage dialogue.

## CHECKPOINT THỰC TẾ CỦA PHIÊN 2026-09-09

### Đã dịch và QA trong phiên

- CP đã đi liên tục trong file làm việc từ **#5,701 → #12,700**.
- Mốc dịch tiếp theo: **#12,701**.
- Các mẻ gần cuối #11,601→#12,700 đã được QA token/Hán tự theo batch.

### Đã materialize thành file trên GitHub

- Tại lần kiểm tra repo ngày 2026-09-09, các shard thật hiện có liên tục **#5,701 → #6,900**.
- Dải **#6,901 → #12,700** đã được dịch trong phiên nhưng cần khôi phục/upload từ lịch sử phiên. Việc recovery đang được thực hiện; xem `CHECKPOINT.json` để biết mốc materialized mới nhất.

### Phần chưa được bảo toàn/kiểm chứng

- CP **#1 → #5,700**: từng được báo đã dịch trong hội thoại cũ, nhưng chưa tìm thấy bản persisted đáng tin cậy trong repo.
- DLL **#1 → #2,419**: từng được báo hoàn tất, nhưng chưa có file persisted được xác minh trong repo.
- Vì vậy hai phần trên vẫn là release blocker nếu không tìm lại được bản cũ.

## QA bắt buộc

So source/target cho:
- số lượng `$`, `#`, `@`, `^`
- `#$b#`
- emotion `$N`
- `$q/$r`
- `{{...}}`
- bracket token `[SDS_...]`, item IDs
- `%...`
- Hán tự còn sót trong text hiển thị

Không chỉ kiểm token tổng. Với những đoạn preview bị cắt/trượt key, phải đối chiếu **key gốc thật theo thứ tự `default.json`**.

## Cách tiếp tục ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF trong repo ronvotri/Seven-Deadly-Sins-votrivalley.`

Assistant phải:
1. Đọc `HANDOFF.md` + `CHECKPOINT.json`.
2. Liệt kê shard thật trong `translations/cp` trước khi tin checkpoint materialized.
3. Nếu recovery #6,901→#12,700 chưa hoàn tất, ưu tiên phục hồi/upload các batch đó trước.
4. Khi dữ liệu đã an toàn, tiếp tục dịch từ **#12,701**.
5. Không tính tiến độ chỉ vì chat từng báo. Chỉ phân biệt rõ `session_verified` và `github_materialized`.

## Mục tiêu phát hành

Bản cuối chỉ chứa file Việt hóa/cấu trúc cần thiết để chép vào mod gốc, không kèm tài sản game/mod gốc không cần thiết.
