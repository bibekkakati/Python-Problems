"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. The red region
denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the
orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point ,
and the orange tree is at point .

link : https://www.hackerrank.com/challenges/apple-and-orange/problem

When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value
of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.

Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in
the inclusive range )?
"""


def fruits_count(startPointHouse, endPointHouse, appleTreePoint, orangeTreePoint, md_apples, nd_orange):
    count_apples = 0
    count_oranges = 0
    for i in md_apples:
        if (i + appleTreePoint >= startPointHouse) & (i + appleTreePoint <= endPointHouse):
            count_apples += 1
    for j in nd_orange:
        if (j + orangeTreePoint >= startPointHouse) & (j + orangeTreePoint <= endPointHouse):
            count_oranges += 1
    print(count_apples, " apples")
    print(count_oranges, " oranges")


fruits_count(int(input("HOUSE START POINT: ")),
             int(input("HOUSE END POINT: ")),
             int(input("APPLE TREE POINT: ")),
             int(input("ORANGE TREE POINT: ")),
             [2, -4, 3], [-8, 6, -2])
