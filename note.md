-----

- [参考链接](https://github.com/626626cdllp/Test/blob/master/Test_framework/test/common/browser.py)
- [参考链接](https://www.jianshu.com/p/b87ec158aad8)
- [参考链接](https://my.oschina.net/u/3041656/blog/820023)
- [参考链接](https://blog.csdn.net/cyjs1988/article/details/75570579)


- 安装allure-pytest包
- 生成xml报告  'allure generate %s -o %s' % (XML_REPORT_PATH, HTML_REPORT_PATH)
- allure 打开测试报告 allure open -h 127.0.0.1 -p 8083 ./report/

## pytest的装饰器
```
@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
(变量的名称，对应参数元组的数组，id的数组)
@pytest.fixture
pytest --durations=3 统计每个用例执行的时间
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@pytest.mark.flaky(reruns=5, reruns_delay=2)
指定用例失败重试 reruns：重试次数，reruns_delay:重试间隔时间
@pytest.mark.run(order=1) 指定运行顺序 order从小到大
@pytest.mark.P0  指定运行级别 pytest -v -m "P0"

https://mp.weixin.qq.com/s?__biz=MzAwNjEzMDUyNw==&mid=2650199814&idx=2&sn=f14ddce5a97d19a370c4d33f8d74507f
https://github.com/xinxi1990/atxdemo/blob/master/conftest.py

```


## allure的装饰器
```
@allure.feature("aaa") 功能块
@allure.story("bbb") 功能块
@allure.step("步骤一") 测试步骤
@allure.severity("critical") 优先级blocker, critical, normal, minor, trivial共五个等级
@allure.issue("BUG号：123") bug号，问题表识，关联标识已有的问题，可为一个url链接地址
@allure.testcase("用例名：测试字符串相等") 用例标识，关联标识用例，可为一个url链接地址
    allure.attach 可对中间测试的某个结果保存下来，便于追溯
    allure.attach("str_add返回结果", "{0}".format(res))
    allure.environment(host="172.6.12.27", test_vars=paras)

pytest.main(['--allure_stories=测试模块_demo1, 测试模块_demo2', '--allure_severities=critical, blocker'])
可对指定的模块或者优先级进行测试

```


### pytest扩展

```
pytest-django: 针对Django框架的单测框架
pytest-twisted: 针对twisted框架的单测框架
pytest-cov: 产生覆盖率报告
pytest-instafail: 发送错误时报告错误信息
pytest-bdd 测试驱动开发工具
pytest-konira 测试驱动开发工具
pytest-timeout: 支持超时功能
pytest-pep8: 支持PEP8检查
pytest-flakes: 结合pyflakes进行代码检查
pytest-randomly:测试顺序随机
pytest-xdist: 分布式测试
pytest-instafail: 出错立即返回
pytest-rerunfailures:
```