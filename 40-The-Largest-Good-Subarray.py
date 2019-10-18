"""
====BIBEK====
Problem Code: LGOODSUB
====BIBEK====
"""


def sub_array():

    final_array = []

    sub_arr_lst = []

    no_of_arrays = int(input("Enter the no. of arrays : "))

    while True:
        if (no_of_arrays <= 0) | (no_of_arrays > 10) | (no_of_arrays == ""):
            print("Input Error|Limit Exceed or Blank Input")
            break
        else:
            for val in range(0, no_of_arrays):
                arr = input("Enter the array elements : ")
                lst = list(map(int, arr))
                final_array.append(lst)
        for i in range(0, no_of_arrays):
            len_fa = len(final_array[i])
            if len_fa > 0 & len_fa < 10**5:
                for k in range(0, 4):
                    for j in range(0, len_fa - 2):
                        if final_array[i][len_fa - (j+1)] < final_array[i][k + 1]:
                            sub_arr_len = ((len_fa - (j + 1)) - (k + 1)) + 1
                            sub_arr_lst.append(sub_arr_len)
            rev_array = list(reversed(final_array))
            if len_fa > 0 & len_fa < 10**5:
                for k in range(0, 4):
                    for j in range(0, len_fa - 2):
                        if rev_array[i][len_fa - (j+1)] < rev_array[i][k + 1]:
                            sub_arr_len = ((len_fa - (j + 1)) - (k + 1)) + 1
                            sub_arr_lst.append(sub_arr_len)

                for k in range(0, int(len_fa/2)):
                    if rev_array[i][len_fa - (k + 2)] < rev_array[i][k + 1]:
                        sub_arr_len = ((len_fa - (k + 2)) - (k + 1)) + 1
                        sub_arr_lst.append(sub_arr_len)

            result = max(sub_arr_lst)
            print("Largest good subarray in case", i+1, " is ", result)


sub_array()

