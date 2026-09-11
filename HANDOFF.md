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

## Trạng thái chính thức

**RELEASE READY.**

Không còn range dịch nào cần tiếp tục trong 3.13.4.

Nếu user nói `tiếp` sau mốc này, không được tự dịch lại. Việc hợp lệ tiếp theo chỉ là:

1. hỗ trợ test bản ZIP trong game;
2. sửa lỗi cụ thể nếu log/gameplay phát hiện;
3. chuẩn bị nội dung Nexus/README/changelog nếu user yêu cầu;
4. update Việt hóa khi Seven Deadly Sins có source version mới.

## Quy tắc persist vẫn giữ nguyên

Mọi fix sau release phải commit GitHub trước khi tính là hoàn thành, đồng thời cập nhật checkpoint/handoff nếu trạng thái thay đổi.
