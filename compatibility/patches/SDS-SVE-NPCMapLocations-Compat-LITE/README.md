# SDS x SVE x NPC Map Locations Compatibility LITE

Bản rút gọn ưu tiên ổn định sau chuỗi TEST1-TEST8.

## Giữ lại

- Town minimap calibration đã test ổn.
- `VotriValley.SDS_BridgeCorridor` cho hành lang cầu nhỏ trong Town.
- `VotriValley.SDS_EastTown` cho khu Joja/nhà thờ.
- `MoveEntries` để custom WorldPositions được xét trước `Default`.

## Cố tình không sửa

- `Custom_ShearwaterBridge`.
- map thật / terrain / Buildings.
- warp / route East Scarp.
- minimap ngoài Town.

## Known limitation

Marker trên `Custom_ShearwaterBridge` có thể vẫn lệch theo tọa độ SVE gốc. Đây chỉ là lỗi hiển thị minimap. User quyết định chấp nhận giới hạn này thay vì tiếp tục can thiệp sâu vào `Data/WorldMap`.

## Cài đặt

1. Xóa toàn bộ các pack `SDS-SVE-NPCMapLocations-Compat-TEST1` đến `TEST8` nếu còn cài.
2. Chỉ cài folder `[CP] SDS-SVE-NPCMapLocations-Compat-LITE`.
3. Giữ SDS, Stardew Valley Expanded, NPC Map Locations và Content Patcher như bình thường.
4. Restart game hoàn toàn.

## Runtime findings được giữ lại

- Town WorldPositions có thứ tự; custom entries cần nằm trước `Default`.
- TEST5 xác nhận `SDS_BridgeCorridor` match tại Town `(62,54)`, `(69,53)`, `(74,54)`.
- TEST6 sửa lại `Default MapPixelArea` từ SVE wide mapping `X588 Y184 Width388 Height320` về calibration runtime `X588 Y184 Width180 Height320`.
- Phần Town phía bên kia cầu nhỏ sau đó được user xác nhận hết lỗi.
- `Custom_ShearwaterBridge` vẫn báo runtime pixel area gốc SVE `X1000 Y360 Width172 Height40`; TEST7/8 không tạo thay đổi đáng tin cậy nên bridge override bị loại khỏi LITE.

## Không tự động mở lại minimap research

Chỉ quay lại sửa Shearwater/minimap nếu user chủ động yêu cầu. Không dùng lại TEST1-TEST8 làm bản phát hành.
