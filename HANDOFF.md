# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên sau. CP đã hoàn tất sạch. Mục tiêu hiện tại là DLL và đóng gói release.**

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

## CP - ĐÃ HOÀN TẤT

CP đã được reconstruction, materialize và full audit thành công.

Final canonical commit:

`2ca310f` - `Finalize canonical CP translation and clean audit`

Kết quả `audit/CP_AUDIT.json`:

- **24,827 / 24,827 key covered**
- missing: **0**
- duplicate: **0**
- unknown: **0**
- technical token mismatch: **0**
- Hán tự: **0**

Các lỗi persistence/misalignment quan trọng đã xử lý:

- khôi phục batch thất lạc `9301-9400`;
- realign `10101-10200` theo exact source 3.13.4;
- realign `10601-10700` theo exact source 3.13.4;
- sửa token cuối ở `10608`;
- canonical hóa `translations/cp` thành shard không chồng lấn.

**Không quay lại dịch CP nữa**, trừ khi source mod có version mới.

## DLL - PHASE HIỆN TẠI

- Expected: **2,419 key**.
- Exact DLL source 2,419 key đã từng được workflow xác định và đưa vào artifact `sds-exact-missing-cp-dll-source`.
- Exact source file trong artifact: `DLL_1_2419_SOURCE.json`.
- **Điểm bắt đầu hiện tại: DLL #1.**
- Chưa được phép gọi release-ready cho tới khi DLL 1-2419 được persist + QA sạch.

### Quy trình DLL bắt buộc

1. Dùng exact DLL source đã extract, không đoán key/order.
2. Dịch/recover theo batch khoảng 100 key.
3. QA từng batch:
   - token skeleton đúng thứ tự;
   - 0 Hán tự;
   - không tự sửa ID/token kỹ thuật.
4. **Commit GitHub ngay sau mỗi batch.**
5. Một batch chỉ được tính hoàn thành khi đã có commit SHA.
6. Sau DLL #2419, chạy full DLL audit rồi mới ghép package.

## QUY TẮC BẮT BUỘC: PERSIST GITHUB

1. **Một batch chỉ được tính là hoàn thành khi đã có commit SHA trên GitHub.**
2. Trước khi kết thúc mỗi phiên SDS:
   - commit mọi batch đã hoàn thành;
   - cập nhật `CHECKPOINT.json` khi trạng thái/điểm nối thay đổi;
   - cập nhật `HANDOFF.md` khi cần;
   - ghi rõ exact next index/range.
3. **Không để bản dịch hoàn chỉnh chỉ nằm trong chat.**
4. Ưu tiên batch 100 key để giảm rủi ro mất dữ liệu.

## Quy tắc dịch/QA

1. Tiếng Việt tự nhiên như hội thoại game, không dịch máy cứng.
2. Giữ cá tính NPC.
3. Chuẩn hóa tên nhân vật Latin, không để Hán tự trong target.
4. Không tự thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^`, route ID/key, item ID và Content Patcher token khác.
5. QA bằng token skeleton đúng thứ tự + quét Hán tự.
6. Không tự gán giới tính cho `%kid1`, `%kid2`, `%pet` nếu source/game không bắt buộc.

## Giọng nhân vật quan trọng

- Lane: ngọt, láu lỉnh, thương nhân, hơi flirt.
- Rane: sắc hơn Lane, trêu/chọc, hơi chiếm hữu.
- Sariel: lịch sự, kiêu hãnh, ngọt có gai.
- Uriel: nghiêm, kiêu, trang trọng, đôi lúc cay độc; dùng tiếng Việt tự nhiên, không máy móc.
- Moore: lạnh, tàn nhẫn, hoa mỹ.
- Hovsep: nhút nhát, mềm, đáng yêu, dễ giật mình, buồn ngủ.
- Lucas: ngọt nhưng nguy hiểm, thông minh, thích trêu.
- Teresa: giữ self-reference `Nunu` khi source dùng đặc điểm đó.
- Shirai: kỳ dị, rờn rợn, thân mật bất an.
- Cupid: hoạt ngôn, đáng yêu, tự tin, mê trà/chuyện phiếm/tình yêu.
- Pelette: cộc, nóng tính, có vết thương quá khứ; mềm hơn ở heart/marriage cao.
- Siren: sôi nổi, tò mò văn hóa loài người, thường tự xưng `chị đây`.
- Wim: bartender thân thiện, hơi sân khấu, thích Xenia, muốn là quý ông đáng tin.

## Việc cần làm từ đây

1. **DLL #1 → #2419**.
2. Persist + QA từng batch lên GitHub.
3. Full DLL audit: coverage đầy đủ, 0 token mismatch, 0 Hán tự, 0 unknown/duplicate.
4. Ghép CP + DLL thành cấu trúc Việt hóa cài được.
5. Build gói release chỉ chứa file Việt hóa cần thiết, không kèm asset gốc.

## Cách bắt đầu ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF mới nhất trên GitHub.`

Assistant phải đọc `HANDOFF.md`, `CHECKPOINT.json`, audit mới nhất và nối từ exact persisted checkpoint.

## Điểm nối chính xác

**DLL #1. CP đã DONE.**
