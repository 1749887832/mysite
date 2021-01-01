from django.db import models


# Create your models here.
class Server(models.Model):
    id = models.AutoField(primary_key=True)
    # server
    server = models.CharField(max_length=128, null=True)


class Modular(models.Model):
    id = models.AutoField(primary_key=True)
    # modular_name
    modular_name = models.CharField(max_length=128, null=True)


class content(models.Model):
    id = models.AutoField(primary_key=True)
    # headers
    headers = models.CharField(max_length=256, null=True)
    # type
    type = models.CharField(max_length=128, null=True)
    # payload
    payload = models.CharField(max_length=1024, null=False)
    # modular_id
    modular_id = models.IntegerField(null=False)


# Create your models here.
class Case_models(models.Model):
    id = models.AutoField(primary_key=True)
    # 用例名称
    case_name = models.CharField(max_length=64, null=True)
    # 测试单id
    single_id = models.IntegerField(null=True)


class Step(models.Model):
    id = models.AutoField(primary_key=True)
    # 接口地址
    request_url = models.CharField(max_length=1024, null=False)
    # 请求参数
    request_data = models.CharField(max_length=8192, null=False)
    # 断言参数
    assert_variable = models.CharField(max_length=1024, null=False)
    # 断言期望
    expect = models.CharField(max_length=1024, null=False)
    # 是否获取参数
    is_globals = models.CharField(max_length=1024, null=False)
    # 参数的字段（必须是后端返回的字段）
    response_variable = models.CharField(max_length=1024, null=True)
    # 使用变量（不可重复）
    use_variable = models.CharField(max_length=1024, null=True)
    # 请求类型
    request_type = models.CharField(max_length=1024, null=False)
    # 结果
    result = models.CharField(max_length=32, null=True)
    # 按照顺序执行
    order_where = models.CharField(max_length=32, null=True)
    # 用例id
    case_id = models.IntegerField(null=False)
