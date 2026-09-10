# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên sau. Mục tiêu hiện tại là hoàn thiện repo và bản Việt hóa phát hành.**

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

### CP từng được dịch tuần tự tới cuối

- Đã đi tới **#24,827 / 24,827** trong lịch sử làm việc.
- Batch cuối lịch sử: `#24,797 → #24,827`.
- Một số đoạn từng dịch nhưng không được persist, nên hiện đang khôi phục/làm lại đúng các khoảng dữ liệu thất lạc để tạo file phát hành thật.

### Repo reconstruction hiện tại

- Recovery đã được khôi phục liên tục tới **#8900**.
- Các shard mới đã commit trong phiên này:
  - `recovery/index/CP_8501_8600.json`
  - `recovery/index/CP_8601_8700.json`
  - `recovery/index/CP_8701_8800.json`
  - `recovery/index/CP_8801_8850.json`
  - `recovery/index/CP_8851_8900.json`
- QA cho các batch mới: **0 technical token mismatch / 0 Hán tự**.
- **Điểm tiếp tục chính xác hiện tại: #8901.**
- Exact missing-source artifact cho CP gaps + DLL 2,419 key đã được tạo thành công bằng GitHub Actions.

## QUY TẮC BẮT BUỘC: CUỐI MỖI PHIÊN PHẢI PERSIST GITHUB

1. **Một batch chỉ được tính là hoàn thành khi đã có commit SHA trên GitHub.**
2. Trước khi kết thúc mỗi phiên SDS, phải:
   - commit toàn bộ batch đã hoàn thành;
   - cập nhật `CHECKPOINT.json` nếu trạng thái/điểm nối thay đổi;
   - cập nhật `HANDOFF.md` khi cần;
   - ghi rõ exact next index/range để phiên sau nối tiếp.
3. **Không để phần dịch hoàn chỉnh chỉ nằm trong chat.** Nếu bị ngắt giữa batch, batch đó chưa được tính là hoàn thành và phải tiếp tục từ source/recovery ở phiên kế tiếp.
4. Ưu tiên commit theo batch nhỏ-vừa, thường 100 key, để giảm rủi ro mất dữ liệu.

## CHÍNH SÁCH CHỐNG VÒNG LẶP

1. Không dịch lại chỉ vì `translations/cp` thiếu file nếu còn bản đã persist ở nơi khác.
2. Với mọi dải thiếu, kiểm tra theo thứ tự:
   - `recovery/index/`
   - `translations/cp/`
   - git commit history
   - GitHub Actions artifacts/workflow outputs
   - file/handoff persisted từ các phiên trước
3. Nếu recovery shard đã có tiếng Việt, chỉ materialize sang exact key 3.13.4.
4. Nếu dữ liệu thực sự thất lạc sau khi đã vét recovery/history/artifact, được phép làm lại đúng khoảng thất lạc để hoàn thiện file phát hành.
5. Audit missing range phản ánh repo coverage, không tự động đồng nghĩa với chưa từng dịch trong lịch sử.

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
- Uriel: nghiêm, kiêu, trang trọng, đôi lúc cay độc.
- Moore: lạnh, tàn nhẫn, hoa mỹ.
- Hovsep: nhút nhát, mềm, đáng yêu, dễ giật mình, buồn ngủ.
- Lucas: ngọt nhưng nguy hiểm, thông minh, thích trêu.
- Teresa: giữ self-reference `Nunu` khi source dùng đặc điểm đó.
- Shirai: kỳ dị, rờn rợn, thân mật bất an.
- Cupid: hoạt ngôn, đáng yêu, tự tin, mê trà/chuyện phiếm/tình yêu.
- Pelette: cộc, nóng tính, có vết thương quá khứ; mềm hơn ở heart/marriage cao.
- Siren: sôi nổi, tò mò văn hóa loài người, thường tự xưng `chị đây`.
- Wim: bartender thân thiện, hơi sân khấu, thích Xenia, muốn là quý ông đáng tin.

## DLL

- Expected: **2,419 key**.
- Exact DLL source 2,419 key đã được workflow xác định và đưa vào artifact cùng missing CP source.
- Sau khi CP gaps hoàn tất, tiếp tục DLL 1-2419, persist theo cùng quy tắc mỗi batch phải có commit SHA.

## Việc cần làm từ đây

1. Tiếp tục CP từ **#8901**.
2. Hoàn tất toàn bộ CP gaps còn lại và materialize sang `translations/cp`.
3. Refresh full CP audit, mục tiêu 24,827/24,827, 0 token mismatch, 0 Hán tự, 0 unknown.
4. Hoàn tất DLL 2,419 key, persist + QA.
5. Ghép file `vi.json`/cấu trúc i18n cần thiết và build gói release chỉ chứa file Việt hóa.

## Cách bắt đầu ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF mới nhất trên GitHub.`

Assistant phải đọc `HANDOFF.md`, `CHECKPOINT.json`, audit mới nhất và nối từ exact persisted checkpoint, không dựa vào đoạn chat chưa commit.

## Mục tiêu phát hành

Bản cuối chỉ chứa file Việt hóa/cấu trúc cần thiết để chép vào mod gốc, không kèm asset game/mod gốc không cần thiết.
