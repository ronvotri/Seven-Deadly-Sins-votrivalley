# HANDOFF - Seven Deadly Sins Vietnamese Localization

> **Seven Deadly Sins 3.13.4 Việt hóa đã hoàn tất, audit sạch và đóng gói xong. Không tiếp tục dịch lại nếu không có lỗi test hoặc source version mới.**

## Repo

`ronvotri/Seven-Deadly-Sins-votrivalley`

## Source

- Mod: Seven Deadly Sins 1.6
- Version: **3.13.4**
- Nexus file ID: **178657**
- CP source: **24,827 key**
- DLL source: **2,419 key**

## CP - DONE

Canonical commit: `2ca310f`

`audit/CP_AUDIT.json`:

- 24,827 / 24,827 covered
- missing 0
- duplicate 0
- unknown 0
- token mismatch 0
- Hán tự 0

## DLL - DONE

Canonical commit:

`c2e0461693e423785a6dc4ea44eb5fc430b84949`

Canonical file:

`translations/dll/vi.json`

`audit/DLL_AUDIT.json`:

- 2,419 / 2,419 covered
- missing 0
- duplicate 0
- conflicting duplicate 0
- unknown 0
- token mismatch 0
- Hán tự 0

## RELEASE - DONE

Release commit:

`cac241011ff8e0eb15d8902ed94b06e78006bfa7`

Archive trong repo:

`dist/Seven-Deadly-Sins-3.13.4-Vietnamese-Localization.zip`

GitHub Actions artifact ID:

`10187640215`

ZIP đã được build và mở lại để xác minh. Nó chỉ chứa đúng hai file Việt hóa:

1. `Seven Deadly Sins 1.6/[CP] Seven Deadly Sins/i18n/vi.json`
2. `Seven Deadly Sins 1.6/SevenDeadlySins/i18n/vi.json`

Số key thực tế trong ZIP:

- CP `vi.json`: **24,827**
- DLL `vi.json`: **2,419**

Không kèm asset gốc hoặc file mod gốc không cần thiết.

## Trạng thái chính thức của Việt hóa

**RELEASE READY.**

Không còn range dịch nào cần tiếp tục trong 3.13.4.

Nếu user nói `tiếp` trong ngữ cảnh Việt hóa, không được tự dịch lại. Việc hợp lệ chỉ là:

1. hỗ trợ test bản ZIP trong game;
2. sửa lỗi cụ thể nếu log/gameplay phát hiện;
3. chuẩn bị nội dung Nexus/README/changelog nếu user yêu cầu;
4. update Việt hóa khi Seven Deadly Sins có source version mới.

---

# COMPATIBILITY RESEARCH - IN PROGRESS

User hiện đang nghiên cứu khả năng chơi đồng thời:

- Seven Deadly Sins 3.13.4
- East Scarp 3.0.9
- Stardew Valley Expanded
- Ridgeside Village
- Pelipper Town + optional compatibility files
- StarCrossed

Hồ sơ nghiên cứu chuẩn:

`compatibility/SDS-EastScarp-SVE-RESEARCH.md`

Research checkpoint commit:

`d718a376f70ef6d52c34420a2c16f6da9dc89130`

## East Scarp đã xác minh

Từ archive East Scarp 3.0.9 do user cung cấp:

- East Scarp **có patch trực tiếp `Maps/Town` khi không cài SVE**.
- Asset patch liên quan: `assets/Patches/Town_ES.tmx`.
- Vùng patch đã quan sát:
  - X = 109
  - Y = 63
  - Width = 21
  - Height = 14
- Warp ở mép đông Town quan sát quanh:
  - X ≈ 120
  - Y ≈ 72–75
  - destination `EastScarp_Crossing`

### Điểm cực kỳ quan trọng về SVE

East Scarp Town patch nói trên có điều kiện tương đương:

`HasMod FlashShifter.StardewValleyExpandedCP = false`

Tức là **khi có SVE, East Scarp không dùng entrance vanilla ở mép phải Pelican Town theo cách trên**.

Đã thấy route SVE-aware:

`Custom_ShearwaterBridge -> EastScarp_Village`

Vì vậy phải tách riêng hai trường hợp:

1. `SDS + East Scarp` không có SVE;
2. `SDS + East Scarp + SVE`.

Không được kết luận hai trường hợp giống nhau.

## Pelipper compatibility files

Các file kiểu:

- `PelipperTown.RidgesideVillage`
- `PelipperTown.SVE`
- `PelipperTown.EastScarp`
- `PelipperTown.StarCrossed`

chỉ giải quyết **Pelipper Town ↔ expansion tương ứng**.

Chúng **không phải** patch cho `SDS ↔ East Scarp` hay `SDS ↔ SVE`.

## SDS map extraction đang thực hiện

Repo Việt hóa không giữ toàn bộ asset/map gốc SDS, nên exact source SDS 3.13.4 đang được extract lại từ đúng SMAPI dataset/Nexus file `178657`.

Workflow:

`.github/workflows/sds-extract-map-compat.yml`

Trigger commit:

`42977829ac9a7d65c1a14b5f0bf60db4df78e2ca`

Initial run ID:

`34609160529`

## Điểm resume chính xác

**Không dịch lại. Không nghiên cứu East Scarp từ đầu.**

Khi tiếp tục:

1. mở `compatibility/SDS-EastScarp-SVE-RESEARCH.md`;
2. kiểm kết quả workflow extract SDS 3.13.4;
3. tìm tất cả patch SDS đụng `Maps/Town`, Town/warp/tile property và các location liên quan;
4. ghi chính xác `FromArea` / `ToArea` hoặc vùng patch SDS;
5. đối chiếu với East Scarp `X109 Y63 W21 H14`;
6. kiểm riêng trường hợp có SVE vì East Scarp chuyển route sang Shearwater Bridge;
7. sau đó mới kết luận:
   - không cần patch;
   - chỉ cần patch warp;
   - cần map compatibility patch;
   - hoặc xung đột lớn hơn.

Nếu cần patch, làm thành **mod compatibility riêng**, không sửa trực tiếp file Việt hóa.

## Quy tắc persist vẫn giữ nguyên

Mọi phát hiện compatibility đã xác minh hoặc patch hoàn thành phải commit GitHub trước khi tính là hoàn thành. Cuối mỗi phiên phải cập nhật lại `CHECKPOINT.json`, `HANDOFF.md` và file nghiên cứu compatibility nếu trạng thái thay đổi.
