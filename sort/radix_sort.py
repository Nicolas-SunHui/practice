ori = [52,26,34,48,61,25,48,77,34,56,29]
sort_ge = []
sort_shi = []
basket = [[],[],[],[],[],[],[],[],[],[]]
basket_s = [[],[],[],[],[],[],[],[],[],[]]
for o in ori:
    digit_ge = o % 10
    basket[digit_ge].append(o)
for b in basket:
    for n in b:
        sort_ge.append(n)
for o in sort_ge:
    digit_shi = o // 10
    basket_s[digit_shi].append(o)
for b in basket_s:
    for n in b:
        sort_shi.append(n)
print(sort_shi)