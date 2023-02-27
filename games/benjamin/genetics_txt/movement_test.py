import move_class
import games.benjamin.genetics_txt.app as app

human_1 = app.summon_human(Level=10)

movement_object = move_class.move_class(move_type="forward gab")
print(movement_object.muscle_group)

print("output "+str(movement_object.action(human_1)))
print("\n")
print(human_1.torso_height)
print(human_1.chest_muscle_group)
print(human_1.arm_muscle_group)
print(human_1.size)

human_1.chest_muscle_group = 10000
human_1.arm_muscle_group = 10000
human_1.chest_muscle_group

print("\n")

print("output "+str(movement_object.action(human_1)))
print("\n")
print(human_1.torso_height)
print(human_1.chest_muscle_group)
print(human_1.arm_muscle_group)
print(human_1.size)



human_1.torso_height = 1.5
human_1.size = 1.5

print("\n")

print("output "+str(movement_object.action(human_1)))
print("\n")
print(human_1.torso_height)
print(human_1.chest_muscle_group)
print(human_1.arm_muscle_group)
print(human_1.size)


movement_object.level = 5
print(movement_object.level)
print("output "+str(movement_object.action(human_1)))
#print(human_1.size)
#print(movement_object.action(parent=human_1))