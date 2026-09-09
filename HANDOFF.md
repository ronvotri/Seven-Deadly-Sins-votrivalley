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
- Nguồn CP 3.13.4 đã được xác minh trực tiếp từ mod dump SMAPI, đúng file Nexus **178657** và đúng **24,827 key**.

## Quy tắc dịch đã chốt

1. Văn phong tiếng Việt tự nhiên, giống hội thoại game, không dịch máy cứng.
2. Giữ cá tính riêng từng NPC, không dùng một bộ xưng hô chung.
3. Chuẩn hóa tên nhân vật sang tên Latin mà mod dùng, tránh lẫn chữ Hán trong câu Việt.
4. Không tự thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^` và các Content Patcher token khác.
5. Sau mỗi cụm phải QA token + kiểm Hán tự.
6. Nội dung 3.13.4 là nguồn cấu trúc cuối cùng. Bản Anh 3.12.2 chỉ dùng đối chiếu/ngữ cảnh.
7. Với `%kid1`, `%kid2`, `%pet`, tránh tự gán giới tính nếu nguồn/game không bắt buộc.

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

## CHECKPOINT THỰC TẾ - cập nhật 2026-09-09

### Mốc dịch hiện tại

- **CP đã được dịch/QA tới #14,996.**
- **Mốc dịch tiếp theo: #14,997.**
- Hai batch mới nhất của phiên hiện tại:
  - `#14,797 → #14,896`
  - `#14,897 → #14,996`
- Cả hai batch mới đều QA sạch token kỹ thuật và **0 Hán tự** còn sót trong text hiển thị.

### Dữ liệu đã materialize trên GitHub

- Key-based shards trong `translations/cp` đã được xác minh tới **#14,500**, và có thêm hai shard mới:
  - `translations/cp/CP_14797_14896.json`
  - `translations/cp/CP_14897_14996.json`
- Phần **#14,501 → #14,796** đã được bảo toàn bằng recovery index:
  - `recovery/index/CP_14501_14600.json`
  - `recovery/index/CP_14601_14700.json`
  - `recovery/index/CP_14701_14796.json`
- Hai batch mới cũng có recovery index song song:
  - `recovery/index/CP_14797_14896.json`
  - `recovery/index/CP_14897_14996.json`
- Vì vậy nội dung dịch đã được bảo toàn liên tục qua **#14,996** dù dải #14,501→#14,796 chưa được tái dựng thành key-based shard.

### Phần cần xử lý về sau

- Tái dựng key-based shard cho **#14,501 → #14,796** từ source 3.13.4 + recovery index trước bản release cuối.
- CP **#1 → #5,700**: từng được báo đã dịch trong hội thoại cũ, nhưng vẫn chưa có bản persisted đáng tin cậy được xác minh.
- DLL **#1 → #2,419**: từng được báo hoàn tất, nhưng chưa có file persisted được xác minh.
- Hai phần trên vẫn là release blocker nếu không tìm lại được bản cũ.

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

Không chỉ kiểm token tổng. Với những đoạn preview bị cắt/trượt key, phải đối chiếu **key gốc thật theo thứ tự `default.json` 3.13.4**.

## Cách tiếp tục ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF trong repo ronvotri/Seven-Deadly-Sins-votrivalley.`

Assistant phải:
1. Đọc `HANDOFF.md` + `CHECKPOINT.json`.
2. Kiểm tra shard thật trong `translations/cp` và `recovery/index` trước khi tin mốc.
3. Xem **#14,996** là endpoint đã được bảo toàn hiện tại.
4. Tiếp tục dịch từ **CP #14,997** theo đúng source 3.13.4.
5. Mỗi batch phải tạo cả key-based shard và recovery index, rồi QA token/Hán tự.
6. Không tính tiến độ chỉ vì chat từng báo. Chỉ tính phần đã QA và đã được materialize/preserve rõ ràng.

## Mục tiêu phát hành

Bản cuối chỉ chứa file Việt hóa/cấu trúc cần thiết để chép vào mod gốc, không kèm tài sản game/mod gốc không cần thiết.
