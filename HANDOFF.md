# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Nguồn sự thật cho các phiên sau. CP và DLL đều đã hoàn tất sạch. Mục tiêu hiện tại chỉ còn đóng gói bản phát hành.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Source đã chốt

- Mod: Seven Deadly Sins 1.6
- Version: **3.13.4**
- Nexus file ID: **178657**
- CP default: **24,827 key**
- DLL default: **2,419 key**
- Exact CP source:
  `downloads/Nexus/15/15100/178657/Seven Deadly Sins 1.6/[CP] Seven Deadly Sins/i18n/default.json`
- Exact DLL source:
  `downloads/Nexus/15/15100/178657/Seven Deadly Sins 1.6/SevenDeadlySins/i18n/default.json`
- Cấu trúc/key/order luôn theo exact source 3.13.4.

## CP - DONE

Canonical commit:

`2ca310f` - `Finalize canonical CP translation and clean audit`

Kết quả `audit/CP_AUDIT.json`:

- **24,827 / 24,827 key covered**
- missing: **0**
- duplicate: **0**
- unknown: **0**
- technical token mismatch: **0**
- Hán tự: **0**

Canonical CP nằm tại `translations/cp/`.

**Không quay lại dịch CP**, trừ khi source mod có version mới.

## DLL - DONE

Toàn bộ DLL đã được dịch tuần tự và persist tới **#2,419 / 2,419**.

Final canonical commit:

`c2e0461693e423785a6dc4ea44eb5fc430b84949` - `Finalize canonical DLL Vietnamese and clean audit`

Canonical DLL:

`translations/dll/vi.json`

Kết quả `audit/DLL_AUDIT.json`:

- **2,419 / 2,419 index covered**
- missing: **0**
- duplicate: **0**
- conflicting duplicate: **0**
- unknown: **0**
- technical token mismatch: **0**
- Hán tự: **0**

**Không quay lại dịch DLL**, trừ khi source mod có version mới.

## QUY TẮC BẮT BUỘC: PERSIST GITHUB

1. Một phần việc chỉ được tính là hoàn thành khi đã có commit SHA trên GitHub.
2. Trước khi kết thúc mỗi phiên SDS phải cập nhật `CHECKPOINT.json` và `HANDOFF.md` nếu trạng thái thay đổi.
3. Không để phần hoàn chỉnh chỉ nằm trong chat.
4. Khi đóng gói release, phải persist cấu trúc/package hoặc workflow tạo package vào repo trước khi gọi là hoàn thành.

## Quy tắc dịch/QA vẫn giữ nguyên

1. Tiếng Việt tự nhiên như hội thoại game.
2. Giữ cá tính NPC.
3. Tên nhân vật Latin, không để Hán tự trong target.
4. Không thêm/bớt token kỹ thuật: `@`, `$...`, `#$b#`, `$q/$r`, `{{...}}`, `[SDS_...]`, `%...`, `^`, `|...|`, item ID và token khác.
5. QA bằng token skeleton đúng thứ tự + quét Hán tự.

## Giọng nhân vật quan trọng

- Lane: ngọt, láu lỉnh, thương nhân, hơi flirt; self-reference `La` khi source dùng.
- Rane: sắc hơn Lane, trêu/chọc, hơi chiếm hữu; `Ra` theo ngữ cảnh source.
- Sariel: lịch sự, kiêu hãnh, ngọt có gai.
- Uriel: nghiêm, kiêu, trang trọng, đôi lúc cay độc; thường `ta / ngươi`, mềm dần ở heart cao.
- Moore: lạnh, tàn nhẫn, hoa mỹ.
- Hovsep: nhút nhát, mềm, đáng yêu, dễ giật mình, buồn ngủ.
- Lucas: ngọt nhưng nguy hiểm, thông minh, thích trêu.
- Teresa: giữ self-reference `Nunu` khi source dùng.
- Shirai: kỳ dị, rờn rợn, thân mật bất an.
- Cupid: hoạt ngôn, đáng yêu, tự tin, mê trà/chuyện phiếm/tình yêu.
- Pelette: cộc, nóng tính, có vết thương quá khứ; mềm hơn ở heart/marriage cao.
- Siren: sôi nổi, tò mò văn hóa loài người, thường tự xưng `chị đây`.
- Wim: bartender thân thiện, hơi sân khấu, thích Xenia, muốn là quý ông đáng tin.

## PHASE HIỆN TẠI - RELEASE PACKAGING

Không còn key nào cần dịch trong source 3.13.4.

Việc tiếp theo:

1. Xác định chính xác đường dẫn cài đặt của hai file i18n trong mod gốc:
   - `[CP] Seven Deadly Sins/i18n/vi.json`
   - `SevenDeadlySins/i18n/vi.json`
2. Materialize CP canonical thành một `vi.json` theo đúng key/order source.
3. Dùng `translations/dll/vi.json` cho phần DLL.
4. Build gói localization-only, không kèm asset gốc/mod gốc không cần thiết.
5. Kiểm tra JSON parse, số key và đường dẫn trong ZIP.
6. Persist workflow/source package và bản archive phát hành.

## Cách bắt đầu ở chat mới

Người dùng chỉ cần nói:

> `Tiếp tục Seven Deadly Sins từ HANDOFF mới nhất trên GitHub.`

Assistant phải đọc `HANDOFF.md`, `CHECKPOINT.json`, `audit/CP_AUDIT.json`, `audit/DLL_AUDIT.json` và tiếp tục **đóng gói release**, không dịch lại CP/DLL.

## Điểm nối chính xác

**CP DONE. DLL DONE. Tiếp tục từ release packaging.**
