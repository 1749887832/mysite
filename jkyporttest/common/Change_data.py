class Change_data:
    def __init__(self):
        super().__init__()

    def Changes_data(self, chang_data, data_dict):
        # 替换的请求参数中的true或者false，因为true或false是python中的关键字，会导致错误
        if 'true' in chang_data:
            chang_data = chang_data.replace('true', 'True')
        if 'false' in chang_data:
            chang_data = chang_data.replace('false', 'False')
        # 替换掉请求参数中使用的变量
        for i in data_dict:
            if i in chang_data:
                chang_data = chang_data.replace(i, str(data_dict[i]))
        return eval(chang_data)
