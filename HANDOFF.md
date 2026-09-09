# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên làm việc sau. Đọc file này cùng `CHECKPOINT.json` và `audit/CP_AUDIT.json` trước khi tiếp tục.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Mod nguồn

- Mod: Seven Deadly Sins 1.6
- Version đang Việt hóa: **3.13.4**
- Nexus file ID chính xác: **178657**
- CP default: **24,827 key**
- DLL default: **2,419 key**
- Source CP chính xác đã xác minh từ SMAPI dump:
  `downloads/Nexus/15/15100/178657/Seven Deadly Sins 1.6/[CP] Seven Deadly Sins/i18n/default.json`
- Bản Anh 3.12.2 chỉ được dùng làm tham khảo ngữ cảnh. **Cấu trúc/key/order cuối cùng luôn theo Chinese source 3.13.4.**

## Quy tắc dịch đã chốt

1. Tiếng Việt tự nhiên như hội thoại game, không dịch máy cứng.
2. Giữ cá tính riêng từng NPC.
3. Chuẩn hóa tên nhân vật sang tên Latin của mod, không để chữ Hán trong target.
4. Không tự thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^`, route ID/key, item ID và Content Patcher token khác.
5. QA mỗi batch bằng **token skeleton theo đúng thứ tự** + quét Hán tự.
6. Với `%kid1`, `%kid2`, `%pet` và biến tương tự, không tự gán giới tính nếu source/game không bắt buộc.
7. Những lỗi/chuỗi kỳ lạ vốn có trong source phải được giữ nguyên nếu chúng là cấu trúc kỹ thuật; không tự “sửa hộ” source.

## Giọng nhân vật quan trọng

- Lane: ngọt, láu cá, bán hàng, ve vãn.
- Rane: sắc hơn Lane, trêu chọc, thao túng nhẹ, hơi chiếm hữu.
- Sariel: lịch sự/kiêu, ngọt nhưng có gai.
- Uriel: nghiêm, kiêu, trang trọng, đôi khi độc miệng.
- Moore: lạnh, độc, hoa mỹ.
- Hovsep: rụt rè, mềm, đáng yêu, dễ hoảng, hay buồn ngủ.
- Lucas: ngọt nhưng nguy hiểm, thông minh, hay trêu.
- Teresa: giữ tự xưng **`Nunu`** khi source dùng đặc điểm này.
- Shirai: dị thường, rùng rợn, thân mật theo kiểu bất an.
- Cupid: lắm lời, dễ thương, tự tin, mê trà/hóng chuyện tình cảm.
- Pelette: cộc, nóng, mang nhiều vết thương cũ; mềm dần theo tim và marriage dialogue.
- Siren: hoạt bát, tò mò văn hóa loài người, thường tự xưng **“chị đây”**.
- Wim: bartender thân thiện, hơi kịch tính, thích Xenia và muốn trở thành một quý ông đáng tin.

## Mốc dịch tuần tự

### CP đã đi tới cuối source

- Chuỗi dịch tuần tự đã đi tới **CP #24,827 / 24,827**.
- Batch cuối: `#24,797 → #24,827` (31 key).
- Batch cuối QA: **0 lỗi token / 0 Hán tự**.
- Recovery cuối: `recovery/index/CP_24797_24827.json`.
- Key-based cuối đã được materialize: `translations/cp/CP_24797_24827.json`.

**Quan trọng:** “đã đi tới cuối source” không đồng nghĩa repo đã đủ 24,827 key. Audit toàn repo phát hiện nhiều dải lịch sử từ các phiên cũ không được persisted.

## Audit repo thực tế

Nguồn báo cáo:
- `audit/CP_AUDIT.json`
- `audit/CP_MISMATCH_SUMMARY.json`
- `audit/mismatches/*.json`

Audit v2 sau khi reconcile recovery → key-based cho kết quả:

- Exact CP source: **24,827 key**
- Key-based hiện có: **13,527 key**
- Key-based còn thiếu: **11,300 key**
- Dải thiếu chính xác:
  - **#1 → #5,700**
  - **#6,901 → #11,200**
  - **#11,301 → #11,600**
  - **#12,701 → #13,700**
- Recovery hiện có: **12,227 index**
- Recovery còn thiếu: **12,600 index**
- Hán tự trong key-based hiện có: **0**
- Key lạ: **0**
- Index trùng: **0**
- Recovery ↔ key-based mismatch sau reconcile: **0**
- Technical token mismatch còn lại: **189 key**, nằm trong **22 block** và đã có exact source + current target ở `audit/mismatches/*.json`.

### Ý nghĩa

Các bản dịch mới/tail đã được bảo toàn tới #24,827. Tuy nhiên repo **chưa release-ready** vì dữ liệu của một số phiên cũ bị thất lạc/không từng được commit, và một số shard cũ có lỗi token hoặc từng lệch key.

## Chính sách reconciliation

Khi một dải có **complete recovery shard**, recovery index được coi là bản QA-preserved mới hơn và là nguồn ưu tiên. Key-based tương ứng phải được dựng lại bằng:

`exact source 3.13.4 index → exact key + recovery Vietnamese value`

Audit v2 đã reconcile các recovery shard hiện có vào key-based. Sau reconcile, mismatch recovery ↔ key-based = **0**.

## Các lỗi token cần sửa

- Tổng: **189**
- Không sửa bằng cách chỉ đếm `$`/`#`.
- Dùng `audit/CP_MISMATCH_SUMMARY.json` để xem block.
- Mỗi file trong `audit/mismatches/` chứa:
  - source index
  - exact source key
  - exact Chinese source value
  - current Vietnamese target
  - source token skeleton
  - target token skeleton
- Một cụm Pelette quanh #11,686→#11,718 cho thấy bản cũ bị lệch nội dung/key, vì vậy phải **dịch lại exact source cho các key lỗi**, không chỉ chèn token cơ học.

## DLL

- Expected: **2,419 key**.
- Hội thoại cũ từng báo DLL hoàn tất, nhưng repo hiện **không có persisted DLL translation**; thư mục `translations` hiện chỉ xác minh có `translations/cp`.
- Không được ghi DLL hoàn tất trong bản phát hành cho tới khi tìm lại hoặc dịch lại và commit đủ 2,419 key.

## Thứ tự việc cần làm khi quay lại SDS

1. **Sửa 189 token mismatch** dựa trên `audit/mismatches/*.json`, cập nhật đồng thời recovery + key-based.
2. Tìm bản persisted đáng tin cậy của các dải CP thiếu; nếu không có thì dịch lại exact source 3.13.4 cho:
   - 1-5700
   - 6901-11200
   - 11301-11600
   - 12701-13700
3. Khôi phục hoặc dịch lại **DLL 1-2419** và commit vào repo.
4. Chạy audit cuối:
   - coverage CP = 24,827/24,827
   - missing = 0
   - token mismatch = 0
   - Han = 0
   - duplicate/unknown key = 0
5. Sau đó mới ráp file Việt hóa phát hành/Nexus package.

## Cách bắt đầu ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF mới nhất trên GitHub.`

Assistant phải đọc:
1. `HANDOFF.md`
2. `CHECKPOINT.json`
3. `audit/CP_AUDIT.json`
4. `audit/CP_MISMATCH_SUMMARY.json`

Không được tiếp tục từ #24,828. **Tail translation đã kết thúc. Việc tiếp theo là repair/recovery.**

## Mục tiêu phát hành

Bản cuối chỉ chứa file Việt hóa/cấu trúc cần thiết để chép vào mod gốc, không kèm asset game/mod gốc không cần thiết.
