import tool

while True :
    tool.show_menu()
    opt = int(input("你的选择是："))
    if opt in [1,2,3,4,0]:
        if opt == 1:
            tool.new_card()
            # for card in cards_dict:
            #     print(cards_dict)

        elif opt == 2:
            tool.show_all_card()
        elif opt == 3:
            tool.deal_card()
        elif opt == 4:
            pass
        elif opt == 0:
            break
        else:
            print("输入错误，请重新输入！")