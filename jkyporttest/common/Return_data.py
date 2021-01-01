class Return_msg:
    # 处理用户需要存储的变量
    def return_msg(self, data, need_data):
        # print(data, need_data)
        if need_data in [k for k, v in data.items()]:
            return data[need_data]
        elif need_data in [k for k, v in data['data'].items()]:
            return data['data'][need_data]
        elif need_data in [k for k, v in data['data']['list'][0].items()]:
            return data['data']['list'][0][need_data]
        elif need_data in [k for k, v in data['data']['extend']]:
            return data['data']['extend'][need_data]
        else:
            return 'error'
