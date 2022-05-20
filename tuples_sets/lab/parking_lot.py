# n = int(input())
#
# parking_lot_logs = [input().split(', ') for _ in range(n)]
#
# parking_lot = set()
#
# for direction, car_number in parking_lot_logs:
#     if direction == 'IN':
#         parking_lot.add(car_number)
#     elif car_number in parking_lot:
#         parking_lot.remove(car_number)
#
# if parking_lot:
#     [print(car_number) for car_number in parking_lot]
# else:
#     print('Parking Lot is Empty')
#
#

n = int(input())

parking_lot_logs = [input().split(', ') for _ in range(n)]
print(parking_lot_logs)
parking_lot = set()

for direction, car_number in parking_lot_logs:
    if direction == 'IN':
        parking_lot.add(car_number)
    elif car_number in parking_lot:
        parking_lot.remove(car_number)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')
