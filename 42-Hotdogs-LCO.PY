"""
Jack bought 400 hotdogs for the school picnic. If they were contained in packages of 8 hotdogs, how many total packages did he buy?
Write the program without using / or % operator.
"""

total_hotdogs = 400

hotdogs_pack = 8

total_packages = 0

for i in range(1, total_hotdogs):
    temp = hotdogs_pack * i
    if(temp <= total_hotdogs):
        total_packages += 1
    else:
        break

print(total_packages)