def 生成可注册银行卡(bankName='', bankBin='', lastNumberIsEven=''):

    bankCardInfo = {}
    if bankName == '' and bankBin == '':
        # print("随机生成银行卡")
        # 没指定银行名称和卡Bin，随机生成
        i = len(cardbin_list)
        # print(cardbin_list[695])
        j = random.randint(0,i-1)
        # print(cardbin_list[j])
        cardno = cardbin_list[j]['id'] + random_digi_str(cardbin_list[j]['bankcard_length'] - len(cardbin_list[j]['id']))
        bankname = cardbin_list[j]['bank_name']
        bankcode = cardbin_list[j]['bank_code']
        bankCardInfo['bankCardNo'] = cardno
        bankCardInfo['bankName'] = bankname
        bankCardInfo['bankCode'] = bankcode
    elif bankName:
        # 指定了银行名称，生成特定银行的银行卡
        # print("指定银行名称")
        for bankBinInfo in cardbin_list:
            if bankBinInfo['bank_name'] == bankName:
                if bankBin:
                    # 如果也传了卡bin，判断银行名称与卡bin是否一致
                    if bankBinInfo['id'] == bankBin:
                        cardno = bankBin + random_digi_str(bankBinInfo['bankcard_length'] - len(bankBinInfo['id']))
                        bankCardInfo['bankCardNo'] = cardno
                        bankCardInfo['bankName'] = bankName
                        bankCardInfo['bankCode'] = bankBinInfo['bank_code']
                        break
                else:
                    cardno = bankBinInfo['id'] + random_digi_str(bankBinInfo['bankcard_length'] - len(bankBinInfo['id']))
                    bankCardInfo['bankCardNo'] = cardno
                    bankCardInfo['bankName'] = bankName
                    bankCardInfo['bankCode'] = bankBinInfo['bank_code']

        if bankCardInfo == {}:
            if bankBin == '':
                return "请传入正确的银行名称"
            else:
                return "卡bin与银行名称不一致"

    elif bankBin:
        # 指定卡Bin
        # print("指定卡Bin")
        for bankBinInfo in cardbin_list:
            if bankBinInfo['id'] == bankBin:
                if bankName:
                    # 如果也传了银行名称，则判断卡bin与银行名称是否对应
                    if bankBinInfo['bank_name'] == bankName:
                        cardno = bankBin + random_digi_str(bankBinInfo['bankcard_length'] - len(bankBinInfo['id']))
                        cardCode = bankBinInfo['bank_code']
                        bankCardInfo['bankCardNo'] = cardno
                        bankCardInfo['bankName'] = bankName
                        bankCardInfo['bankCode'] = cardCode
                        break
                    else:
                        return "卡bin与银行名称不一致"
                else:
                    # 只传了卡bin
                    cardno = bankBin + random_digi_str(bankBinInfo['bankcard_length'] - len(bankBinInfo['id']))
                    bankCardInfo['bankCardNo'] = cardno
                    bankCardInfo['bankName'] = bankBinInfo['bank_name']
                    bankCardInfo['bankCode'] = bankBinInfo['bank_code']
                    break

        if bankCardInfo == {}:
            return "请传入正确的银行卡Bin"

    if lastNumberIsEven == "1":
        # 生成偶数结尾的银行卡
        # print("生成偶数结尾的银行卡")
        # print(bankCardInfo)
        if int(bankCardInfo['bankCardNo'][-1]) % 2 == 0:
            pass
        else:
            while True:
                i = random.randrange(0, 10)
                if i % 2 == 0:
                    bankCardInfo['bankCardNo'] = bankCardInfo['bankCardNo'][:-1] + str(i)
                    break
    elif lastNumberIsEven == "2":
        # 生成奇数结尾的银行卡
        # print("生成奇数结尾的银行卡")
        # print(bankCardInfo)
        if int(bankCardInfo['bankCardNo'][-1]) % 2 == 0:
            while True:
                i = random.randrange(0, 10)
                if i % 2 != 0:
                    bankCardInfo['bankCardNo'] = bankCardInfo['bankCardNo'][:-1] + str(i)
                    break
    logger.info("生成银行卡信息：{}".format(bankCardInfo))
    return bankCardInfo

if __name__ == '__main__':
    # first_6 = ''
    # while  '621771' not in first_6:
    card_info = 生成可注册银行卡(bankName='', bankBin='', lastNumberIsEven='')
    print("随机生成可注册卡信息:",card_info)
    # first_6 = card_info[0]
    # random_digi_str(5)