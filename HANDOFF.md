# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên làm việc sau. Đọc file này trước khi tiếp tục.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Mod nguồn

- Mod: Seven Deadly Sins 1.6
- Version đang Việt hóa: **3.13.4**
- File nguồn người dùng đã cung cấp trong phiên gốc: `Seven Deadly Sins 1.6-3.13.4 15100 3.13.4 2026-08-14T08-26Z oD4nNsEqK.zip`
- CP default có **24,827 key**.
- DLL default có **2,419 key**.

## Quy tắc dịch đã chốt

1. Văn phong tiếng Việt tự nhiên, giống hội thoại game, không dịch máy cứng.
2. Giữ cá tính riêng từng NPC. Không dùng một bộ xưng hô chung cho tất cả.
3. Chuẩn hóa tên nhân vật sang tên Latin mà mod dùng, tránh lẫn chữ Hán trong câu tiếng Việt.
4. Không tự thêm/bớt token kỹ thuật. Phải giữ nguyên các dạng như:
   - `@`
   - `$h`, `$l`, `$1`, `$2`, ...
   - `#$b#`
   - `$q ...`, `$r ...`
   - `{{...}}`
   - `[SDS_...]`
   - `%item`, `%spouse`, `[letterbg ...]`, `[textcolor ...]`
   - nhánh giới tính và các token Content Patcher khác.
5. Sau mỗi cụm phải QA token + kiểm tra Hán tự còn sót.
6. Với nội dung mới 3.13.4 (ví dụ Cupid), lấy 3.13.4 làm chuẩn. Không đè bản Anh cũ 3.12.2 lên nội dung mới.
7. Bản dịch Anh từ repo `RedRevenant/SDSi18nConversion` có thể dùng làm cầu nối/ngữ cảnh, nhưng key/version 3.13.4 của mod người dùng mới là nguồn cấu trúc cuối cùng.

## Giọng nhân vật đã dùng

- **Lane**: ngọt, láu cá, bán hàng, ve vãn; thân mật tăng theo tim.
- **Rane**: sắc hơn Lane, trêu chọc, thao túng nhẹ, hơi chiếm hữu.
- **Sariel**: lịch sự/kiêu, ngọt nhưng có gai.
- **Uriel**: nghiêm, kiêu, trang trọng, đôi khi độc miệng.
- **Moore**: lạnh, độc, hoa mỹ; không bình dân hóa quá mức.
- **Hovsep**: rụt rè, mềm, đáng yêu, dễ hoảng.
- **Lucas**: ngọt nhưng nguy hiểm, thông minh, có lúc rất trêu.
- **Teresa**: giữ tự xưng `Nunu` khi nguồn dùng đặc điểm này.
- **Shirai**: dị thường, rùng rợn, thân mật theo kiểu bất an; không làm mềm lore quá mức.
- **Cupid**: lắm lời, dễ thương, tự tin, mê trà/hóng chuyện tình cảm, đôi khi dọa dùng mũi tên chì.

## CẢNH BÁO QUAN TRỌNG VỀ CHECKPOINT

Trong cuộc trò chuyện trước từng có các báo cáo tiến độ lên đến CP `#8,400` và DLL `2,419/2,419`. Tuy nhiên khi kiểm tra **file thật trên ổ đĩa** trước khi nối GitHub, phát hiện:

- File `[CP] Seven Deadly Sins/i18n/vi.json` hiện có **2,700 key**.
- 2,700 key này khớp chính xác một dải liên tục theo thứ tự key của `default.json`: **#5,701 → #8,400**.
- Các key **#1 → #5,700 không còn tồn tại trong file checkpoint hiện tại** dù trước đó đã từng được báo hoàn thành trong chat.
- File `SevenDeadlySins/i18n/vi.json` của DLL **không còn trên ổ đĩa** khi kiểm tra repo handoff, dù chat trước đã báo DLL hoàn thành.

Vì vậy, **KHÔNG được coi #1→#5,700 hoặc DLL 2,419 là dữ liệu đã được bảo toàn**, cho tới khi chúng được phục hồi hoặc dịch lại và commit vào repo.

## Nguồn sự thật hiện tại

Nguồn sự thật đáng tin cậy nhất hiện tại là:

- CP translated keys: **#5,701 → #8,400** (2,700 key), đã tồn tại trong file `vi.json` tại thời điểm tạo handoff.
- Mốc tiếp theo nếu tiếp tục tuyến đang dịch: **#8,401**.
- Nhưng trước khi phát hành bản hoàn chỉnh, bắt buộc phải phục hồi/dịch lại **#1 → #5,700** và DLL nếu repo chưa có các phần đó.

## QA đã dùng

Mỗi mẻ cần đối chiếu token từ source và target; đặc biệt kiểm tra:

- số lượng và thứ tự `@`
- `#$b#`
- emotion `$N`
- `$q/$r`
- `{{...}}`
- `[SDS_...]`
- `%...`
- `^`
- Hán tự còn sót trong text hiển thị

Không coi dấu `%` trong câu văn như `20%` là vô hại nếu bộ QA/token parser của mod có thể hiểu nhầm; ưu tiên viết `hai mươi phần trăm` nếu cần.

## Cách tiếp tục ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF trong repo ronvotri/Seven-Deadly-Sins-votrivalley.`

Assistant cần:

1. Đọc `HANDOFF.md` và `CHECKPOINT.json` trước.
2. Kiểm tra các translation shard/file đã commit trong repo.
3. Không tin mốc tiến độ cũ chỉ từ hội thoại nếu không có file tương ứng trong repo.
4. Tiếp tục từ checkpoint thực tế và commit sau mỗi mẻ lớn.

## Mục tiêu phát hành

Bản cuối nên chỉ chứa file Việt hóa, cấu trúc thuận tiện để chép vào mod gốc, không kèm file game/mod gốc nếu không cần thiết.
