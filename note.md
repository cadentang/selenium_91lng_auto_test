-----

- [�ο�����](https://github.com/626626cdllp/Test/blob/master/Test_framework/test/common/browser.py)
- [�ο�����](https://www.jianshu.com/p/b87ec158aad8)
- [�ο�����](https://my.oschina.net/u/3041656/blog/820023)
- [�ο�����](https://blog.csdn.net/cyjs1988/article/details/75570579)


- ��װallure-pytest��
- ����xml����  'allure generate %s -o %s' % (XML_REPORT_PATH, HTML_REPORT_PATH)
- allure �򿪲��Ա��� allure open -h 127.0.0.1 -p 8083 ./report/

## pytest��װ����
```
@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
(���������ƣ���Ӧ����Ԫ������飬id������)
@pytest.fixture
pytest --durations=3 ͳ��ÿ������ִ�е�ʱ��
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@pytest.mark.flaky(reruns=5, reruns_delay=2)
ָ������ʧ������ reruns�����Դ�����reruns_delay:���Լ��ʱ��
@pytest.mark.run(order=1) ָ������˳�� order��С����
@pytest.mark.P0  ָ�����м��� pytest -v -m "P0"

https://mp.weixin.qq.com/s?__biz=MzAwNjEzMDUyNw==&mid=2650199814&idx=2&sn=f14ddce5a97d19a370c4d33f8d74507f
https://github.com/xinxi1990/atxdemo/blob/master/conftest.py

```


## allure��װ����
```
@allure.feature("aaa") ���ܿ�
@allure.story("bbb") ���ܿ�
@allure.step("����һ") ���Բ���
@allure.severity("critical") ���ȼ�blocker, critical, normal, minor, trivial������ȼ�
@allure.issue("BUG�ţ�123") bug�ţ������ʶ��������ʶ���е����⣬��Ϊһ��url���ӵ�ַ
@allure.testcase("�������������ַ������") ������ʶ��������ʶ��������Ϊһ��url���ӵ�ַ
    allure.attach �ɶ��м���Ե�ĳ�������������������׷��
    allure.attach("str_add���ؽ��", "{0}".format(res))
    allure.environment(host="172.6.12.27", test_vars=paras)

pytest.main(['--allure_stories=����ģ��_demo1, ����ģ��_demo2', '--allure_severities=critical, blocker'])
�ɶ�ָ����ģ��������ȼ����в���

```


### pytest��չ

```
pytest-django: ���Django��ܵĵ�����
pytest-twisted: ���twisted��ܵĵ�����
pytest-cov: ���������ʱ���
pytest-instafail: ���ʹ���ʱ���������Ϣ
pytest-bdd ����������������
pytest-konira ����������������
pytest-timeout: ֧�ֳ�ʱ����
pytest-pep8: ֧��PEP8���
pytest-flakes: ���pyflakes���д�����
pytest-randomly:����˳�����
pytest-xdist: �ֲ�ʽ����
pytest-instafail: ������������
pytest-rerunfailures:
```