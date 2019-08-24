list_1 = []
def show_menu():
    """菜单界面"""
    print("*" * 22)
    print("欢迎进入名片管理系统！")
    print("\n1.新增名片\n2.查看名片\n3.修改名片\n"
          "0.退出系统\n\n请输入你的选择：")
    print("*" * 22)

show_menu()

def new_card():
    """新增名片"""
    name = input("请输入姓名：")
    num = input("请输入电话")
    qq = input("请输入QQ：")
    card_dict = {}
    card_dict["姓名"] = name
    card_dict["电话"] = num
    card_dict["QQ"] = qq
    list_1.append(card_dict)
    # print(card_dict)
    # return list_1
new_card()

def show_all_card():
    for i in ["姓名","电话","QQ"]:
        print(i,end="\t")
    print()

    for card in list_1:
        print("%s \t%s \t%s \t" % (card['姓名'],card['电话'],card['QQ']))

def deal_card():
    while True:
        print("1.修改   2.删除   0.退出")
        num = int(input("请输入你的选择："))
        if num == 1:
            name_1 = input("你要修改谁的名片")
            for card in list_1:
                if card["姓名"] == name_1:
                    while True:
                        print("1.姓名  2.电话  3.QQ  0.退出")
                        num_1 = int(input("请选择你要修改的内容："))
                        if num_1 == 1:
                            name = input("新的姓名：")
                            card["姓名"] = name
                        elif num_1 == 2:
                            num = input("新的电话：")
                            card["电话"] = num
                        elif num_1 == 3:
                            qq_num = input("新的QQ")
                            card["QQ"] = qq_num
                        elif num_1 == 0:
                            break
                        else:
                            print("输入错误")

        elif num == 2:
            name_1 = input("你要删除谁的名片")
            for card in list_1:
                if card["姓名"] == name_1:
                    list_1.remove(card)
                    break
        elif num == 0:
            break
        else:
            print("输入错误，请重新输入：")




