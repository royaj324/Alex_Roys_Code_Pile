positions = [[3, 4], [5, 7]]
velocities = []
for pos, time in positions:
    velocity=float(pos/time)
    velocities.append(velocity)

print(velocities)