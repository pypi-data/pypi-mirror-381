from dknovautils import commons, iprint_debug, iprint_warn, AT  # type:ignore
from dknovautils.commons import *
import socket

import platform
import subprocess


class DkNetwork:

    @classmethod
    def ping_ip(cls, ip: str) -> bool:
        try:
            # Linux/macOS: '-c 1' 表示发送1个包，Windows: '-n 1'
            param = "-n" if subprocess.os.name == "nt" else "-c"
            command = ["ping", param, "1", ip]
            response = subprocess.call(
                command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            return response == 0  # 返回 0 表示成功
        except Exception as e:
            return False

    @classmethod
    def ping_ip2(cls, ip: str, timeout: int = 5) -> bool:
        """
        检查某个局域网 IP 是否能 ping 通
        :param ip: 要检测的 IP 地址
        :param timeout: 超时时间（秒）
        :return: True 表示可达，False 表示不可达
        """
        # 根据系统选择 ping 命令参数
        param = "-n" if platform.system().lower() == "windows" else "-c"
        # 超时参数
        timeout_param = "-w" if platform.system().lower() == "windows" else "-W"

        try:
            result = subprocess.run(
                ["ping", param, "1", timeout_param, str(timeout), ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return result.returncode == 0
        except Exception:
            return False

    @classmethod
    def http_get_url_simple_str(
        cls,
        url: str,
        encoding: str = "utf-8",
        timeout: float = 5.0,
        verbose: bool = False,
    ) -> str | None:
        """

        https://stackabuse.com/guide-to-sending-http-requests-in-python-with-urllib3/

        """
        _http = urllib3.PoolManager(timeout=timeout)

        try:
            if verbose:
                iprint_debug(f"get url start {url}")
            r = _http.request("GET", url, timeout=timeout, retries=False)
            # print(json.loads(r.data.decode('utf-8')))
            s = r.data.decode(encoding)
            assert isinstance(s, str)
            return s
        except Exception as e:
            iprint_debug(f"err65715 {url} {e}")
            return None
        finally:
            if verbose:
                iprint_debug(f"get url end {url}")


http_get_url_simple_str = DkNetwork.http_get_url_simple_str


def _f_test_http_get_url_simple_str() -> None:
    if True:
        url = "https://www.baidu.com/"
        r = http_get_url_simple_str(url)
        assert r and len(r) > 10

        url = "http://www.baidu.com/"
        r = http_get_url_simple_str(url)
        assert r and len(r) > 10

    url = "http://192.168.0.1/"
    r = http_get_url_simple_str(url)
    print(r)
    assert r and len(r) > 10

    url = "http://192.168.0.2/"
    r = http_get_url_simple_str(url, verbose=True)
    print(r)
    assert r is None

    print("test end")


def http_scan_urls(
    urls: List[str], *, limit: int = 200, timeout: float = 5.0
) -> List[str]:
    """
    顺序返回能正常获取内容的url list。
    limit是限制打印的对应的值的文本长度。没有多大作用。
    实现中是多线程访问网络。

    """
    # port = 9310
    # urls = [f"http://192.168.0.{i}:{port}" for i in range(1, 256)]

    ma = {}

    def fa(url: str) -> None:
        ma[url] = None
        rs = http_get_url_simple_str(url, timeout=timeout)
        ma[url] = rs

    ths = [threading.Thread(target=fa, args=(url,)) for url in urls]

    for t in ths:
        t.start()

    for t in ths:
        t.join()

    ks = list((u, ma[u].strip()[:limit]) for u in ma if ma[u])
    PRE = "*" * 20
    iprint(f"{PRE} f_scan_url good {PRE}")
    for k, v in ks:
        iprint(f"{k} {v}")

    return [k for k, v in ks]


def is_port_open(dst: str, port: int, desc: str = "", timeout: int = 5) -> bool:
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set a timeout of 1 second
    s.settimeout(timeout)
    try:
        # try to connect to the port
        s.connect((dst, port))
        # port is open
        # iprint(f"Port {port} is open")
        return True
    except:
        # port is closed
        # iprint(f"Port {port} is closed")
        return False
    finally:
        # always close the socket
        s.close()
