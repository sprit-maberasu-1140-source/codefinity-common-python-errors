def add_item_to_lists(target_list, other_list, item):
    # もし target_list と other_list が同じリストなら…
    if target_list is other_list:
        # target_list をコピーして別のリストにする
        target_list = list(target_list)
    # item を target_list にだけ追加する
    target_list.append(item)
    # ２つのリストを表示する
    print(f"Target list: {target_list}")
    print(f"Other list: {other_list}")

a = [1, 2, 3]
b = a
add_item_to_lists(a, b, 99)