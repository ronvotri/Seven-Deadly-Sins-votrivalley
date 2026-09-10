# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên sau. Mục tiêu hiện tại là HOÀN THIỆN REPO, không dịch lại nội dung đã làm.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Source đã chốt

- Mod: Seven Deadly Sins 1.6
- Version: **3.13.4**
- Nexus file ID: **178657**
- CP default: **24,827 key**
- DLL default: **2,419 key**
- Exact CP source đã xác minh từ SMAPI dump:
  `downloads/Nexus/15/15100/178657/Seven Deadly Sins 1.6/[CP] Seven Deadly Sins/i18n/default.json`
- Cấu trúc/key/order cuối cùng luôn theo source 3.13.4.

## TRẠNG THÁI DỊCH THỰC TẾ

### CP ĐÃ DỊCH TUẦN TỰ TỚI CUỐI

- Đã đi tới **#24,827 / 24,827**.
- Batch cuối: `#24,797 → #24,827`.
- Batch cuối QA: **0 lỗi token / 0 Hán tự**.
- Đây là mốc hoàn thành nội dung dịch CP, không được hiểu thành yêu cầu dịch tiếp từ #24,828.

### Vấn đề còn lại là PERSISTENCE / RECONSTRUCTION

Một số phiên cũ đã dịch nhưng dữ liệu không được commit đầy đủ vào repo, hoặc tồn tại ở recovery shard / lịch sử / artifact thay vì `translations/cp`.

**Từ thời điểm này, tuyệt đối phân biệt:**

- `translation complete` = nội dung đã từng được dịch tới cuối source.
- `repo complete` = toàn bộ dữ liệu đã được khôi phục, materialize, QA và ghép vào repo.

Hiện mục tiêu duy nhất là đưa repo từ trạng thái thứ nhất sang trạng thái thứ hai.

## CHÍNH SÁCH CHỐNG VÒNG LẶP

1. **KHÔNG dịch lại một key chỉ vì `translations/cp` đang thiếu file.**
2. Với mọi dải thiếu, phải vét theo thứ tự:
   - `recovery/index/`
   - `translations/cp/`
   - git commit history
   - GitHub Actions artifacts / workflow outputs
   - file/handoff đã persisted từ các phiên trước
3. Nếu recovery shard đã có tiếng Việt, chỉ materialize sang exact key 3.13.4. **Không dịch lại câu chữ.**
4. Nếu key-based và recovery khác nhau, ưu tiên bản QA-preserved đáng tin cậy hơn rồi chạy token audit.
5. **Chỉ được dịch lại sau khi chứng minh không còn bất kỳ persisted copy nào và phải có sự đồng ý rõ ràng của người dùng.** Không tự động fallback sang retranslation.
6. Không dùng số liệu audit cũ để kết luận “chưa dịch”. Audit chỉ phản ánh mức độ dữ liệu đang nằm trong repo tại thời điểm chạy.

## Tình trạng recovery gần nhất

- Chuỗi restore gần nhất trên `main` đã đưa `recovery/index` liên tục tới ít nhất **CP #8500**.
- Các commit mới nhất gồm các shard restore `7901-8000` → `8401-8500`.
- Workflow materialization đã được kích hoạt lại để chuyển **mọi recovery shard hiện có** sang `translations/cp` và refresh audit.
- Các dải phía sau vẫn có nhiều key-based/recovery shard đã persisted ở repo, bao gồm tail tới `24797-24827`.

## Quy tắc dịch/QA giữ nguyên

1. Tiếng Việt tự nhiên như hội thoại game, không dịch máy cứng.
2. Giữ cá tính NPC.
3. Chuẩn hóa tên nhân vật Latin, không để Hán tự trong target.
4. Không tự thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^`, route ID/key, item ID và Content Patcher token khác.
5. QA bằng token skeleton đúng thứ tự + quét Hán tự.
6. Không tự gán giới tính cho `%kid1`, `%kid2`, `%pet` nếu source/game không bắt buộc.

## DLL

- Expected: **2,419 key**.
- Lịch sử trước đây đã báo DLL từng hoàn thành, nhưng repo hiện chưa xác minh được persisted DLL translation.
- **Áp dụng cùng chính sách recovery-first. Không tự dịch lại DLL chỉ vì repo hiện chưa thấy file.**

## Việc cần làm từ đây

1. Materialize toàn bộ `recovery/index` hiện có sang exact key-based `translations/cp`.
2. Refresh audit để xác định **repo holes**, không gọi chúng là “chưa dịch”.
3. Với từng repo hole, tìm bản đã dịch trong history/artifact/persisted source trước.
4. Reconcile duplicate/overlap và sửa lỗi cấu trúc token nếu có.
5. Khôi phục DLL theo cùng nguyên tắc recovery-first.
6. Khi coverage repo đạt đủ, chạy final QA và đóng gói bản Việt hóa phát hành.

## Cách bắt đầu ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF mới nhất trên GitHub.`

Assistant phải đọc `HANDOFF.md`, `CHECKPOINT.json`, audit mới nhất và **không được tự quay lại dịch các range đã từng hoàn thành**.

## Mục tiêu phát hành

Bản cuối chỉ chứa file Việt hóa/cấu trúc cần thiết để chép vào mod gốc, không kèm asset game/mod gốc không cần thiết.
